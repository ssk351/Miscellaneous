subroutine closest(x,y,z,xp,yp,zp,dist,n,pos)
! Using divide and conquer
  use ClosestPair
  implicit none

  integer :: n

  integer :: i,j
  double precision, dimension(n) :: x, y, z
  double precision, dimension(2) :: xp, yp, zp
  integer, dimension(2) :: pos 
  type(point), dimension(n) :: points

  type(point), dimension(2) :: p
  double precision :: dp, dr, dist

  ! init the random generator here if needed

  do i = 1, n
!     print *,"x(",i,") = ",x(i)
     points(i) = point(x(i), y(i), z(i))
  end do

!  call closest_pair_simple(points, p, dp, pos)
!  print *, "sim ", p(1)%x,p(2)%x,p(1)%y,p(2)%y,p(1)%z,p(2)%z
  call closest_pair(points, p, dr,pos ,n)
  print *,"From subroutine : "
  print *, "rec ", p(1)%x,p(2)%x,p(1)%y,p(2)%y,p(1)%z,p(2)%z

  xp(1) = p(1)%x; xp(2) = p(2)%x; yp(1) = p(1)%y; yp(2) = p(2)%y; zp(1) = p(1)%z; zp(2) = p(2)%z
  dist = dr
!  dist = dp

!    do i=1,n
!      do j=i+1,n
!          if ( (x(i).eq.xp(1)).and.(x(j).eq.xp(2)).and.(y(i).eq.yp(1)).and.(y(j).eq.yp(2)).and.(z(i).eq.zp(1)).and.(z(j).eq.zp(2)) )then
!              pos = (/i,j/)
!          end if
!      end do
!    end do
end subroutine closest
