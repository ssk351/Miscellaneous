subroutine collision(xt,yt,zt,rt,nt,r_after_collision)
!     use ClosestPair
     implicit none
     character(90)::read_file
     integer*8::nt
     double precision,dimension(nt)::x_dummy,y_dummy,z_dummy,rt
     double precision,dimension(2)::xp,yp,zp
     double precision,dimension(nt)::r_after_collision , xt  , yt , zt 
     double precision::r1, r2, min, dist
     integer::no_of_collision, m, n, i, j, it, si, sj, old_collision
     logical :: log_coll=.false.
     integer,dimension(2) :: pos
no_of_collision=0;
!load('step011000.out')
r_after_collision = rt
x_dummy = xt
y_dummy =yt
z_dummy =zt
r1=0.0; r2=0.0;
no_of_collision =0;
!moving over all particles
no_of_collision=0;old_collision=1
do while (no_of_collision.ne.old_collision)

min=100;

call closest(x_dummy,y_dummy,z_dummy,xp,yp,zp,min,nt,pos)

write(*,'(A,A,F20.14,2I8)') "coordinates of nearest pair = ","min dist =", min,pos(1),pos(2)
old_collision = no_of_collision


!-----minimum finding loop ends
!-------collision
do i=pos(1),pos(1)
    do j=pos(2),pos(2)
 print *, "Check 1"
           if((min < (r_after_collision(i) + r_after_collision(j))).and.(r_after_collision(i).ne.0.0).and.r_after_collision(j).ne.0) then
              print *,"collision number ", no_of_collision+1
               no_of_collision = no_of_collision +1
              r1 = r_after_collision(i)
              r2 = r_after_collision(j)       
              log_coll = .true. 
              if(r_after_collision(i).gt.r_after_collision(j)) then
              print *,"Check1 collision old_collision",no_of_collision,old_collision
              x_dummy(j)=maxval(x_dummy(:))*(no_of_collision + 1)
              y_dummy(j)=maxval(y_dummy(:))*(no_of_collision + 1)
              z_dummy(j)=maxval(z_dummy(:))*(no_of_collision + 1)
              r_after_collision(i) = r_after_collision(i)+r_after_collision(j)
              r_after_collision(j) =0.0
              
              else
              print *,"Check2 collision old_collision",no_of_collision,old_collision
              x_dummy(i)=maxval(x_dummy(:))*(no_of_collision + 1)
              y_dummy(i)=maxval(y_dummy(:))*(no_of_collision + 1)
              z_dummy(i)=maxval(z_dummy(:))*(no_of_collision + 1)
              r_after_collision(j) = r_after_collision(i)+r_after_collision(j)
              r_after_collision(i) =0.0
              end if 
           end if
    end do
end do


!-------collision
print *,m, " th bigger loop of ",nt
    write(*,'(A,I8,1x,F20.14,2x,A,I8,A,I8,A,2F20.14)') "i, minimum = ",i, min ,"bigger loop ",m, " of ",nt,"r1, r2 = ",r1,r2

!deallocate(points)
!deallocate(p)


end do  ! end of do while
end subroutine collision
