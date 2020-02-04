lista = ['Fernando',21,'55-46757886','55-38149959']

nombre,edad,*telefono = lista
print(lista)
print(telefono)

*tiempo_trenes,tiempo_actual = [10,12,14,15,24,11]

promedio = sum(tiempo_trenes)/len(tiempo_trenes)

def avg_comparison(promedio,actual):
    mensaje = ''
    if actual > promedio:
        mensaje =  "Más de la media"
    elif actual == promedio:
        mensaje =  "Igual que la media"
    else:
        mensaje = "Menos que la media"
    return mensaje

print(f'tiempo de trenes historicos: {tiempo_trenes}')
print(f'ultimo tiempo: {tiempo_actual}')
print(f'promedio historico:{int(promedio)}')
print(avg_comparison(promedio,tiempo_actual))
