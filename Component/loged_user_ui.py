from Component.config import *
import customtkinter as ctk
import cv2
import threading
from tkinter import Label, Frame
from PIL import Image, ImageTk
import os
from Component.ui_config import *
from Component.detectar_personas import *
from dotenv import load_dotenv
load_dotenv(dotenv_path="Component/.env")
cam1 = None
cam2 = None
cam3 = None
cam4 = None
cam5 = None
cam6 = None
stop_threads = False
def show_camera(cam, cam_lbl):
    Config_Ui()
    global stop_threads
    while not stop_threads:
        ret, frame = cam.read()
        if ret:
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            
            frame = detect_and_draw_people(frame)
            
            
            frame_resized = cv2.resize(frame, (250, 250))
            if frame_resized is not None and frame_resized.size > 0:
                im = Image.fromarray(frame_resized)
                img = ImageTk.PhotoImage(im)
                cam_lbl.configure(image=img)
                cam_lbl.image = img
        else:
            cam_lbl.configure(text="DETENIDO")
        
        cv2.waitKey(10)

def start_capture():
    global cam1, cam2, cam3,cam4,cam5,cam6, stop_threads, cam_lbl1, cam_lbl2, cam_lbl3,cam_lbl4,cam_lbl5,cam_lbl6, start_btn
    
    camara0 = os.getenv("CAM0")
    camara1 = os.getenv("CAM1")
    camara2 = os.getenv("CAM2")
    camara3 = os.getenv("CAM3")
    camara4 = os.getenv("CAM4")
    camara5 = os.getenv("CAM5")


    if cam1 is None and cam2 is None and cam3 is None:
        # inicializar camaras
        cam1 = cv2.VideoCapture(camara0)
        cam2 = cv2.VideoCapture(camara1)
        cam3 = cv2.VideoCapture(camara2)
        cam4 = cv2.VideoCapture(camara3)
        cam5 = cv2.VideoCapture(camara4)
        cam6 = cv2.VideoCapture(camara5)

        # verificar cada camara
        if not cam1.isOpened():
            cam_lbl1.configure(text="Error al abrir la camara 1")
            cam1 = None
        else:
            threading.Thread(target=show_camera, args=(cam1, cam_lbl1), daemon=True).start()

        if not cam2.isOpened():
            cam_lbl2.configure(text="Error al abrir la camara 2")
            cam2 = None
        else:
            threading.Thread(target=show_camera, args=(cam2, cam_lbl2), daemon=True).start()

        if not cam3.isOpened():
            cam_lbl3.configure(text="Error al abrir la camara 3")
            cam3 = None
        else:
            threading.Thread(target=show_camera, args=(cam3, cam_lbl3), daemon=True).start()
        
        if not cam4.isOpened():
            cam_lbl4.configure(text="Error al abrir la camara 4")
            cam4 = None
        else:
            threading.Thread(target=show_camera, args=(cam4, cam_lbl4), daemon=True).start()
        if not cam5.isOpened():
            cam_lbl5.configure(text="Error al abrir la camara 5")
            cam5 = None
        else:
            threading.Thread(target=show_camera, args=(cam6, cam_lbl6), daemon=True).start()
        if not cam6.isOpened():
            cam_lbl6.configure(text="Error al abrir la camara 6")
            cam6 = None
        else:
            threading.Thread(target=show_camera, args=(cam6, cam_lbl6), daemon=True).start()

        # act boton
        start_btn.configure(text="Detener")

    else:
        stop_threads = True

        if cam1:
            cam1.release()
            cam_lbl1.configure(image=None, text="DETENIDO")
        if cam2:
            cam2.release()
            cam_lbl2.configure(image=None, text="DETENIDO")
        if cam3:
            cam3.release()
            cam_lbl3.configure(image=None, text="DETENIDO")
        if cam4:
            cam4.release()
            cam_lbl4.configure(image=None, text="DETENIDO")
        if cam5:
            cam5.release()
            cam_lbl5.configure(image=None, text="DETENIDO")
        if cam6:
            cam6.release()
            cam_lbl6.configure(image=None, text="DETENIDO")

        # resetear variables
        start_btn.configure(text="Comenzar")
        cam1 = None
        cam2 = None
        cam3 = None
        cam4 = None
        cam5 = None
        cam6 = None
        

def loged_user(usuario, root):

    global cam_lbl1, start_btn, cam_lbl2, cam_lbl3,cam_lbl4,cam_lbl5,cam_lbl6
    root.destroy()
    ctk.set_appearance_mode("dark") 
    root = ctk.CTk()
    root.after(201, lambda :root.iconbitmap(RUTA_ICONO))
    root.title(APP_NAME + f" ({usuario})")
    root.resizable(0, 0)
    root.geometry(APP_SCREEN)

    config_btn = ctk.CTkButton(
        root, text="Configuracion", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2,
        hover_color = HOVER_COLOR,
        command= Config_Ui
    )
    config_btn.place(x=20, y=20)

    start_btn = ctk.CTkButton(
        root, text="Comenzar", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2,
        hover_color = HOVER_COLOR,
        command=start_capture
    )
    start_btn.place(x=200, y=20)
    #espacios para las camaras
    cam_lbl1 = ctk.CTkLabel(root, text="")
    cam_lbl1.place(x=X_CAMARA1, y=100)

    cam_lbl2 = ctk.CTkLabel(root, text="")
    cam_lbl2.place(x=X_CAMARA2, y=100)

    cam_lbl3 = ctk.CTkLabel(root,text="")
    cam_lbl3.place(x=X_CAMARA3,y=100)

    cam_lbl4 = ctk.CTkLabel(root,text="")
    cam_lbl4.place(x=X_CAMARA1,y=500)

    cam_lbl5 = ctk.CTkLabel(root,text="")
    cam_lbl5.place(x=X_CAMARA2,y=500)

    cam_lbl6 = ctk.CTkLabel(root,text="")
    cam_lbl6.place(x=X_CAMARA3,y=500)




    root.mainloop()