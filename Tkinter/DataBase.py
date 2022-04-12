import psycopg2

# 1. Establecer la conexión con la base de datos
connection = psycopg2.connect(host='localhost', database='Users', user='postgres', password='qZQf6i8cHgY74$&^SU', port=5432)
# 2. Creamos el cursos
cursor = connection.cursor()
# Ejecutamos
cursor.execute('SELECT * FROM public."Users";')
# Visualizar los resultados
for data in cursor.fetchall():
    print(data)

# Insert (sentencia insert) (valores)

sentenciaInsert = '''INSERT INTO public."Users"(
	name, lastname, age, gender)
	VALUES (%s, %s, %s, %s);
    '''
values = ('Cristopher','Herrera',20,'M')
values2 = ('Anderson','Cardenas',22,'M')
cursor.execute(sentenciaInsert,values)
cursor.execute(sentenciaInsert,values2)
connection.commit()
insertedRegisters = cursor.rowcount
print('Inserted ', insertedRegisters)
