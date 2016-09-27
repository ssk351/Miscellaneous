#!/bin/bash
for year in {2006..2006}
do
		for dd in {153..275}
			do
				cd ${year}/${dd}/
          cp ../../swath2grid.sh .
          rm -rf swath.out
					bsub -q "cccr-res" -W 720:00 -J "swath_${year}_${dd}" -o "swath.out" < ./swath2grid.sh
				cd -
			done
done
