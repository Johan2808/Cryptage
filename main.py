from tkinter import * 
from tkinter import messagebox
import base64
import os

#fonction encrypt
def encrypt():
    password = champ2.get()
    if password == "1234":
        #creation d'un nouveau fenetre
        screen1 = Toplevel(screen)
        screen1.title("Encryptage")
        screen1.geometry("400x200")
        screen1.configure(bg="#4B5D67")
        
        #get message
        message = champ.get("1.0" , END).strip()
        encode_message = message.encode("utf-8")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("utf-8")

        #traiter message
        text = Label(screen1 , text="Encrypté" , fg="black" , font=("calibri",13),bg="#4B5D67")
        text.place(x=10 , y=0)

        champ3 = Text(screen1,font = "Robote 20", bg = "white", relief = GROOVE , wrap=WORD , bd=0)
        champ3.place(x=10 , y=40 , width=380 , height = 150)
        champ3.insert(END , encrypt)
    elif password == "":
        messagebox.showerror("encrytage" , "Input Password")
    elif password != "1234":
        messagebox.showerror("encryptage" , "Invalide Passeword")

#fonction decrypt
def decrypt():
    password = champ2.get().strip()
    if password == "1234":
        #creation d'un nouveau fenetre
        screen2 = Toplevel(screen)
        screen2.title("Decryptage")
        screen2.geometry("400x200")
        screen2.configure(bg="#4B5D67")
        
        #get message
        message = champ.get("1.0" , END)
        decode_message = message.encode("utf-8")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("utf-8")

        #traiter message
        text = Label(screen2 , text="Decrypté" , fg="black" , font=("calibri",13),bg="#4B5D67")
        text.place(x=10 , y=0)

        champ3 = Text(screen2,font = "Robote 20", bg = "white", relief = GROOVE , wrap=WORD , bd=0)
        champ3.place(x=10 , y=40 , width=380 , height = 150)
        champ3.insert(END , decrypt)
    elif password == "":
        messagebox.showerror("encrytage" , "Input Password")
    elif password != "1234":
        messagebox.showerror("encryptage" , "Invalide Passeword")


def main_screen():
    global screen
    global code
    global champ
    global champ2

    screen = Tk()
    screen.geometry("375x398")
    screen.minsize(375 , 398)
    screen.maxsize(375 , 398)


    #icon
    screen.iconbitmap(r"E:\programmation\python_Projects\endecryptage-decryptage\projet\Cryptage.ico")

    #titre du page
    screen.title("En/De-Cryptage")

    #couleur de background
    screen.config(background="#4B5D67")

    #fonction reset
    def reset():
        champ.delete("1.0", END) #il s'agit d'un text widget
        champ2.delete(0, END) # il s'agit d'un Entry widget


    #label pour texte du haut
    text1=Label(text="Entrer un texte pour encrypter/decrypter" , fg="black" , font=("calibri",13), bg="#4B5D67")
    text1.place(x=10 , y=10)
    champ = Text(font = "Robote 20", bg = "white", relief = GROOVE , wrap=WORD , bd=0)
    champ.place(x=10 , y=50 , width = 355, height = 100)

    #label pour texte du bas
    text2 = Label(text="Entrer un clé" , fg="black" , font=("calibri",13),bg="#4B5D67")
    text2.place(x=10 , y=170)
    champ2 = Entry(textvariable=StringVar() , width=19 , bd=0 , font=("arial",25) , show="*")
    champ2.place(x=10 , y=200)

    #bouton encrypter
    boutonEnc = Button(text="ENCRYPTER", height="2" , width=23 , bg="#0747a1" , bd = 0, command=encrypt)
    boutonEnc.place(x=10 , y=250)

    #bouton decrypter
    boutonEnc = Button(text="DECRYPTER", height="2" , width=23 , bg="#308B85" , bd = 0,command=decrypt)
    boutonEnc.place(x=200 , y=250)

    #bouton reset
    boutonEnc = Button(text="RESET", height="2" , width=50 , bg="#277441" , bd = 0 , command = reset)
    boutonEnc.place(x=10 , y=300)


    #afficher en boucle
    screen.mainloop()

main_screen()