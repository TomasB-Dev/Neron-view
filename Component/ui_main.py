import customtkinter as ctk
from Component.config import *
from Component.validar_user import *
from PIL import Image
def Ui():
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    #configurar de la venta main

    root.title(APP_NAME)
    root.resizable(0,0)
    root.geometry(APP_SCREEN)
    #obtener datos provicional
    #iniciar sesion
    logo_main = ctk.CTkImage(Image.open("Resources/images/Logo.png"),size=(250,250))
    ver_imagen = ctk.CTkLabel(root,text="",image=logo_main)
    ver_imagen.place(x=510,y=50)
    user_login = ctk.CTkEntry(root,
                            width=WIDTH_LOGIN,
                            placeholder_text="Usuario",
                            border_color=NEGRO,
                            border_width=1,
                            corner_radius=CORNER_RADIO_ENTRYS,
                            height=HEIGTH_LOGIN,
                            font=LOGIN_FONT)
    user_login.place(x=450,y=310)

    user_key = ctk.CTkEntry(root,
                            show="*",
                            height=HEIGTH_LOGIN,
                            placeholder_text="Contraseña",
                            width=WIDTH_LOGIN,
                            border_color=NEGRO,
                            border_width=1,
                            corner_radius=CORNER_RADIO_ENTRYS,
                            font=LOGIN_FONT)
    user_key.place(x=450,y=370)
    def get_datos():
        usuario = user_login.get()
        clave = user_key.get()
        validar_user(usuario,clave)

    login_btn = ctk.CTkButton(root,
                            text="LOGIN",
                            height=HEIGTH_LOGIN,
                            border_color=NEGRO,
                            border_width=1,
                            corner_radius=CORNER_RADIO_ENTRYS,
                            fg_color=DORADO_BOTON,
                            text_color=NEGRO,
                            width=WIDTH_LOGIN,
                            font=LOGIN_FONT,
                            hover_color = HOVER_COLOR,
                            command=get_datos
                            )
    login_btn.place(x=450,y=450)

    root.mainloop()