       real*4 data(1440,400),datain(1440,400)
       real lon
       real lat
       CHARACTER*1     cvarin (4), cvar (4)
C
       EQUIVALENCE (cvarin, varin)
       EQUIVALENCE (cvar,   var)

       open(10,file='3B42_daily.2009.05.31.7.bin',
     +     access='DIRECT',status='OLD',recl=1440*400*4)
c
       read(10,rec=1)datain
c
C       This part is for Little Endian machine
C (The data was written in Big Endian).
C       Now that the data has been read into the array, swap
C       the byte order.
C
        DO i = 1, 1440
            DO j = 1, 400
                varin = datain (i, j)
                cvar (1) = cvarin (4)
                cvar (2) = cvarin (3)
                cvar (3) = cvarin (2)
                cvar (4) = cvarin (1)
                data (i, j) = var
            END DO
        END DO
c
c
c
       do 15 jj=1,400
       do 15 ii=1,1440
       if (ii <= 720) then
       lon = 0.125 + 0.25*(ii-1)
       else
       lon = 0.125 + 0.25*(ii-1) - 360.0
       endif
       lat = -49.875+0.25*(jj-1)
       write(*,*)lon,lat,data(ii,jj)
15     continue
c
       close(10)
c
       end

