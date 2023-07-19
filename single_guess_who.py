from random import randint
from tkinter import *
from tkinter import messagebox
import tkinter as tk

persona1 = ['giovanni', 'no','marroni', 'corti','no', 'maschio']
persona2 = ['beatrice','si' ,'Neri', 'Medi','no', 'Femmina']
persona3 = ['vincenzo', 'no', 'Neri', 'corti','no', 'maschio']

persone=[persona1, persona2, persona3]


random=2
punti=0

loop=True

home=tk.Tk()
home.title('Home')
home.geometry('700x700')
home.configure(bg='light grey')
home.grid_propagate(0)

for i in range(0,6):
  home.grid_columnconfigure(i, weight=1, minsize=25)

for j in range(0,6):
  home.grid_rowconfigure(j, weight=1, minsize=25)

point = Label(home, text='PUNTI:',font=('arial', 12))
point.grid(row=3, column=3, sticky='n')
      
def label1(bottone):
  if bottone==1:
    occhiali_lbl = Label(home, text=persone[random][1], font=('Arial', 12), bg='light grey', fg='black')
    occhiali_lbl.grid(row=0, column=2, sticky='w')
  elif bottone==2:
    colore = Label(home, text=persone[random][2], font=('Arial', 12), bg='light grey', fg='black')
    colore.grid(row=1, column=4, sticky='e')
  elif bottone==3:
    lunghezza = Label(home, text=persone[random][3],font=('Arial', 12), bg='light grey', fg='black')
    lunghezza.grid(row=0, column=4, sticky='e')
  elif bottone==4:
    barba = Label(home, text=persone[random][4],font=('Arial', 12), bg='light grey', fg='black')
    barba.grid(row=1, column=2, sticky='w')
  elif bottone==5:
    sesso=Label(home, text=persone[random][5],font=('Arial', 12), bg='light grey', fg='black')
    sesso.grid(row=2, column=2, sticky='w')
  elif bottone==6:
    rdm()

def rdm():
    global loop, random
    if loop:
        random=randint(0,2)
    for widget in home.winfo_children():
      if isinstance(widget, Label)and widget != point and widget != n_point and widget != titolo:
        widget.destroy()
        
rdm()

def enter(event):
  global punti
  persona=barra_persona.get()
  if event.keysym=='Return':
    if persona.lower()==persone[random][0]:
      punti+=1
      n_point.config(text=punti)
      if messagebox.showinfo('Grande', 'Congratulazioni è corretto'):
        rdm()
        barra_persona.delete(0, END)
    else:
      messagebox.showinfo('Peccato', 'E sbagliato ma non demordere puoi ritentare')
      barra_persona.delete(0, END)

def cerca():
  global punti
  persona=barra_persona.get()

  if persona.lower()==persone[random][0]:
    punti+=1
    n_point.config(text=punti)
    if messagebox.showinfo('Grande', 'Congratulazioni è corretto'):
      rdm()
      barra_persona.delete(0, END)
    else:
      messagebox.showinfo('Peccato', 'E sbagliato ma non demordere puoi ritentare')
      barra_persona.delete(0, END)


#Creazione dei bottoni per gli indizi

occhiali_btn=Button(home, text='Occhiali', height=5, width=15, command=lambda: label1(1))
occhiali_btn.grid(row=0, column=1)

lunghezza_btn=Button(home, text='Lunghezza\ncapelli', height=5, width=15, command=lambda: label1(3))
lunghezza_btn.grid(row=0, column=5, sticky='w')

colore_btn=Button(home, text='Colore\nCapelli', height=5, width=15, command=lambda: label1(2))
colore_btn.grid(row=1, column=5, sticky='w')

barba_btn=Button(home, text='Barba\nBaffi', height=5, width=15, command=lambda: label1(4))
barba_btn.grid(row=1, column=1)

sesso_btn=Button(home, text='Sesso', height=5, width=15, command=lambda: label1(5))
sesso_btn.grid(row=2, column=1,)

nuova_btn=Button(home, text='Nuova Persona', height=5, width=15, command=lambda: label1(6))
nuova_btn.grid(row=2, column=5, sticky='w')

barra_persona=Entry(home)
barra_persona.grid(row=4, column=3, sticky='we')
conferma_btn=Button(home, text='Conferma', command=cerca)
conferma_btn.grid(row=4, column=3,sticky='swe')

home.bind("<Return>", enter)

n_point = Label(home, text=punti, font=('arial', 12))
n_point.grid(row=3, column=3, sticky='ne')

titolo = Label(home, text='Guess Who', font=('Arial', 30), fg='black', bg='light grey')
titolo.grid(row=0, column=3, sticky='n')



home.mainloop()
