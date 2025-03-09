# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# import mysql.connector
# from tkinter import messagebox, filedialog

# class Criminal:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry('3840x2160+0+0')
#         self.root.title("CRIMINAL'S MANAGEMENT SYSTEM")

#         # variable
#         self.var_case_id = StringVar()
#         self.var_criminal_no = StringVar()
#         self.var_criminal_name = StringVar()
#         self.var_nickname = StringVar()
#         self.var_arrest_date = StringVar()
#         self.var_date_of_crime = StringVar()
#         self.var_address = StringVar()
#         self.var_age = StringVar()
#         self.var_occupation = StringVar()
#         self.var_birthmark = StringVar()
#         self.var_crime_type = StringVar()
#         self.var_father_name = StringVar()
#         self.var_gender = StringVar()
#         self.var_wanted = StringVar()
#         self.var_image = StringVar()  # Variable to store image path

#         label_title = Label(self.root, text="CRIMINAL'S MANAGEMENT SYSTEM ", font=('times new roman', 40, 'bold'), bg='black', fg='gold')
#         label_title.place(x=0, y=0, width=1530, height=70)

#         # ncr logo
#         img_logo = Image.open(r"C:\images\quasar.jpg")
#         img_logo = img_logo.resize((60, 60), Image.LANCZOS)
#         self.photo_logo = ImageTk.PhotoImage(img_logo)

#         self.logo = Label(self.root, image=self.photo_logo)
#         self.logo.place(x=80, y=5, width=60, height=60)

#         # Main Frame
#         Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
#         Main_frame.place(x=10, y=90, width=1515, height=690)

#         # Upper Frame
#         upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information ', font=('times new roman', 11, 'bold'), bg='white', fg='red')
#         upper_frame.place(x=10, y=10, width=1500, height=315)
#         upper_frame.grid_columnconfigure(6, minsize=250, weight=0)

#         # Labels and Entries
#         # Case ID
#         caseid = Label(upper_frame, text='Case ID :', font=('arial', 14, 'bold'), bg='white')
#         caseid.grid(row=0, column=0, padx=2, sticky=W)

#         caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=22, font=('arial', 9, 'bold'))
#         caseentry.grid(row=0, column=1, padx=2, sticky=W)

#         # Criminal number
#         lbl_criminal_no = Label(upper_frame, font=('arial', 14, 'bold'), text='Criminal NO:', bg='white')
#         lbl_criminal_no.grid(row=0, column=2, padx=2, pady=7, sticky=W)

#         txt_criminal_no = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=22, font=('arial', 9, 'bold'))
#         txt_criminal_no.grid(row=0, column=3, padx=2, pady=7)

#         # Criminal Name
#         lbl_Name = Label(upper_frame, text='Criminal Name :', font=('arial', 14, 'bold'), bg='white')
#         lbl_Name.grid(row=1, column=0, padx=2, pady=2, sticky=W)

#         txt_Name = ttk.Entry(upper_frame, textvariable=self.var_criminal_name, width=22, font=('arial', 9, 'bold'))
#         txt_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)

#         # Nick Name
#         lbl_Nick_Name = Label(upper_frame, text='Criminal Nick Name:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Nick_Name.grid(row=1, column=2, padx=2, pady=2, sticky=W)

#         txt_Nick_Name = ttk.Entry(upper_frame, textvariable=self.var_nickname, width=22, font=('arial', 9, 'bold'))
#         txt_Nick_Name.grid(row=1, column=3, sticky=W, padx=2, pady=7)

#         # Arrest Date
#         lbl_Arrest_Date = Label(upper_frame, text='Arrest date:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Arrest_Date.grid(row=2, column=0, padx=2, pady=2, sticky=W)

#         txt_Arrest_Date = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=22, font=('arial', 9, 'bold'))
#         txt_Arrest_Date.grid(row=2, column=1, sticky=W, padx=2, pady=7)

#         # Date of Crime
#         lbl_Date_of_crime = Label(upper_frame, text='Date Of Crime:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Date_of_crime.grid(row=2, column=2, padx=2, pady=2, sticky=W)

#         txt_Date_of_crime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=22, font=('arial', 9, 'bold'))
#         txt_Date_of_crime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

