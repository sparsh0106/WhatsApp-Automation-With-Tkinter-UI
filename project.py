from tkinter import *
import pywhatkit


main_root = Tk()

main_root.geometry("1600x900")

def send_message():
    phone_num = str(entry_1.get())
    msg = str(entry_2.get())
    hour = int(entry_3.get())
    minute = int(entry_4.get())
    pywhatkit.sendwhatmsg(phone_num, msg, hour, minute)

label_1 = Label(main_root, text = "WhatsApp Automation", font = ('Bahnschrift 30 underline bold'))
label_1.pack()

label_2 = Label(main_root, text = "Enter mobile number with country code : ", font = ('Bahnschrift 20'))
label_2.pack()

entry_1 = Entry(main_root, bg = 'yellow', font = 'Bahnschrift')
entry_1.place(x = 1066, y = 66)

label_3 = Label(main_root, text = "Enter the message : ", font = ('Bahnschrift 20'))
label_3.pack()

entry_2 = Entry(main_root, bg = 'yellow', font = 'Bahnschrift')
entry_2.place(x = 940, y = 105)

label_4 = Label(main_root, text = "Enter hour (24 hour format) : ", font = ('Bahnschrift 20'))
label_4.pack()

entry_3 = Entry(main_root, bg = 'yellow', font = 'Bahnschrift')
entry_3.place(x = 997, y = 144)

label_5 = Label(main_root, text = "Enter minutes : ", font = ('Bahnschrift 20'))
label_5.pack()

entry_4 = Entry(main_root, bg = 'yellow', font = 'Bahnschrift')
entry_4.place(x = 913, y = 184)

button_1 = Button(main_root, text = "SEND", font = "BaHnScHrIfT 20", bg = 'red', fg = 'white', activebackground = 'yellow', bd = 3, command = send_message)
button_1.pack()

label_5 = Label(main_root, text = "Note : This program will only work if you have WhatsApp Web signed in on your web browser", font = ('Candara 20 italic'))
label_5.place(x = 300, y = 500)


main_root.mainloop()
