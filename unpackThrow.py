#podemos usar una variable para "tirar" los valores que no nos sirven
# por convención se usa _

array = (5,4,3)

a,_,c = array

print(f'array = {array}')
print(f'a = {a}')
print(f'c = {c}')
print(_)
#el valor en la variable existe, pero se considera basura