#         # Address
#         lbl_Address = Label(upper_frame, text='Address:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Address.grid(row=3, column=0, padx=2, pady=2, sticky=W)

#         txt_Address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=('arial', 9, 'bold'))
#         txt_Address.grid(row=3, column=1, sticky=W, padx=2, pady=7)

#         # Age
#         lbl_Age = Label(upper_frame, text='Age:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Age.grid(row=3, column=2, padx=2, pady=2, sticky=W)

#         txt_Age = ttk.Entry(upper_frame, textvariable=self.var_age, width=22, font=('arial', 9, 'bold'))
#         txt_Age.grid(row=3, column=3, sticky=W, padx=2, pady=7)

#         # Occupation
#         lbl_Occupation = Label(upper_frame, text='Occupation:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Occupation.grid(row=4, column=0, padx=2, pady=2, sticky=W)

#         txt_Occupation = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=22, font=('arial', 9, 'bold'))
#         txt_Occupation.grid(row=4, column=1, sticky=W, padx=2, pady=7)

#         # Birth Mark
#         lbl_Birth_Mark = Label(upper_frame, text='Birth Mark:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Birth_Mark.grid(row=4, column=2, padx=2, pady=2, sticky=W)

#         txt_Birth_Mark = ttk.Entry(upper_frame, textvariable=self.var_birthmark, width=22, font=('arial', 9, 'bold'))
#         txt_Birth_Mark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

#         # Crime Type
#         lbl_Crime_type = Label(upper_frame, text='Crime Type:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Crime_type.grid(row=0, column=4, padx=2, pady=2, sticky=W)

#         txt_Crime_Type = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=22, font=('arial', 9, 'bold'))
#         txt_Crime_Type.grid(row=0, column=5, sticky=W, padx=2, pady=7)

#         # Father Name
#         lbl_Father_Name = Label(upper_frame, text='Father Name:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Father_Name.grid(row=1, column=4, padx=2, pady=2, sticky=W)

#         txt_Father_name = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=22, font=('arial', 9, 'bold'))
#         txt_Father_name.grid(row=1, column=5, sticky=W, padx=2, pady=7)

#         # Gender
#         lbl_Gender = Label(upper_frame, text='Gender:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Gender.grid(row=2, column=4, padx=2, pady=2, sticky=W)

#         # Radio button for gender 
#         radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
#         radio_frame_gender.place(x=825, y=76, width=160, height=31)

#         male = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Male', value='male', font=('arial', 10, 'bold'), bg='white')
#         male.grid(row=0, column=0, pady=2, padx=5, sticky=W)

#         female = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Female', value='female', font=('arial', 10, 'bold'), bg='white')
#         female.grid(row=0, column=1, pady=2, padx=5, sticky=W)

#         # Wanted
#         lbl_Most_Wanted = Label(upper_frame, text='Most Wanted:', font=('arial', 14, 'bold'), bg='white')
#         lbl_Most_Wanted.grid(row=3, column=4, padx=2, pady=2, sticky=W)

#         # Radio button for wanted
#         radio_frame_Most_Wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
#         radio_frame_Most_Wanted.place(x=825, y=118, width=160, height=31)

#         Yes = Radiobutton(radio_frame_Most_Wanted, variable=self.var_wanted, text='Yes', value='Yes', font=('arial', 10, 'bold'), bg='white')
#         Yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)

#         No = Radiobutton(radio_frame_Most_Wanted, variable=self.var_wanted, text='No', value='No', font=('arial', 10, 'bold'), bg='white')
#         No.grid(row=0, column=1, pady=2, padx=5, sticky=W)

#         # Image Upload Button
#         btn_upload_image = Button(upper_frame, text='Upload Image', command=self.upload_image, font=('arial', 12, 'bold'), width=14, bg='blue', fg='white')
#         btn_upload_image.grid(row=5, column=0, padx=5, pady=5)

#         # Buttons
#         button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
#         button_frame.place(x=5, y=230, width=725, height=50)

#         # Add button
#         btn_add = Button(button_frame, command=self.add_data, text='Record Save', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
#         btn_add.grid(row=0, column=0, padx=5, pady=7)

