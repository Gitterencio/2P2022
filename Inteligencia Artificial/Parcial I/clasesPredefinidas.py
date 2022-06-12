i=1
print(type(i))
print('i es :{0}'.format(i))

#alias
j=i
i=4

print('i=4,j es :{0} por inmutabilidad de i'.format(j))

print('\nint(2.7)  {0}'.format(int(2.7)))
print('\nint("234")  {0}'.format(int("234")))
print('\nint(True)  {0}'.format(int(True)))


print('\nbool(0)  {0}'.format(bool(0)))
print('\nbool(1)  {0}'.format(bool(1)))
print('\nbool(h)  {0}'.format(bool('h')))
print('\nbool('')  {0} \n'.format(bool('')))

l =[1,2,3]
t=(1,2,3)
l[0] = 4

print(l)

#t[0]=4 error , tupla es inmmutable

print(t)

l =[1,2,3]
t=(1,2,l)

print(t)

s="hola"
print(s)
s="""multiples 
lineas """

print(s)