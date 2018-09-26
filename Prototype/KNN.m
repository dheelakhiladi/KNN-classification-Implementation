clc
clear all
A = [2,3,4,6,7,5,2,4];
K = 3;
[m,n] = size(A);
count =0
for i = 1:n
  count =0;
  for j = 1:n
    C(i,j)= sqrt((A(1,i)-A(1,j))^2);
  endfor
endfor
C = sort(C);
printf('Sorted distance matrix is ')
C
x = input('Enter The value of K: ');
x = x+1;
sprintf('First row tells us about the original data and Below that is the neighbors')
for i = 1:x
  for j= 1:n
    P(i,j) = C(i,j) +A(1,j);
  endfor
endfor
P