#         # Update button
#         btn_update = Button(button_frame, command=self.update_data, text='Update', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
#         btn_update.grid(row=0, column=1, padx=5, pady=7)

#         # Delete button
#         btn_delete = Button(button_frame, command=self.delete_data, text='Delete', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
#         btn_delete.grid(row=0, column=2, padx=5, pady=7)

#         # Clear button
#         btn_clear = Button(button_frame, command=self.clear_data, text='Clear', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
#         btn_clear.grid(row=0, column=3, padx=5, pady=7)

#         # Image display
#         # self.img_display = Label(upper_frame, bg='white')
#         # self.img_display.grid(row=0, column=6, rowspan=5, padx=10, pady=10)
#         self.img_display = Label(upper_frame, bg='white')
#         self.img_display.grid(row=0, column=6, rowspan=5, padx=10, pady=10, sticky='nsew')
#         # Down Frame
#         Down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information Table ', font=('times new roman', 11, 'bold'), bg='white', fg='red')
#         Down_frame.place(x=10, y=330, width=1500, height=350)

#         # Search Frame
#         search_frame = LabelFrame(Down_frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=('times new roman', 11, 'bold'), bg='white', fg='red')
#         search_frame.place(x=0, y=0, width=1480, height=83)

#         search_by = Label(search_frame, text='Search By:', font=('arial', 14, 'bold'), bg='red')
#         search_by.grid(row=0, column =0, padx=20, sticky=W)

#         self.var_com_search = StringVar()

#         combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=('arial', 12, 'bold'), width=18, state='readonly')
#         combo_search_box['value'] = ('Select Option', 'Case_ID', 'Criminal_NO')
#         combo_search_box.current(0)
#         combo_search_box.grid(row=0, column=1, sticky=W, padx=10)

#         self.var_search = StringVar()
#         search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=('arial', 12, 'bold'))
#         search_txt.grid(row=0, column=2, padx=10, sticky=W)

#         # Search button
#         btn_search = Button(search_frame, command=self.search_data, text='Search', font=('arial', 10, 'bold'), width=14, bg='blue', fg='white')
#         btn_search.grid(row=0, column=3, padx=10, pady=15)

#         # All button
#         btn_all = Button(search_frame, command=self.fetch_data, text='Show All', font=('arial', 10, 'bold'), width=14, bg='blue', fg='white')
#         btn_all.grid(row=0, column=4, padx=10, pady=15)

#         crimeagency = Label(search_frame, text='NATIONAL CRIME AGENCY:', font=('arial', 20, 'bold'), bg='white', fg='crimson')
#         crimeagency.grid(row=0, column=6, padx=50,sticky=W)

#         # Table frame
#         table_frame = Frame(Down_frame, bd=2, relief=RIDGE)
#         table_frame.place(x=0, y=90, width=1490, height=235)

#         # Scrollbar
#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.criminal_table = ttk.Treeview(table_frame, column=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)

#         scroll_x.config(command=self.criminal_table.xview)
#         scroll_y.config(command=self.criminal_table.yview)

#         self.criminal_table.heading('1', text='Case Id')
#         self.criminal_table.heading('2', text='Criminal NO')
#         self.criminal_table.heading('3', text='Criminal Name')
#         self.criminal_table.heading('4', text='NickName')
#         self.criminal_table.heading('5', text='Arrest Date')
#         self.criminal_table.heading('6', text='Date of Crime')
#         self.criminal_table.heading('7', text='Address')
#         self.criminal_table.heading('8', text='Age')
#         self.criminal_table.heading('9', text='Occupation')
#         self.criminal_table.heading('10', text='Birth Mark')
#         self.criminal_table.heading('11', text='Crime Type')
#         self.criminal_table.heading('12', text='Father Name')
#         self.criminal_table.heading('13', text='Gender')
#         self.criminal_table.heading('14', text='Wanted')

