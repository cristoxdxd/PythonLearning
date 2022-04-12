import psycopg2

class BaseDatos:

    def __init__(self, dataBase: str)-> None:
        self.cursor = None
        self.baseDatos = dataBase
        self.conexion = None
        self.conectar()
      
    def conectar(self):
        try:
            print('Base: ',self.baseDatos)
            self.conexion = psycopg2.connect(host='localhost', 
                                            database=str(self.baseDatos),
                                            user='postgres', 
                                            password='lkjqZQf6i8cHgY74$&^SUyui', 
                                            port=5432)
            print('Successfully connected to the database')
            self.cursor = self.conexion.cursor()

        except:
            print('Error connecting to the database')

    def addUser(self,name, lastname, age, gender, email, education):
        idU=name
        values = (idU,name, lastname,age, gender, email, education)
        sentenciaInsert = '''INSERT INTO public."Users"(
            id, name, lastname, age, gender, email, education)
	        VALUES (%s, %s, %s, %s, %s, %s, %s);
            '''
        self.cursor.execute(sentenciaInsert,values)
        self.conexion.commit()

    def getUsersData(self):
        self.cursor.execute('SELECT * FROM public."Users";')
        usersData = self.cursor.fetchall();
        #for data in datosUsuarios:
            #print(data)
        return usersData
