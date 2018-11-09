# -*- coding: utf-8 -*-
import base64
from Tkinter import Tk, Canvas, BOTH, NW, Label, StringVar, Entry, Button
import tkFileDialog
import tkMessageBox
import pymysql
from PIL import ImageTk,Image
# import pymysql
# import os


class database():

    def connect(self):
        conn=pymysql.connect(user="root",password="",host="localhost",database="university")
        return conn


    def show(self,tableName,tableIndex):
            root = Tk()
            root.title('Book Bank')
            root.geometry("367x600")
            canvas=Canvas(root)
            canvas.pack(fill=BOTH,expand=1)

            im = Image.open('wall3.jpg')
            img = ImageTk.PhotoImage(image=im)
            canvas.create_image(0,0,image=img,anchor=NW)

        # try:
            Label(canvas,text=unicode("إضافة كتاب","utf-8"),bg='black', fg="white",width=80).pack(pady=30)

            # Entries

            bookName = StringVar()
            bookPrice = StringVar()
            folder_path = StringVar()
           # image = Image.open(folder_path.get())

            phoneNo = StringVar()
            email = StringVar()

            def browse_button():
                # Allow user to select a directory and store it in global var called folder_path
                # global folder_path
                filename = tkFileDialog.askopenfilename(filetypes = (("jpg files","*.jpg"),("all files","*.*")))#filetypes=[("Image File",'.jpg')]
                if filename:
                    try:
                        folder_path.set(filename)
                    except:
                        tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'" % filename)
                        return

                # print("filepath:",folder_path.get())



            # Labels

            Label(canvas,text=unicode("اسم الكتاب:","utf-8"),bg='black', fg="white", font=10,width=20).place(x=105,y=100)
            Entry(canvas, bd=3, width=21, textvariable=bookName).place(x=88,y=130)


            Label(canvas, text=unicode(" سعر الكتاب:","utf-8"), bg='black', fg="white", font=10,width=20).place(x=105,y=180)
            Entry(canvas, bd=3, width=21, textvariable=bookPrice).place(x=88,y=210)


            Label(canvas, text=unicode("صورة الكتاب:","utf-8"),bg='black', fg="white",width=19).place(x=100,y=260)
            Button(canvas,text="Browse",width=10,bg='black', fg="white",command=browse_button).place(x=130,y=290)

            Label(canvas, text=unicode("رقم الجوال:","utf-8"),bg='black', fg="white", font=10,width=20).place(x=105,y=340)
            Entry(canvas, bd=3, width=21, textvariable=phoneNo).place(x=88,y=370)

            Label(canvas, text=unicode("البريد الإلكتروني:","utf-8"),bg='black', fg="white", font=10,width=20).place(x=105,y=420)
            Entry(canvas, bd=3, width=21, textvariable=email).place(x=88,y=450)






            def insert_Button():

                sql = "insert into %s (Book_name,Book_image,seller_email,seller_phone,Book_price) VALUES('%s',LOAD_FILE('%s'),'%s','%d',%d)" % (
                    tableName, bookName.get(),folder_path.get(), email.get(), int(phoneNo.get()),float(bookPrice.get()))
                # sql="INSERT INTO %s VALUES('%s',LOAD_FILE('%s'),'%s','%s',$d)"%(np,e,nob,p)

                conn = self.connect()
                cur = conn.cursor()
                try:
                    cur.execute(sql)
                    conn.commit()


                except Exception as e:
                    print sql
                    conn.rollback()
                    print 'For Select instruction: ', e

                conn.close()
                root.destroy()
                from AvailableBooks import AvailableBooks
                AvailableBooks().show(tableIndex)


            Button(canvas,text=unicode("أضف","utf-8"),width=10,bg='black', fg="white",command=insert_Button).place(x=130,y=540)


        # except Exception as e:
        #     print e


            root.mainloop()


