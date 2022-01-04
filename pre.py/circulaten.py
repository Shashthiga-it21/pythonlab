a=[55,66,77,88,99,33,54,65,65,64]
print(a)
for i in range(10):
 temp=a[0]
 for j in range( len(a)-1):
    a[j]=a[j+1]
 a[len(a)-1]=temp
 print(a)

print("###")

a=[55,66,77,88,99,33,54,65,65,64]
print(a)
for i in range(10):
 temp=a[0]
 for j in range(9):
    a[j]=a[j+1]
 a[9]=temp
 print(a)