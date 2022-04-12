import tkinter as tk
from tkinter import GROOVE, SUNKEN, Frame, ttk, NO, messagebox
from turtle import color
from matplotlib.pyplot import text

#from sympy import root
from DataBase2 import BaseDatos
from utilidades import center

colorGreen = '#b4ffff'
colorDarkgreen = '#003d33'
colorBlue = '#042E6C'
colorYellow = '#F1E790'
colorBlack = '#000000'
colorWhite = '#FFFFFF'
titlesFont = ('Courie',14,'bold')
generalFont = ('Courie',11,'normal')

class Ventana:
    def __init__(self) -> None:
        self.dataConnection = BaseDatos('Users')
        self.root = tk.Tk()
        self.root.title('Users')
        self.root.resizable(True,True)
        self.root.geometry('600x500')
        center(self.root)
        self.root.configure(bg=colorGreen)
        self.frameRegistro = None
        self.frameUsuarios = None
        self.dibujar()
 
    def guardarInformacion(self, name: str, lastname: str, age: int):
        print(f'Información {name} {lastname} {age}')

    def saludar(self,texto):
        print('Dices', texto)

    def showRegisterFrame(self):
        #print('Mostrando frame registro')
        self.hiddeAllFrames()
        self.frameRegistro.place(x=0,y=100)

    def mostrarFrameUsuarios(self):
        #print('Mostrando frame usuarios')
        self.hiddeAllFrames()
        self.frameUsuarios.place(x=0,y=100)

    def hiddeAllFrames(self):
        #print('Ocultando todos los frames')
        self.frameRegistro.place_forget()
        self.frameUsuarios.place_forget()

    def dibujar(self):

# ---------------------  Encabezado -----------------------------#
        titulo = tk.Label(self.root,text='Users Manage System', bg=colorGreen, font=titlesFont)    
        titulo.place(x=170,y=15)

        btnRegistro = tk.Button(self.root, text='User Register', font=generalFont, 
                    command=self.showRegisterFrame, width=15, height=1, bd=2,
                    bg=colorDarkgreen, fg=colorWhite,relief=SUNKEN)
        btnRegistro.place(x=40,y=55)

        btnUsuarios= tk.Button(self.root, text='Users', font=generalFont, 
                    command=self.mostrarFrameUsuarios, width=15, height=1, bd=2,
                    bg=colorDarkgreen, fg=colorWhite,relief=SUNKEN)
        btnUsuarios.place(x=240,y=55)

        btnSalir= tk.Button(self.root, text='Exit', font=generalFont, 
                    command=self.root.destroy, width=15, height=1, bd=2,
                    bg=colorDarkgreen, fg=colorWhite,relief=SUNKEN)
        btnSalir.place(x=440,y=55)
        

# ---------------------  Frame Usuario -----------------------------#    
        self.frameUsuarios = Frame(self.root, width=600, height=400, bg=colorGreen, relief='sunken')
        self.frameUsuarios.place(x=0,y=100)

        texto1 = tk.Label(self.frameUsuarios, text='Datos de los usuarios', bg=colorGreen,
                font=generalFont, fg=colorBlue)
        texto1.place(x=20, y=20)

        # Tabla
        columnas = ('Name','Lastname','Age','Gender','Email','Education')
        tblUsr = ttk.Treeview(self.frameUsuarios, height=15, columns=columnas, show='headings')
        tblUsr.place(x=15, y=60)

        for heading in columnas:
            tblUsr.heading(heading, text=heading)
            tblUsr.column(heading, minwidth=95, width=95, stretch=NO)

        def llenarDatos():
            data = self.dataConnection.getUsersData()
            for fila in data:
                tblUsr.insert('','end', values=fila)

        btnLlenarDatos= tk.Button(self.frameUsuarios, text='Cargar Usuario', font=('Courie',10,'normal'), 
                    command=llenarDatos, height=1, bd=2,bg=colorDarkgreen, fg=colorWhite,relief=SUNKEN)
        btnLlenarDatos.place(x=300,y=20)


# ---------------------  Frame Registro -----------------------------#

        self.frameRegistro = Frame(self.root, width=600, height=400, bg=colorGreen, relief='sunken')
        self.frameRegistro.place(x=0,y=100)

        texto1 = tk.Label(self.frameRegistro, text='Enter the data', bg=colorGreen,
                font=generalFont, fg=colorBlue)
        texto1.place(x=20, y=60)

        lblNombre = tk.Label(self.frameRegistro, text='Name:', bg=colorGreen, font=generalFont)
        lblNombre.place(x=20, y=110)

        lblApellido = tk.Label(self.frameRegistro, text='Lastname:', bg=colorGreen, font=generalFont)
        lblApellido.place(x=20, y=150)

        lblEdad = tk.Label(self.frameRegistro, text='Age:', bg=colorGreen, font=generalFont)
        lblEdad.place(x=20, y=190)
        
        lblSexo = tk.Label(self.frameRegistro, text='Gender:', bg=colorGreen, font=generalFont)
        lblSexo.place(x=20, y=230)

        lblCorreo = tk.Label(self.frameRegistro, text='Email:', bg=colorGreen, font=generalFont)
        lblCorreo.place(x=20, y=270)

        lblFormacion = tk.Label(self.frameRegistro, text='Education:', bg=colorGreen, font=generalFont)
        lblFormacion.place(x=20, y=310)

        # Input
        inputName = tk.Entry(self.frameRegistro, width=20)
        inputName.place(x=100,y=110)

        inputLastname = tk.Entry(self.frameRegistro)
        inputLastname.place(x=100,y=150)

        inputAge = tk.Entry(self.frameRegistro)
        inputAge.place(x=100,y=190)

        inputEmail = tk.Entry(self.frameRegistro)
        inputEmail.place(x=100,y=270)

        # Radio Button
        radioGender = tk.StringVar()
        def selectGender():
            print(f'Gender selection: {radioGender.get()}')

        radioM = tk.Radiobutton(self.frameRegistro, text='Male', value='M', bg=colorGreen, 
                                variable=radioGender, command=selectGender, tristatevalue=0)
        radioM.place(x=100, y=230)

        radioF = tk.Radiobutton(self.frameRegistro, text='Female', value='F', bg=colorGreen, 
                                variable=radioGender, command=selectGender, tristatevalue=0)
        radioF.place(x=200, y=230)

        # Combobox Formación Academica
        listaFormacionAcademica = ['Elementary School','Middle School','High School','University']
        cmbEducation = tk.ttk.Combobox(self.frameRegistro, values=listaFormacionAcademica, width=21)
        cmbEducation.place(x=100, y=310)

        def saveInfo2():                        
            try:
                # Validar

                # Guardar
                self.dataConnection.addUser(inputName.get(), inputLastname.get(), 
                                                    inputAge.get(), radioGender.get(),inputEmail.get(),
                                                    cmbEducation.get())
            except:
                messagebox.showwarning(message="Can't register the user", title=f'Error Registration') 

        # width de los botones es un numero
        btnGuardar = tk.Button(self.frameRegistro, text='Save\nInformation', font=generalFont, 
                    command=saveInfo2, width=15, height=2, bd=2,
                    bg=colorBlack, fg=colorWhite,
                    relief=SUNKEN)
        btnGuardar.place(x=400,y=200)
             

# Main loop
        self.root.mainloop()

ventana = Ventana()