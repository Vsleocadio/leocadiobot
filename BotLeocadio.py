from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from tkinter import *
from tkinter import messagebox
from subprocess import CREATE_NO_WINDOW

lista_comentarios = []

class Botinstagram:

    def __init__(self):
        self.window = Tk()
        self.window.iconbitmap('itens/iconinsta.ico')
        self.window.eval('tk::PlaceWindow . center')
        self.window.title('LeocadioBOT')
        self.window.minsize(width=350, height=150)
        self.window.maxsize(width=350, height=150)
        self.window.configure(bg='pink')

        self.screen = Entry(self.window,font='arial 10 bold', bg='#cdf7f7', fg='black', width=50)
        self.screen.pack(padx=3, pady=3)

        self.botao1 = Button(self.window, text = '1º ADD LINK SORTEIO', bg='red' ,width=18 ,font='arial 12 bold',command = self.getlink)
        self.botao1.pack()

        self.botao0 = Button(self.window, text='2º ADD COMENT', bg='cyan', width=14, font='arial 12 bold', command=self.coments)
        self.botao0.pack(padx=10, pady=10)

        self.botao2 = Button(self.window, text = '3º INICIAR', bg='gold',width=10 ,font='arial 12 bold',command = self.start)
        self.botao2.pack(padx=5, pady=5)

        messagebox.showinfo(title='BEM VINDO', message='''Desenvolvedor: VICTOR LEOCÁDIO
        instagram: viictorl11
        twitter: VicLeoo ''')

        self.window.mainloop()

    def coments(self):
        self.comentarios = self.screen.get()
        lista_comentarios.append(self.comentarios)
        messagebox.showinfo(title='Comentários', message='{} [ADICIONADO]'.format(self.comentarios))
        self.screen.delete(0, END)

    def getlink(self):
        self.t = self.screen.get()
        self.screen.delete(0, END)
        messagebox.showinfo(title='Sorteio', message='Link do SORTEIO ADICIONADO')

    def start(self):
        messagebox.showinfo(title='BOT', message=''' 
            BOT INICIANDO!
        
            VOCÊ TEM 1 MINUTO PARA LOGAR NA SUA CONTA DO INSTAGRAM
        
            APÓS LOGAR, AGUARDE E DEIXE O BOT AGIR.
        
            SEUS COMENTÁRIOS ADICIONADOS: 
        
            {}
        '''.format(lista_comentarios))
        service = Service('itens/chromedriver')
        service.creationflags = CREATE_NO_WINDOW
        self.navegador = webdriver.Chrome(service=service)
        self.navegador.get('https://www.instagram.com')
        time.sleep(60)
        self.navegador.get('{}'.format(self.t))
        while True:
            for coments in lista_comentarios:
                time.sleep(4)
                textarea = self.navegador.find_element_by_tag_name('textarea')
                time.sleep(1)
                textarea.click()
                time.sleep(1)
                textarea = self.navegador.find_element_by_tag_name('textarea')
                time.sleep(6)
                textarea.clear()
                time.sleep(6)
                textarea.send_keys(coments)
                time.sleep(6)
                self.navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/div[2]/div').click()
            time.sleep(260)
            self.navegador.refresh()
            time.sleep(5)


Botinstagram()