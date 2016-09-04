program TestClosestPair
  use ClosestPair
  implicit none
 
  integer, parameter :: n = 10000
 
  integer :: i
  real :: x, y
  type(point), dimension(n) :: points
 
  type(point), dimension(2) :: p
  real :: dp, dr
 
  ! init the random generator here if needed
 
  do i = 1, n
     call random_number(x)
     call random_number(y)
     points(i) = point(x*20.0-10.0, y*20.0-10.0)
  end do
 
  call closest_pair_simple(points, p, dp)
  print *, "sim ", p(1)%x,p(2)%x,p(1)%y,p(2)%y
  call closest_pair(points, p, dr)
  print *, "rec ", p(1)%x,p(2)%x,p(1)%y,p(2)%y
end program TestClosestPair
