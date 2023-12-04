from tkinter import Frame
from turtle import color
import customtkinter as ctk
from PIL import Image

janela = ctk.CTk()

class Aplication():

    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()


    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def tela(self):
        janela.geometry('700x400')
        janela.title('Tela de login')
        janela.resizable(False, False)
        janela.iconbitmap('icon.ico')

    def tela_login(self):
        #imagem
        img = ctk.CTkImage(dark_image=Image.open('yasuo_label.png'), size=(380, 309))
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=0,y=110)

        #frame login
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side='right')

        #titulo
        label = ctk.CTkLabel(master=janela, text='Ligas\nLendas APP', font=('Beaufort', 40), text_color='#d4b33a', )
        label.place(x=70, y=15)

        #titulo login
        label = ctk.CTkLabel(master=login_frame, text='Login', font=('Segoe', 40), text_color='gray')
        label.place(x=125, y=40)

        #usuario
        entry_login = ctk.CTkEntry(master=login_frame, placeholder_text='Usuário', width=300, font=('Roboto', 14))
        entry_login.place(x=25, y=105)
        label_login = ctk.CTkLabel(master=login_frame, text='*Campo Usuário obrigatório.', text_color='Green')
        label_login.place(x=25, y=135)

        #senha
        entry_password = ctk.CTkEntry(master=login_frame, placeholder_text='Senha', width=300, font=('Roboto', 14), show="*")
        entry_password.place(x=25, y=175)
        label_password = ctk.CTkLabel(master=login_frame, text='*Campo Senha obrigatório.', text_color='green')
        label_password.place(x=25, y=205)

        #checkbox
        checkbox = ctk.CTkCheckBox(master=login_frame, text='Manter login')
        checkbox.place(x=25, y=235)

        #botao login
        login_button = ctk.CTkButton(master=login_frame, text='Entrar', width=300)
        login_button.place(x=25, y=285)

        #botao cadastro
        register_span = ctk.CTkLabel(master=login_frame, text='Não tem uma conta?', width=145)
        register_span.place(x=20, y=325)
        register_button = ctk.CTkButton(master=login_frame, text='Cadastre-se', width=155, fg_color='green', hover_color='#32612D')
        register_button.place(x=170, y=325)

Aplication()