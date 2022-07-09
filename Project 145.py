
from tkinter import *
root = Tk()

root.title("Nakul's Driving License")

root.configure(bg="#dedaf0")
canvas=Canvas(root,width=700,height=550)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 700, 45, fill="#1a0f4d"   )

label_heading = canvas.create_text(200,20, font=('Helvetica', '24', 'bold italic') ,text="Nakul's Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)

def myLicense():
    id_value = 19827198349
    print(type(id_value))
    name = "Nakul Sanjay"
    print(type(name))
    dob = "20 November 2009"
    print(type(dob))
    pin = 12345
    print(type(pin))
    address = "Taj Mahal, Agra"
    print(type(address))
    vehicle_type = ["Two Wheeler"]
    print(type(vehicle_type))
    
    label_id['text'] = id_value
    label_name['text'] = name
    label_dob['text'] = dob
    label_pin['text'] = pin
    label_address['text'] = address
    label_vehicle_type['text'] = vehicle_type
    
    
    
button1 = Button(root, text = "Show my Driving License", command = myLicense)
button1.pack()

button1.configure(width = 20 , activebackground = "#ab99f7", relief= RIDGE)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()


root.mainloop()