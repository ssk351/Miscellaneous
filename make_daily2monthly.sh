#!/bin/bash
set -e
maxprocs=32
queue="cccr-res"
files=""
years=""
months="1/12"

sizeof() { echo $#; }

while getopts 'n:y:m:' flag; do
	case "${flag}" in
		n) files="$OPTARG" ;;
    y) years="$OPTARG" ;;
    m) months="$OPTARG" ;;
    *) error "Unexpected option ${flag}" ;;
	esac
done

if [[ -z $files || -z $years || -z $months ]]; then
	echo Usage examples:
	echo $0 -n filename_without_timestamp -y startyear/endyear -m startmonth/endmonth
	echo $0 -n filename_without_timestamp -y year1,year2,year3,.. -m month1,month2,month3,..
fi

if [[ $years == *"/"* ]]; then
	yearstart=$(echo $years | awk -F"/" '{print $1}')
	yearend=$(echo $years | awk -F"/" '{print $2}')
  yearlist=$(seq $yearstart $yearend)
else
	yearlist=$years
fi

if [[ $months == *"/"* ]]; then
  monthstart=$(echo $months | awk -F"/" '{print $1}')
  monthend=$(echo $months | awk -F"/" '{print $2}')
  monthlist=$(seq $monthstart $monthend)
else
  monthlist=$months
fi

ny=$(sizeof $yearlist)
nm=$(sizeof $monthlist)
nf=$(sizeof $files)

totn=$((ny*nm*nf))

nprocs=$maxprocs

if [ $totn -le $nprocs ]; then
	nprocs=$totn
  workperproc=1
  residue=0
else
	workperproc=$((totn/nprocs))
	residue=$((totn%nprocs))
fi

fulllist=""

for file in $files; do
	for yy in $yearlist; do
		for mon in $monthlist; do
      mm=$(printf "%02d" $mon)
      yyyy=$(printf "%04d" $yy)
		  fulllist="$fulllist	${file}_${yyyy}_${mm}"
		done
	done
done

listarray=(`echo ${fulllist}`)

nfilesdone=0

echo ${listarray[0]}

for proc in $(seq 1 $nprocs); do
	tmpfile=$(mktemp --suffix=".sh")
  nwork=$workperproc
  if [ $proc -le $residue ]; then
		nwork=$((nwork+1))
	fi
	for n in $(seq 1 $nwork); do
		file=${listarray[$nfilesdone]}
    nfilesdone=$((nfilesdone+1))
    nls=$(sizeof $(ls ${file}*.nc))
    if [ $nls -lt 28 ]; then
			echo "$file - Do not have atleast 28 days of file to make monthly mean."
      echo Skipping
      continue
		fi
    mkdir -p monthly
	  echo "ncra -O ${file}*.nc monthly/${file}.nc" >> $tmpfile
	done
  if [[ -s $tmpfile ]]; then
		bsub -q $queue -J "monthly_$file" -o "monthly.out" < $tmpfile
  fi
done

# ./make_daily2monthly.sh -n atm3d_ps -y 1856/1856 
