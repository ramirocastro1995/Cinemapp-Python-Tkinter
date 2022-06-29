from tkinter import *
import imdb
import tkinter as tk

root = Tk()
root.title('Buscador de peliculas')
root.geometry("700x675")

#limpiar
def clear():
    my_entry.delete(0, END)
    my_text.delete(0.0, END)


def search():
    ia = imdb.IMDb()
    data = ia.search_movie(my_entry.get())
    #clear
    clear()
    #resultado de wikipedia
    my_text.insert(0.0,data)
    




my_label_frame = LabelFrame(root, text = "search movie")
my_label_frame.pack(pady=20)

#entrybox
my_entry = Entry(my_label_frame, font=("Helvetica", 18), width = 47)
my_entry.pack(pady=20,padx=20)

#textbox frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#scroll vertical
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#scroll horizontal
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)




#textbox
my_text = Text(my_frame,yscrollcommand=text_scroll.set, wrap="word", xscrollcommand=hor_scroll.set)
my_text.pack()

#scrollbars

text_scroll.config(command=my_text.yview)
text_scroll.config(command=my_text.xview)

#botones marco
button_frame = Frame(root)
button_frame.pack(pady=10)

search_button = Button(button_frame, text="lookup",font=("Helvetica",32),fg="#3a3a3a", command = search)
search_button.grid(row=0, column=0,padx=20)

clear_button = Button(button_frame, text="clear",font=("Helvetica",32),fg="#3a3a3a", command = clear)
clear_button.grid(row=0, column=1)


root.mainloop()