#         self.criminal_table['show'] = 'headings'
#         self.criminal_table.column('1', width=100)
#         self.criminal_table.column('2', width=100)
#         self.criminal_table.column('3', width=100)
#         self.criminal_table.column('4', width=100)
#         self.criminal_table.column('5', width=100)
#         self.criminal_table.column('6', width=100)
#         self.criminal_table.column('7', width=100)
#         self.criminal_table.column('8', width=100)
#         self.criminal_table.column('9', width=100)
#         self.criminal_table.column('10', width=100)
#         self.criminal_table.column('11', width=100)
#         self.criminal_table.column('12', width=100)
#         self.criminal_table.column('13', width=100)
#         self.criminal_table.column('14', width=100)

#         self.criminal_table.pack(fill=BOTH, expand=1)

#         self.criminal_table.bind('<ButtonRelease>', self.get_cursor)

#         self.fetch_data()

#     def upload_image(self):
#         file_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image Files", ".jpg;.jpeg;.png "), ("All Files", ".*")))
#         if file_path:
#             self.var_image.set(file_path)  # Store the image path
#             img = Image.open(file_path)
#             img = img.resize((250,250), Image.LANCZOS)  # Resize image for display
#             self.photo_image = ImageTk.PhotoImage(img)
#             self.img_display.config(image=self.photo_image)  # Display the image

#     def add_data(self):
#         if self.var_case_id.get() == "":
#             messagebox.showerror('Error', 'All fields are required')
#         else:
#             try:
#                 conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
#                 my_cursor = conn.cursor()
#                 my_cursor.execute('insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
#                     self.var_case_id.get(),
#                     self.var_criminal_no.get(),
#                     self.var_criminal_name.get(),
#                     self.var_nickname.get(),
#                     self.var_arrest_date.get(),
#                     self.var_date_of_crime.get(),
#                     self.var_address.get(),
#                     self.var_age.get(),
#                     self.var_occupation.get(),
#                     self.var_birthmark.get(),
#                     self.var_crime_type.get(),
#                     self.var_father_name.get(),
#                     self.var_gender.get(),
#                     self.var_wanted.get(),
#                     self.var_image.get()  # Include image path
#                 ))

#                 conn.commit()
#                 self.fetch_data()
#                 self.clear_data()
#                 conn.close()
#                 messagebox.showinfo('Success', 'Criminal record has been added')

#             except Exception as es:
#                 messagebox.showerror('Error', f'Due To {str(es)}')

#     def fetch_data(self):
#         conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
#         my_cursor = conn.cursor()
#         my_cursor.execute('select * from criminal1')
#         data = my_cursor.fetchall()
#         if len(data) != 0:
#             self.criminal_table.delete(*self.criminal_table.get_children())
#             for i in data:
#                 self.criminal_table.insert('', END, values=i)
#         conn.commit()
#         conn.close()

#     def get_cursor(self, event=""):
#         cursor_row = self.criminal_table.focus()
#         content = self.criminal_table.item(cursor_row)
#         data = content['values']

#         self.var_case_id.set(data[0])
#         self.var_criminal_no.set(data[1])
#         self.var_criminal_name.set(data[2])
#         self.var_nickname.set(data[3])
#         self.var_arrest_date.set(data[4])
#         self.var_date_of_crime.set(data[5])
#         self.var_address.set(data[6])
#         self.var_age.set(data[7])
#         self.var_occupation.set(data[8])
#         self.var_birthmark.set(data[9])
#         self.var_crime_type.set(data[10])
#         self.var_father_name.set(data[11])
#         self.var_gender.set(data[12])
#         self.var_wanted.set(data[13])
#         self.var_image.set(data[14])  # Get image path

#         # Display the image
#         img_path = self.var_image.get()
#         if img_path:
#             img = Image.open(img_path)
#             img = img.resize((250, 250), Image.LANCZOS)
#             self.photo_image = ImageTk.PhotoImage(img)
#             self.img_display.config(image=self.photo_image)

