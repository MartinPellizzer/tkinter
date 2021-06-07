from tkinter import *

root = Tk()

# -----------------------------------------------------------
# fornitore
# -----------------------------------------------------------
frame1 = LabelFrame(root, text="Fornitore")
frame1.grid(row=0, column=0)

name_label = Label(frame1, text="Nome: ")
name_label.pack(anchor=W)
name_entry = Entry(frame1)
name_entry.pack(anchor=W)

address_label = Label(frame1, text="Indirizzo: ")
address_label.pack(anchor=W)
address_entry = Entry(frame1)
address_entry.pack(anchor=W)

city_label = Label(frame1, text="Citta: ")
city_label.pack(anchor=W)
city_entry = Entry(frame1)
city_entry.pack(anchor=W)

state_label = Label(frame1, text="Provincia: ")
state_label.pack(anchor=W)
state_entry = Entry(frame1)
state_entry.pack(anchor=W)

zip_label = Label(frame1, text="Cap: ")
zip_label.pack(anchor=W)
zip_entry = Entry(frame1)
zip_entry.pack(anchor=W)

email_label = Label(frame1, text="Email: ")
email_label.pack(anchor=W)
email_entry = Entry(frame1)
email_entry.pack(anchor=W)

phone_label = Label(frame1, text="Tel: ")
phone_label.pack(anchor=W)
phone_entry = Entry(frame1)
phone_entry.pack(anchor=W)

vat_label = Label(frame1, text="IVA: ")
vat_label.pack(anchor=W)
vat_entry = Entry(frame1)
vat_entry.pack(anchor=W)

# -----------------------------------------------------------
# cliente
# -----------------------------------------------------------
frame2 = LabelFrame(root, text="Cliente")
frame2.grid(row=0, column=1)

client_name_label = Label(frame2, text="Nome: ")
client_name_label.pack(anchor=W)
client_name_entry = Entry(frame2)
client_name_entry.pack(anchor=W)

client_address_label = Label(frame2, text="Indirizzo: ")
client_address_label.pack(anchor=W)
client_address_entry = Entry(frame2)
client_address_entry.pack(anchor=W)

client_city_label = Label(frame2, text="Citta: ")
client_city_label.pack(anchor=W)
client_city_entry = Entry(frame2)
client_city_entry.pack(anchor=W)

client_state_label = Label(frame2, text="Provincia: ")
client_state_label.pack(anchor=W)
client_state_entry = Entry(frame2)
client_state_entry.pack(anchor=W)

client_zip_label = Label(frame2, text="Cap: ")
client_zip_label.pack(anchor=W)
client_zip_entry = Entry(frame2)
client_zip_entry.pack(anchor=W)

client_email_label = Label(frame2, text="Email: ")
client_email_label.pack(anchor=W)
client_email_entry = Entry(frame2)
client_email_entry.pack(anchor=W)

client_phone_label = Label(frame2, text="Tel: ")
client_phone_label.pack(anchor=W)
client_phone_entry = Entry(frame2)
client_phone_entry.pack(anchor=W)

client_vat_label = Label(frame2, text="IVA: ")
client_vat_label.pack(anchor=W)
client_vat_entry = Entry(frame2)
client_vat_entry.pack(anchor=W)


root.mainloop()
