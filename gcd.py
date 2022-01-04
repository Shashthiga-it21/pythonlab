def add():
 a=int(input("enter a:"))
 b=int(input("enter b:"))
 print("sum is",a+b)
add()

a=12
b=16
for i in range(1,a):
  if ((a%i==0) and (b%i==0)):
      gcd=i
print(gcd)

a=12
b=16
c=20
for i in range(1,a):
  if ((a%i==0) and (b%i==0) and (c%i==0)):
      gcd=i
print(gcd)

a=12
b=16
c=20
for i in range(1,a):
  if ((a%i==0) and (b%i==0) and (c%i==0)):
      lcm=i
print(lcm)