#     def update_data(self):
#         if self.var_case_id.get() == "":
#             messagebox.showerror('Error', 'All fields are required')
#         else:
#             try:
#                 update = messagebox.askyesno('Update', 'Are you sure update this criminal record')
#                 if update > 0:
#                     conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
#                     my_cursor = conn.cursor()
#                     my_cursor.execute('update criminal1 set criminal_no=%s, criminal_name=%s, nickname=%s, arrest_date=%s, date_of_crime=%s, address=%s, age=%s, occupation=%s, birthmark=%s, crime_type=%s, father_name=%s, gender=%s, wanted=%s, image=%s where case_id=%s', (
#                         self.var_criminal_no.get(),
#                         self.var_criminal_name.get(),
#                         self.var_nickname.get(),
#                         self.var_arrest_date.get(),
#                         self.var_date_of_crime.get(),
#                         self.var_address.get(),
#                         self.var_age.get(),
#                         self.var_occupation.get(),
#                         self.var_birthmark.get(),
#                         self.var_crime_type.get(),
#                         self.var_father_name.get(),
#                         self.var_gender.get(),
#                         self.var_wanted.get(),
#                         self.var_image.get(),  # Include image path
#                         self.var_case_id.get()
#                     ))
#                 else:
#                     if not update:
#                         return

#                 conn.commit()
#                 self.fetch_data()
#                 self.clear_data()
#                 conn.close()
#                 messagebox.showinfo('Success', 'Criminal record successfully updated')
#             except Exception as es:
#                 messagebox.showerror('Error', f'Due To {str(es)}')

#     def delete_data(self):
#         if self.var_case_id.get() == "":
#             messagebox.showerror('Error', 'All fields are required')
#         else:
#             try:
#                 delete = messagebox.askyesno('Delete', 'Are you sure delete this criminal record')
#                 if delete > 0:
#                     conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
#                     my_cursor = conn.cursor()
#                     sql = 'delete from criminal1 where case_id=%s'
#                     value = (self.var_case_id.get(),)
#                     my_cursor.execute(sql, value)
#                 else:
#                     if not delete:
#                         return
#                 conn.commit()
#                 self.fetch_data()
#                 self.clear_data()
#                 conn.close()

#                 messagebox.showinfo('Success', 'Criminal record has been deleted')

#             except Exception as es:
#                 messagebox.showerror('Error', f'Due To {str(es)}')

#     def clear_data(self):
#         self.var_case_id.set("")
#         self.var_criminal_no.set("")
#         self.var_criminal_name.set("")
#         self.var_nickname.set("")
#         self.var_arrest_date.set("")
#         self.var_date_of_crime.set("")
#         self.var_address.set("")
#         self.var_age.set("")
#         self.var_occupation.set("")
#         self.var_birthmark.set("")
#         self.var_crime_type.set("")
#         self.var_father_name.set("")
#         self.var_gender.set("")
#         self.var_wanted.set("")
#         self.var_image.set("")  # Clear image path
#         self.img_display.config(image='')  # Clear displayed image

#     def search_data(self):
#         if self.var_com_search.get() == "Select Option" or self.var_search.get() == "":
#             messagebox.showerror('Error', 'All fields are required')
#         else:
#             try:
#                 conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
#                 my_cursor = conn.cursor()
#                 my_cursor.execute('select * from criminal1 where ' + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get() + "%'"))
#                 rows = my_cursor.fetchall()
#                 if len(rows) != 0:
#                     self.criminal_table.delete(*self.criminal_table.get_children())
#                     for i in rows:
#                         self.criminal_table.insert('', END, values=i)
#                 conn.commit()
#                 conn.close()

#             except Exception as es:
#                 messagebox.showerror('Error', f'Due To {str(es)}')

# if __name__ == "__main__":
#     root = Tk()
#     obj = Criminal(root)
# root.mainloop()



