from tkinter import *
import sqlite3

root = Tk()


'''
c.execute("""
	CREATE TABLE addresses(
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zip integer
	)
""")
'''

def submit():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	
	c.execute("INSERT INTO addresses VALUES(:first_name, :last_name, :address, :city, :state, :zip)",
		{
			'first_name': first_name.get(),
			'last_name': last_name.get(),
			'address': address.get(),
			'city': city.get(),
			'state': state.get(),
			'zip': zip.get(),
		}
	)
	
	conn.commit()
	conn.close()
	
	first_name.delete(0, END)
	last_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zip.delete(0, END)
	
	

def query():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	
	print_records = ""
	for record in records:
		print_records += str(record[0]) + " " + str(record[6]) + "\n"
		
	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)
	
	conn.commit()
	conn.close()
	
def delete():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	
	c.execute("DELETE FROM addresses WHERE oid=" + delete_entry.get())
	
	conn.commit()
	conn.close()
	
	
def edit():
	global editor
	editor = Tk()
	editor.title("Update Record")
	
	global first_name_editor
	global last_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zip_editor
	
	first_name_editor = Entry(editor, width=30)
	first_name_editor.grid(row=0, column=1, padx=20)
	last_name_editor = Entry(editor, width=30)
	last_name_editor.grid(row=1, column=1)
	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1)
	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1)
	state_editor = Entry(editor, width=30)
	state_editor.grid(row=4, column=1)
	zip_editor = Entry(editor, width=30)
	zip_editor.grid(row=5, column=1)

	first_name_label_editor = Label(editor, text="first_name_label")
	first_name_label_editor.grid(row=0, column=0)
	last_name_label_editor = Label(editor, text="last_name_label")
	last_name_label_editor.grid(row=1, column=0)
	address_label_editor = Label(editor, text="address_label")
	address_label_editor.grid(row=2, column=0)
	city_label_editor = Label(editor, text="city_label")
	city_label_editor.grid(row=3, column=0)
	state_label_editor = Label(editor, text="state_label")
	state_label_editor.grid(row=4, column=0)
	zip_label_editor = Label(editor, text="zip_label")
	zip_label_editor.grid(row=5, column=0)
	
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	
	record_id = delete_entry.get()
	c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
	records = c.fetchall()
	
	for record in records:
		first_name_editor.insert(0, record[0])
		last_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zip_editor.insert(0, record[5])
	
	conn.commit()
	conn.close()
	
	save_button = Button(editor, text="Save", command=save)
	save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
	
def save():
	conn = sqlite3.connect("address_book.db")
	c = conn.cursor()
	
	record_id = delete_entry.get()
	
	c.execute("""
		UPDATE addresses SET 
		first_name = :first_name, 
		last_name = :last_name, 
		address = :address, 
		city = :city, 
		state = :state, 
		zip = :zip 
		WHERE oid = :oid
		""",
		{
			"first_name": first_name_editor.get(),
			"last_name": last_name_editor.get(),
			"address": address_editor.get(),
			"city": city_editor.get(),
			"state": state_editor.get(),
			"zip": zip_editor.get(),
			
			"oid": record_id
		}
	)
	
	conn.commit()
	conn.close()
	
	editor.destroy()
	
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20)
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zip = Entry(root, width=30)
zip.grid(row=5, column=1)

delete_entry = Entry(root, width=30)
delete_entry.grid(row=9, column=1)

first_name_label = Label(root, text="first_name_label")
first_name_label.grid(row=0, column=0)
last_name_label = Label(root, text="last_name_label")
last_name_label.grid(row=1, column=0)
address_label = Label(root, text="address_label")
address_label.grid(row=2, column=0)
city_label = Label(root, text="city_label")
city_label.grid(row=3, column=0)
state_label = Label(root, text="state_label")
state_label.grid(row=4, column=0)
zip_label = Label(root, text="zip_label")
zip_label.grid(row=5, column=0)

delete_label = Label(root, text="id num")
delete_label.grid(row=9, column=0)


	
submit_button = Button(root, text="Add to db", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

query_btn = Button(root, text="Show Record", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

root.mainloop()
