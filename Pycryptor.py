from tkinter.filedialog import asksaveasfile
from cryptography.fernet import Fernet
from tkinter import *


root = Tk()
root.title("Pycryptor")


def GenerateKey():
    global key
    key = Fernet.generate_key()
    Key.delete(0, END)
    Key.insert(0, key)

def Encrypt():
    KEY = Key.get()
    text = t.get()
    encrypted = Fernet(KEY).encrypt(text.encode('ascii'))
    t.delete(0, END)
    t.insert(0, encrypted)
def Decrypt():
    KEY = Key.get()
    text = t.get()
    decrypted = Fernet(KEY).decrypt(text.encode('ascii'))
    t.delete(0, END)
    t.insert(0, decrypted)

def SaveKey():
    KEY = Key.get()
    with open("PycryptorKey.key", "w") as f:
        f.write(KEY)
        f.close()
    

Key = Entry(root, width=100)
Key.insert(0, "Key")

t = Entry(root, width=200)
t.insert(0, "Enter a text")

GK = Button(root, bg="green", text="Generate Key", command=GenerateKey)
SAVEKEY = Button(root, text="Save Key", bg="purple", command=SaveKey)
ENCRYPT = Button(root, bg="blue", text="Encrypt", command=Encrypt)
DECRYPT = Button(root, bg="blue", text="Decrypt", command=Decrypt)

Key.grid(row=0)
GK.grid(row=1)
SAVEKEY.grid(row=2)
t.grid(row=3)
ENCRYPT.grid(row=4)
DECRYPT.grid(row=5)

info = Label(root, text="Pycryptor is used to encrypt any content with a given key. The content can't be decrypted without the key.", fg="purple").grid(row=6)
credit = Label(root, text="Made by Doges 2022", fg="purple").grid(row=7)
root.mainloop()






