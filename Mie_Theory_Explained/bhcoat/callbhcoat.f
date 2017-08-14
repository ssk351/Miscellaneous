      PROGRAM CALLBHCOAT
      IMPLICIT UNDEFINED(A-Z)
C Local variables:
      INTEGER INPIND
      REAL PI,RADCOR,RADMAN,REFMED,WAVEL
      COMPLEX EPSCOR,EPSMAN
C Variables passed to subroutine:
      REAL QBACK,QEXT,QSCA,XCOR,XMAN
      COMPLEX REFCOR,REFMAN
C***********************************************************************
C Program to compute optical properties of coated spheres using
C subroutine BHCOAT from Bohren & Huffman
C
C History:
C 90/10/11 (BTD) Modified structure of CALLBHCOAT
C 92/11/24 (BTD) Explicit declaration of all variables
c    ******************************************************************
C
C Caution:
c     BHCOAT should not be used for large, highly absorbing coated
c     spheres.
c     x*refim1, x*refim2, and y*refim2 should be less than about 30.
c
C REFMED = (real) refractive index of surrounding medium
C***********************************************************************
      PI=4.*ATAN(1.)
      REFMED=1.0
C Specify whether to supply refractive index by hand or to obtain it
C using subroutine INDEX
      WRITE(*,*)'WISH TO SPECIFY REF.INDICES (0) OR DIEL.CONST (1)?'
      READ(*,*)INPIND
 0050 WRITE(*,*)'ENTER RADIUS OF CORE (PHYSICAL UNITS) (0 to stop)'
      READ(*,*)RADCOR
      IF(RADCOR.LE.0.)STOP
      WRITE(*,*)'ENTER RADIUS OF MANTLE (PHYSICAL UNITS)'
      READ(*,*)RADMAN
 0100 WRITE(*,*)'ENTER WAVELENGTH (PHYSICAL UNITS) (0 to change size)'
      READ(*,*)WAVEL
      IF(WAVEL.LE.0.)GOTO 0050
      IF(INPIND.EQ.0)THEN
         WRITE(*,*)'ENTER COMPLEX REFRACTIVE INDEX OF CORE'
         READ(*,*)REFCOR
         WRITE(*,*)'ENTER COMPLEX REFRACTIVE INDEX OF MANTLE'
         READ(*,*)REFMAN
      ENDIF
      IF(INPIND.EQ.1)THEN
         WRITE(*,*)'ENTER COMPLEX DIELEC.CONSTANT OF CORE'
         READ(*,*)EPSCOR
         WRITE(*,*)'ENTER COMPLEX DIELEC.CONSTANT OF MANTLE'
         READ(*,*)EPSMAN
         REFCOR=SQRT(EPSCOR)
         REFMAN=SQRT(EPSMAN)
      ENDIF
      XCOR = 2.*pi*radcor*refmed/wavel
      XMAN = 2.*pi*RADMAN*refmed/wavel
      CALL BHCOAT(XCOR,XMAN,REFCOR,REFMAN,QEXT,QSCA,QBACK)
      WRITE(*,6010)WAVEL,RADCOR,RADMAN,REFCOR,REFMAN,QEXT,QSCA,QBACK
      GOTO 0100
C
 6010 FORMAT(' WAVE=',1PE10.3,' RADCOR=',E10.3,' RADMAN=',E10.3,/,
     &' REFCOR=',2E10.3,' REFMAN=',2E10.3,/,
     &' QEXT=',E12.5,' QSCA=',E12.5,' QBACK=',E12.5)
      END
