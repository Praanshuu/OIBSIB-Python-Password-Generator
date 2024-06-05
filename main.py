from tkinter import *
import random
import string
from tkinter import messagebox

characterSetList = ""
password = []


def charlist():
    global characterSetList
    characterSetList = ""
    if x.get() == 1:
        characterSetList += string.digits
    if y.get() == 1:
        characterSetList += string.ascii_letters
    if z.get() == 1:
        characterSetList += string.punctuation


def password_generate():
    global password
    password = []
    password_length = int(length_value.get())
    for i in range(password_length):
        randomchar = random.choice(characterSetList)
        password.append(randomchar)
    password = "".join(password)
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)


def copy_to_clipboard():
    text = pw_entry.get()
    window.clipboard_append(text)
    messagebox.showinfo("Information", "Password copied to clipboard")


window = Tk()
window.title("Random Password Generator")
window.geometry("600x500")
window.config(bg='#52fa90')

frame = Frame(window,
              padx=20,
              pady=20,
              bg='#fcfafa'
              )
frame.pack(expand=True)

length = Label(frame,
               text="Enter the password length: ",
               bg='#fcfafa',
               font=("Helvetica", 12, 'bold'),
               padx=10,
               pady=10
               )
length.grid(row=1, column=1, sticky=W, padx=5, pady=5)
length_value = Entry(frame, font=("Helvetica", 12))
length_value.grid(row=1, column=2, sticky=E, padx=5, pady=5)

charset = Label(frame,
                text="Choose character set for password:",
                bg='#fcfafa',
                font=("Helvetica", 12, 'bold'),
                padx=10,
                pady=10
                )
charset.grid(row=2, column=1, columnspan=2, sticky=W, padx=5, pady=5)

x = IntVar()
number_charset = Checkbutton(frame,
                             text="Numbers",
                             bg="#fcfafa",
                             font=('Helvetica', 12),
                             padx=10,
                             pady=5,
                             variable=x,
                             onvalue=1,
                             offvalue=0,
                             command=charlist
                             )
number_charset.grid(row=3, column=1, sticky=W, padx=5, pady=5)

y = IntVar()
letter_charset = Checkbutton(frame,
                             text="Letters",
                             bg="#fcfafa",
                             font=('Helvetica', 12),
                             padx=10,
                             pady=5,
                             variable=y,
                             onvalue=1,
                             offvalue=0,
                             command=charlist
                             )
letter_charset.grid(row=4, column=1, sticky=W, padx=5, pady=5)

z = IntVar()
symbols_charset = Checkbutton(frame,
                              text="Special Characters",
                              bg="#fcfafa",
                              font=('Helvetica', 12),
                              padx=10,
                              pady=5,
                              variable=z,
                              onvalue=1,
                              offvalue=0,
                              command=charlist
                              )
symbols_charset.grid(row=5, column=1, sticky=W, padx=5, pady=5)

button = Button(frame,
                text="Generate",
                font=("Helvetica", 12, 'bold'),
                bg='#0072C6',
                fg='white',
                command=password_generate
                )
button.grid(row=6, column=1, columnspan=2, pady=10)

pw_label = Label(frame,
                 text="Generated password: ",
                 bg='#fcfafa',
                 font=('Helvetica', 12, 'bold'),
                 padx=10,
                 pady=10
                 )
pw_label.grid(row=7, column=1, sticky=W, padx=5, pady=5)

pw_entry = Entry(frame, font=("Helvetica", 12), width=25, justify='center')
pw_entry.grid(row=7, column=2, sticky=E, padx=5, pady=5)

copy_btn = Button(frame, text="Copy", font=("Helvetica", 12, 'bold'),
                  bg='#0072C6', fg='white', command=copy_to_clipboard)

copy_btn.grid(row=8, column=1, columnspan=2, pady=10)

window.mainloop()