from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox, filedialog

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('3840x2160+0+0')
        self.root.title("CRIMINAL'S MANAGEMENT SYSTEM")

        # variable
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_criminal_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()
        self.var_image = StringVar()  # Variable to store image path

        label_title = Label(self.root, text="CRIMINAL'S MANAGEMENT SYSTEM ", font=('times new roman', 40, 'bold'), bg='black', fg='gold')
        label_title.place(x=0, y=0, width=1530, height=70)

        # ncr logo
        img_logo = Image.open(r"C:\images\quasar.jpg")
        img_logo = img_logo.resize((60, 60), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=80, y=5, width=60, height=60)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=90, width=1515, height=690)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information ', font=('times new roman', 11, 'bold'), bg='white', fg='red')
        upper_frame.place(x=10, y=10, width=1500, height=315)
        upper_frame.grid_columnconfigure(6, minsize=250, weight=0)

        # Labels and Entries
        # Case ID
        caseid = Label(upper_frame, text='Case ID :', font=('arial', 14, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=20, font=('arial', 13, 'bold'))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)

        # Criminal number
        lbl_criminal_no = Label(upper_frame, font=('arial', 14, 'bold'), text='Criminal NO:', bg='white')
        lbl_criminal_no.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_criminal_no = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=20, font=('arial',13, 'bold'))
        txt_criminal_no.grid(row=0, column=3, padx=2, pady=7)

        # Criminal Name
        lbl_Name = Label(upper_frame, text='Criminal Name :', font=('arial', 14, 'bold'), bg='white')
        lbl_Name.grid(row=1, column=0, padx=2, pady=2, sticky=W)

        txt_Name = ttk.Entry(upper_frame, textvariable=self.var_criminal_name, width=20, font=('arial', 13, 'bold'))
        txt_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Nick Name
        lbl_Nick_Name = Label(upper_frame, text='Criminal Nick Name:', font=('arial', 14, 'bold'), bg='white')
        lbl_Nick_Name.grid(row=1, column=2, padx=2, pady=2, sticky=W)

        txt_Nick_Name = ttk.Entry(upper_frame, textvariable=self.var_nickname, width=20, font=('arial', 13, 'bold'))
        txt_Nick_Name.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        # Arrest Date
        lbl_Arrest_Date = Label(upper_frame, text='Arrest date:', font=('arial', 14, 'bold'), bg='white')
        lbl_Arrest_Date.grid(row=2, column=0, padx=2, pady=2, sticky=W)

        txt_Arrest_Date = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=20, font=('arial', 13, 'bold'))
        txt_Arrest_Date.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # Date of Crime
        lbl_Date_of_crime = Label(upper_frame, text='Date Of Crime:', font=('arial', 14, 'bold'), bg='white')
        lbl_Date_of_crime.grid(row=2, column=2, padx=2, pady=2, sticky=W)

        txt_Date_of_crime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=20, font=('arial', 13, 'bold'))
        txt_Date_of_crime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Address
        lbl_Address = Label(upper_frame, text='Address:', font=('arial', 14, 'bold'), bg='white')
        lbl_Address.grid(row=3, column=0, padx=2, pady=2, sticky=W)

        txt_Address = ttk.Entry(upper_frame, textvariable=self.var_address, width=20, font=('arial', 13, 'bold'))
        txt_Address.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # Age
        lbl_Age = Label(upper_frame, text='Age:', font=('arial', 14, 'bold'), bg='white')
        lbl_Age.grid(row=3, column=2, padx=2, pady=2, sticky=W)

        txt_Age = ttk.Entry(upper_frame, textvariable=self.var_age, width=20, font=('arial', 13, 'bold'))
        txt_Age.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # Occupation
        lbl_Occupation = Label(upper_frame, text='Occupation:', font=('arial', 14, 'bold'), bg='white')
        lbl_Occupation.grid(row=4, column=0, padx=2, pady=2, sticky=W)

        txt_Occupation = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=20, font=('arial', 13, 'bold'))
        txt_Occupation.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        # Birth Mark
        lbl_Birth_Mark = Label(upper_frame, text='Birth Mark:', font=('arial', 14, 'bold'), bg='white')
        lbl_Birth_Mark.grid(row=4, column=2, padx=2, pady=2, sticky=W)

        txt_Birth_Mark = ttk.Entry(upper_frame, textvariable=self.var_birthmark, width=20, font=('arial', 13, 'bold'))
        txt_Birth_Mark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Crime Type
        lbl_Crime_type = Label(upper_frame, text='Crime Type:', font=('arial', 14, 'bold'), bg='white')
        lbl_Crime_type.grid(row=0, column=4, padx=2, pady=2, sticky=W)

        txt_Crime_Type = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=20, font=('arial', 13, 'bold'))
        txt_Crime_Type.grid(row=0, column=5, sticky=W, padx=2, pady=7)

        # Father Name
        lbl_Father_Name = Label(upper_frame, text='Father Name:', font=('arial', 14, 'bold'), bg='white')
        lbl_Father_Name.grid(row=1, column=4, padx=2, pady=2, sticky=W)

        txt_Father_name = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=20, font=('arial', 13, 'bold'))
        txt_Father_name.grid(row=1, column=5, sticky=W, padx=2, pady=7)

        # Gender
        lbl_Gender = Label(upper_frame, text='Gender:', font=('arial', 14, 'bold'), bg='white')
        lbl_Gender.grid(row=2, column=4, padx=2, pady=2, sticky=W)

        # Radio button for gender 
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=873, y=120, width=160, height=31)

        male = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Male', value='male', font=('arial', 10, 'bold'), bg='white')
        male.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        female = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Female', value='female', font=('arial', 10, 'bold'), bg='white')
        female.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Wanted
        lbl_Most_Wanted = Label(upper_frame, text='Most Wanted:', font=('arial', 14, 'bold'), bg='white')
        lbl_Most_Wanted.grid(row=3, column=4, padx=2, pady=2, sticky=W)

        # Radio button for wanted
        radio_frame_Most_Wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_Most_Wanted.place(x=873, y=175, width=160, height=31)

        Yes = Radiobutton(radio_frame_Most_Wanted, variable=self.var_wanted, text='Yes', value='Yes', font=('arial', 10, 'bold'), bg='white')
        Yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        No = Radiobutton(radio_frame_Most_Wanted, variable=self.var_wanted, text='No', value='No', font=('arial', 10, 'bold'), bg='white')
        No.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Image Frame with fixed size
        self.img_frame = Frame(upper_frame, width=250, height=250, bd=2, relief=RIDGE)
        self.img_frame.grid(row=0, column=6, rowspan=5, padx=10, pady=10, sticky='nsew')
        self.img_frame.grid_propagate(False)  # This prevents the frame from resizing

        self.img_display = Label(self.img_frame, bg='white')
        self.img_display.place(x=0, y=0, relwidth=1, relheight=1)  # Use place manager inside the frame

        

        # Buttons
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=220, width=900, height=50)

        # Add button
        btn_add = Button(button_frame, command=self.add_data, text='Record Save', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=5, pady=7)

        # Update button
        btn_update = Button(button_frame, command=self.update_data, text='Update', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=5, pady=7)

        # Delete button
        btn_delete = Button(button_frame, command=self.delete_data, text='Delete', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=5, pady=7)

        # Clear button
        btn_clear = Button(button_frame, command=self.clear_data, text='Clear', font=('arial', 12, 'bold'), width=16, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=5, pady=7)

        #uplaod image button
        btn_upload_image = Button(button_frame, text='Upload Image', command=self.upload_image, font=('arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_upload_image.grid(row=0, column=4, padx=5, pady=7)

        # Down Frame
        Down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information Table ', font=('times new roman', 11, 'bold'), bg='white', fg='red')
        Down_frame.place(x=10, y=330, width=1500, height=350)

        # Search Frame
        search_frame = LabelFrame(Down_frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=('times new roman', 11, 'bold'), bg='white', fg='red')
        search_frame.place(x=0, y=0, width=1480, height=83)

        search_by = Label(search_frame, text='Search By:', font=('arial', 14, 'bold'), bg='red')
        search_by.grid(row=0, column=0, padx=20, sticky=W)

        self.var_com_search = StringVar()

        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=('arial', 12, 'bold'), width=18, state='readonly')
        combo_search_box['value'] = ('Select Option', 'Case_ID', 'Criminal_NO')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=10)

        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=('arial', 12, 'bold'))
        search_txt.grid(row=0, column=2, padx=10, sticky=W)

        # Search button
        btn_search = Button(search_frame, command=self.search_data, text='Search', font=('arial', 10, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=10, pady=15)

        # All button
        btn_all = Button(search_frame, command=self.fetch_data, text='Show All', font=('arial', 10, 'bold'), width=14, bg='blue', fg='white')
        btn_all.grid(row=0, column=4, padx=10, pady=15)

        crimeagency = Label(search_frame, text='NATIONAL CRIME AGENCY:', font=('arial', 20, 'bold'), bg='white', fg='crimson')
        crimeagency.grid(row=0, column=6, padx=50,sticky=W)

        # Table frame
        table_frame = Frame(Down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=90, width=1490, height=235)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1', text='Case Id')
        self.criminal_table.heading('2', text='Criminal NO')
        self.criminal_table.heading('3', text='Criminal Name')
        self.criminal_table.heading('4', text='NickName')
        self.criminal_table.heading('5', text='Arrest Date')
        self.criminal_table.heading('6', text='Date of Crime')
        self.criminal_table.heading('7', text='Address')
        self.criminal_table.heading('8', text='Age')
        self.criminal_table.heading('9', text='Occupation')
        self.criminal_table.heading('10', text='Birth Mark')
        self.criminal_table.heading('11', text='Crime Type')
        self.criminal_table.heading('12', text='Father Name')
        self.criminal_table.heading('13', text='Gender')
        self.criminal_table.heading('14', text='Wanted')

        self.criminal_table['show'] = 'headings'
        self.criminal_table.column('1', width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)
        self.criminal_table.column('14', width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind('<ButtonRelease>', self.get_cursor)

        self.fetch_data()

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image Files", ".jpg;.jpeg;.png "), ("All Files", ".*")))
        if file_path:
            self.var_image.set(file_path)  # Store the image path
            try:
                img = Image.open(file_path)
                img = img.resize((240, 240), Image.LANCZOS)  # Resize to fit the frame
                self.photo_image = ImageTk.PhotoImage(img)
                self.img_display.config(image=self.photo_image)  # Display the image
            except Exception as e:
                messagebox.showerror("Error", f"Could not load image: {str(e)}")

    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_criminal_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthmark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get(),
                    self.var_image.get()  # Include image path
                ))

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been added')

            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal1')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('', END, values=i)
        conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']
        
        if data:  # Check if data is not empty
            self.var_case_id.set(data[0])
            self.var_criminal_no.set(data[1])
            self.var_criminal_name.set(data[2])
            self.var_nickname.set(data[3])
            self.var_arrest_date.set(data[4])
            self.var_date_of_crime.set(data[5])
            self.var_address.set(data[6])
            self.var_age.set(data[7])
            self.var_occupation.set(data[8])
            self.var_birthmark.set(data[9])
            self.var_crime_type.set(data[10])
            self.var_father_name.set(data[11])
            self.var_gender.set(data[12])
            self.var_wanted.set(data[13])
            
            # Check if there's an image path in the data
            if len(data) > 14:
                self.var_image.set(data[14])
                # Display the image
                img_path = self.var_image.get()
                if img_path:
                    try:
                        img = Image.open(img_path)
                        img = img.resize((240, 240), Image.LANCZOS)
                        self.photo_image = ImageTk.PhotoImage(img)
                        self.img_display.config(image=self.photo_image)
                    except Exception as e:
                        messagebox.showerror("Error", f"Could not load image: {str(e)}")
                        self.img_display.config(image='')
            else:
                self.var_image.set("")
                self.img_display.config(image='')

    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure update this criminal record')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update criminal1 set criminal_no=%s, criminal_name=%s, nickname=%s, arrest_date=%s, date_of_crime=%s, address=%s, age=%s, occupation=%s, birthmark=%s, crime_type=%s, father_name=%s, gender=%s, wanted=%s, image=%s where case_id=%s', (
                        self.var_criminal_no.get(),
                        self.var_criminal_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthmark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_image.get(),  # Include image path
                        self.var_case_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo('Success', 'Criminal record successfully updated')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')

    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you sure delete this criminal record')
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
                    my_cursor = conn.cursor()
                    sql = 'delete from criminal1 where case_id=%s'
                    value = (self.var_case_id.get(),)
                    my_cursor.execute(sql, value)
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo('Success', 'Criminal record has been deleted')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_criminal_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        self.var_image.set("")  # Clear image path
        self.img_display.config(image='')  # Clear displayed image

    def search_data(self):
        if self.var_com_search.get() == "Select Option" or self.var_search.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='R shariff', database='rs')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal1 where ' + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get() + "%'"))
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('', END, values=i)
                else:
                    messagebox.showinfo('Not Found', 'No record found with that criteria')
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')

if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
