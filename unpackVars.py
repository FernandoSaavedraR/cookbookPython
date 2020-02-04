#Desestructurar iterables
#Debes tener el mismo numero de variables que
#elementos en tu iterable
t = (5,4)
x,y = t

print(t)
print(f'[{x},{y}]')

array = ['Fernando','Saavedra Rodríguez',1,True,(90,60,90)]

nombre,apellidos,edad,sexo,medidas = array

print(array)

print(f'nombre: {nombre}')
print(f'apellidos: {apellidos}')
print(f'edad: {edad} {"año" if edad ==1 else "años"}')
print(f'sexo: {"masculino" if sexo else "femenino"}')
print(f'medidas: {medidas}')


