program collision1
     implicit none
     character(90)::read_file
     integer*8::nt
     integer*8::countp 
     double precision,allocatable,dimension(:)::xt,yt,zt,rt,vtxt,vtyt,vtzt
     integer,allocatable,dimension(:)::p_id
     double precision,allocatable,dimension(:)::r_after_collision 
     double precision::thta,thtb
     integer :: it
     namelist/main_nml/read_file, nt
        
!        read_file = "../../../../R30_Raw_Data/step.001000.out"
        open(10,file='input.nml')
        read(10,nml=main_nml)
        close(10)
      countp = nt
        allocate(xt(1:countp))
        allocate(yt(1:countp))
        allocate(zt(1:countp))
        allocate(rt(1:countp))
        allocate(p_id(1:countp))
        allocate(vtxt(1:countp))
        allocate(vtyt(1:countp))
        allocate(vtzt(1:countp))
        allocate(r_after_collision(1:countp))


!read_file = "../../../Raw_Data/step011000.out"
open(25,file=read_file)

 write(*,*) read_file

 do it=1,countp
!   print *,"it = ",it
   read(25,*)p_id(it),xt(it),yt(it),zt(it),rt(it),vtxt(it),vtyt(it),vtzt(it),thta,thtb
!    rt(it) =sqrt(rt(it))
!   print *,"pid = ",p_id(it)
 enddo
  write(*,*)"Reading finished"
call collision(xt,yt,zt,rt,nt,r_after_collision)

open(40,file="radii.dat")
do it=1,countp
write(40,'(4(f11.6,1x) )')  ,xt(it), yt(it),zt(it),r_after_collision(it)
end do
close(40)

end program collision1
