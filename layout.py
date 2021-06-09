from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Quetzalcoalt")
root.geometry("1280x720")
root.config(bg="#ff00ff")
root.resizable(False, False)

main_frame = Frame(root, width=1280, height=670, bg="#ff0000")
main_frame.pack(side=TOP)
main_frame.pack_propagate(False)
statusbar_frame = Frame(root, width=1280, height=50, bg="#303030")
statusbar_frame.pack(side=TOP)
statusbar_frame.pack_propagate(False)
left_panel_frame = Frame(main_frame, width=300, height=670, bg="#202020")
left_panel_frame.pack(side=LEFT)
left_panel_frame.pack_propagate(False)
right_panel_frame = Frame(main_frame, width=980, height=670, bg="#101010")
right_panel_frame.pack(side=LEFT)
right_panel_frame.pack_propagate(False)


entry_width = 20
pad_y = 5
label_pad_x = 3
entry_pad_x = 8

# ---------------------------------------------------------------------------------------
# metadata
# ---------------------------------------------------------------------------------------
metadata_frame = Frame(left_panel_frame, padx=10, pady=10, bg="#202020", border=0)
metadata_frame.pack(side=TOP, pady=pad_y, fill=BOTH)

metadata_id_frame = Frame(metadata_frame, bg="#202020")
metadata_id_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
metadata_id_label = Label(metadata_id_frame, text="Certificate ID:", bg="#202020", fg="#f2f2f2")
metadata_id_label.pack(side=LEFT, padx=label_pad_x)
metadata_id_entry = Entry(metadata_id_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
metadata_id_entry.pack(side=RIGHT, padx=entry_pad_x)

# ---------------------------------------------------------------------------------------
# supplier data
# ---------------------------------------------------------------------------------------
style = ttk.Style()
style.theme_create("dark", settings={
	".": {
		"configure": {
			"background": "#202020",
		}
	},
	"TNotebook": {
		"configure": {
			"background": "#202020",
			"borderwidth": 0,
		}
	},
	"TNotebook.Tab": {
		"configure": {
			"background": "#101010",
			"foreground": "#888888",
			"borderwidth": 0,
			"padding": [10,2],
		},
		"map": {
			"background": [("selected", "#303030")],
			"foreground": [("selected", "#f2f2f2")],
		}
	}
})
style.theme_use("dark")

background_color = "#303030"

notebook = ttk.Notebook(left_panel_frame)

supplier_frame = Frame(notebook, bg=background_color, border=0, padx=10, pady=10)
supplier_frame.pack(side=TOP, pady=pad_y, fill=BOTH)

client_frame = Frame(notebook, bg=background_color, border=0)
client_frame.pack(side=TOP, pady=pad_y, fill=BOTH)


notebook.add(supplier_frame, text="Supplier")
notebook.add(client_frame, text="Client")
notebook.pack(side=TOP, pady=pad_y, fill=BOTH)

supplier_name_frame = Frame(supplier_frame, bg=background_color)
supplier_name_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_name_label = Label(supplier_name_frame, text="Name:", bg=background_color, fg="#f2f2f2")
supplier_name_label.pack(side=LEFT, padx=label_pad_x)
supplier_name_entry = Entry(supplier_name_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_name_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_address_frame = Frame(supplier_frame, bg=background_color)
supplier_address_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_address_label = Label(supplier_address_frame, text="Address:", bg=background_color, fg="#f2f2f2")
supplier_address_label.pack(side=LEFT, padx=label_pad_x)
supplier_address_entry = Entry(supplier_address_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_address_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_city_frame = Frame(supplier_frame, bg=background_color)
supplier_city_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_city_label = Label(supplier_city_frame, text="City:", bg=background_color, fg="#f2f2f2")
supplier_city_label.pack(side=LEFT, padx=label_pad_x)
supplier_city_entry = Entry(supplier_city_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_city_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_state_frame = Frame(supplier_frame, bg=background_color)
supplier_state_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_state_label = Label(supplier_state_frame, text="State:", bg=background_color, fg="#f2f2f2")
supplier_state_label.pack(side=LEFT, padx=label_pad_x)
supplier_state_entry = Entry(supplier_state_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_state_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_zipcode_frame = Frame(supplier_frame, bg=background_color)
supplier_zipcode_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_zipcode_label = Label(supplier_zipcode_frame, text="Zipcode:", bg=background_color, fg="#f2f2f2")
supplier_zipcode_label.pack(side=LEFT, padx=label_pad_x)
supplier_zipcode_entry = Entry(supplier_zipcode_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_zipcode_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_country_frame = Frame(supplier_frame, bg=background_color)
supplier_country_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_country_label = Label(supplier_country_frame, text="Country:", bg=background_color, fg="#f2f2f2")
supplier_country_label.pack(side=LEFT, padx=label_pad_x)
supplier_country_entry = Entry(supplier_country_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_country_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_email_frame = Frame(supplier_frame, bg=background_color)
supplier_email_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_email_label = Label(supplier_email_frame, text="Email:", bg=background_color, fg="#f2f2f2")
supplier_email_label.pack(side=LEFT, padx=label_pad_x)
supplier_email_entry = Entry(supplier_email_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_email_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_phone_frame = Frame(supplier_frame, bg=background_color)
supplier_phone_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_phone_label = Label(supplier_phone_frame, text="Phone:", bg=background_color, fg="#f2f2f2")
supplier_phone_label.pack(side=LEFT, padx=label_pad_x)
supplier_phone_entry = Entry(supplier_phone_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_phone_entry.pack(side=RIGHT, padx=entry_pad_x)

supplier_vat_frame = Frame(supplier_frame, bg=background_color)
supplier_vat_frame.pack(side=TOP, pady=pad_y, fill=BOTH)
supplier_vat_label = Label(supplier_vat_frame, text="VAT:", bg=background_color, fg="#f2f2f2")
supplier_vat_label.pack(side=LEFT, padx=label_pad_x)
supplier_vat_entry = Entry(supplier_vat_frame, width=entry_width, border=0, highlightthickness=0, background="#808080")
supplier_vat_entry.pack(side=RIGHT, padx=entry_pad_x)


root.mainloop()
