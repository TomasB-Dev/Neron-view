from Component.config import *
import customtkinter as ctk
import cv2
import threading
from tkinter import Label, Frame
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="Component/.env")
cam1 = None
cam2 = None
cam3 = None
stop_threads = False
def show_camera(cam, cam_lbl):
    global stop_threads
    while not stop_threads:
        ret, frame = cam.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
    global cam1, cam2, cam3, stop_threads, cam_lbl1, cam_lbl2, cam_lbl3, start_btn

    camara1 = os.getenv("CAM1")
    camara2 = os.getenv("CAM2")


    if cam1 is None and cam2 is None and cam3 is None:
        # Inicializar cámaras
        cam1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam2 = cv2.VideoCapture(camara1)
        cam3 = cv2.VideoCapture(camara2)

        # Verificar cada cámara
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

        # Actualizar texto del botón
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

        # Resetear variables
        start_btn.configure(text="Comenzar")
        cam1 = None
        cam2 = None
        cam3 = None

def loged_user(usuario, root):

    global cam_lbl1, start_btn, cam_lbl2, cam_lbl3
    root.destroy()
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.title(APP_NAME + f" ({usuario})")
    root.resizable(0, 0)
    root.geometry(APP_SCREEN)

    config_btn = ctk.CTkButton(
        root, text="Configuracion", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2
    )
    config_btn.place(x=20, y=20)

    start_btn = ctk.CTkButton(
        root, text="Comenzar", font=LOGIN_FONT,
        height=HEIGHT_BOTONES, corner_radius=10, border_width=2,
        command=start_capture
    )
    start_btn.place(x=200, y=20)
    #Espacios para las camaras
    cam_lbl1 = ctk.CTkLabel(root, text="")
    cam_lbl1.place(x=20, y=100)

    cam_lbl2 = ctk.CTkLabel(root, text="")
    cam_lbl2.place(x=400, y=100)

    cam_lbl3 = ctk.CTkLabel(root,text="")
    cam_lbl3.place(x=780,y=100)



    root.mainloop()