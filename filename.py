# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo

# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')


# def select_file():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)

#     showinfo(
#         title='Selected File',
#         message=filename
#     )
#     print(filename)

# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )

# open_button.pack(expand=True)


# # run the application
# root.mainloop()

# # def open_send_Window():
    
# #     frame2 = Frame(parent, width=500,height=300,bg='green')
# #     frame2.place(x=0,y=0)
# #     b3 = tk.Button(frame2, text='SEND DATA',command = lambda:open_sender_pin())
# #     b3.place(x=10,y=20)
    
# #     back_button = tk.Button(frame2,text='Back' ,command= lambda : main())
# #     back_button.place(x=10,y=250)
    
    
# # def open_sender_pin():
# #     global key
# #     frame4 =Frame(parent,width=500,height=300,bg='green').place(x=0,y=0)
# #     # frame4.place(x=0,y=0)
    
# #     passw_label = tk.Label(frame4, text = 'Password' )
# #     key1=tk.Entry(frame4)
# #     sub_btn=tk.Button(frame4,text = 'Submit', command=lambda: submit())
# #     passw_label.grid(row=1,column=0)
# #     key1.grid(row=1,column=1)
# #     sub_btn.grid(row=2,column=1)
# #     # browse_file =tk.Button(frame4, text="browse" ,command= lambda: browseFiles()).place(x=90,y=90)
# #     label_file_explorer = Label(parent,
# # 							text = "File Explorer using Tkinter",
# # 							width = 100, height = 4,
# # 							fg = "blue")

	
# #     button_explore = Button(frame4,
# #                             text = "Browse Files",
# #                             command = browseFiles)

# #     button_exit = Button(frame4,
# #                         text = "Exit",
# #                         command = exit)

# #     def submit():
        
# #         global key
# #         key= key1.get()
# #         print(key)
# #         key1.delete(0,END)
# #         dict["key"]=key
# #         print(dict["key"])
        
# #         send()

        


# # def open_recieved_Window():
# #     frame1 = Frame(parent, width=500,height=300,bg='green')
# #     frame1.place(x=0,y=0)
   
# #     b4 = tk.Button(frame1, text='RECIEVED DATA',command= lambda:open_reciever_pin())
# #     b4.place(x=10,y=20)

# #     back_button = tk.Button(frame1,text='Back' ,command=lambda : main())
# #     back_button.place(x=10,y=250)
    
    
# # def open_reciever_pin():
# #     # parent.destroy()
    
# #     global key
# #     frame3 =Frame(parent,width=500,height=300,bg='green').place(x=0,y=0)
# #     # frame3.place(x=0,y=0)

# #     passw_label = tk.Label(frame3, text = 'Password' )
# #     key2=tk.Entry(frame3)
# #     sub_btn=tk.Button(frame3,text = 'Submit', command =lambda: submit())
# #     passw_label.grid(row=1,column=0)
# #     key2.grid(row=1,column=1)
# #     sub_btn.grid(row=2,column=1)


# #     def submit():
# #         global key
# #         key= key2.get()
# #         print(key)
# #         key2.delete(0,END)
# #         dict["key"]=key
# #         print(dict["key"])
# #         Received()






# # def main():
# #     frame = Frame(parent, width=500,height=300,bg='yellow')
# #     frame.place(x=0,y=0)
# #     send_data = tk.Button(frame,
# #                    text="SEND",
# #                    fg="green",
# #                    command=lambda: open_sender_pin(),
# #                    width=15,
# # 				   height=5)

# #     send_data.place(x=10,y=20)


# #     receive_data= tk.Button(frame, 
# #                     text="RECIEVED", 
# #                     fg="red",
# #                     command=lambda: open_reciever_pin(),
# #                     # command=lambda: open_recieved_Window(),
# #                     width=15,
# #                     height=5)
# #     receive_data.place(x=150,y=20)