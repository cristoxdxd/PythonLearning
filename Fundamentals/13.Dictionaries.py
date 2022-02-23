dictionary1 = {
    'i1': 1,
    'i2': [True, 'Amnesia',6]
}

print(type(dictionary1))
print(dictionary1)

# Acceder a los datos de un diccionario
print(dictionary1['i2'])

materias = {
    'audiotoriaInformatica': 8,
    'webAvanzada2': 10
}
edad = 22
llaveVariable = 'cedula'
persona = {
    'nombre': 'Fernando',
    'apellido': 'Cárdenas',
    'edad': edad,
    'casado': False,
    21: True,    
    llaveVariable: '1726744814',
    'materias': materias
}

print(type(persona['nombre']))
print(persona['edad'])
print(persona['casado'])
print(persona[21])
print(persona[llaveVariable])
print(persona['materias'])

print('Methods')
print(persona.get('edad'))
print(persona.update({'edad':23}))
persona['universidad'] = 'EPN'
print(persona)
persona.pop(21)
print(persona)

print(persona.values())
print(persona.keys())
print(persona.items())

def obtenerLlave(valorBuscar):
    for llave, valor in persona.items():
        if valorBuscar == valor:
            return llave

print('Llave encontrada:',obtenerLlave('1726744814'))
persona.pop(obtenerLlave('1726744814'))
print(persona)

persona.popitem()
print(persona)

print(persona.get('mascota', 'No existe este valor'))

copiaPersona = persona.copy()
print(copiaPersona)

print(len(copiaPersona))

copiaPersona.clear()
print(copiaPersona)

listaPrueba = [0,1,2,3,4]
diccionarioPrueba = {}
for i in listaPrueba:
    diccionarioPrueba[i] = i

print(diccionarioPrueba)

diccionarioPrueba2 = {}
listaLlave = ['n0','n1','n2','n3','n4']
listaPrueba2 = [0,1,2,3,4]
for i in range(len(listaLlave)):
    diccionarioPrueba2[listaLlave[i]] = listaPrueba2[i]
print(diccionarioPrueba2)

diccionarioPrueba3 = dict(zip(listaLlave,listaPrueba2))
print(diccionarioPrueba3)