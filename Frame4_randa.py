# -*- coding: utf-8 -*-
from Tkinter import Tk, Label, Button,Canvas, NW,BOTH
import tkMessageBox

import PIL
from PIL import Image, ImageTk
from io import BytesIO
# import pymysql
import pymysql

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class BOOK_PROGRAM():
    def connect_DataBase(self):
        conn = pymysql.connect(user="root", password="", host="localhost", database="university")
        return conn

    def show(self, id, table):

        root2 = Tk()
        root2.title("Book Bank")
        root2.geometry("269x345")

        canvas = Canvas(root2)
        canvas.pack(fill=BOTH, expand=1)

        im = Image.open('wall4.jpg')
        img = ImageTk.PhotoImage(image=im)
        # Label(canvas,image=img).place(x=0, y=0)
        # Label(canvas, image=img, anchor=NW).place(x=0, y=0)
        canvas.create_image(0,0,image=img,anchor=NW)
        Label(canvas, text=unicode("معلومات البائع", "utf-8"), bg='black', fg="white", width=50).pack(pady=7)

        sql = "select * from {} where id = {}".format(table, id)
        connect = self.connect_DataBase()
        cur = connect.cursor()
        try:
            cur.execute(sql)
            data = cur.fetchone()
            connect.commit()
        except Exception as e:
            connect.rollback()
            print e

        connect.close()

        file_like = BytesIO(data[2])
        img1 = PIL.Image.open(file_like, mode='r').convert('RGB')
        im1 = img1.resize((130, 150), PIL.Image.ANTIALIAS)  # to chage image size
        im = ImageTk.PhotoImage(im1)
        # canvas.create_image(60, 29, image=im, anchor=NW)
        Label(root2, image=im, anchor=NW).place(x=60, y=30)
        Label(root2,bg='black',fg='white', text="Book Name: {}".format(data[1])).place(x=59, y=188)
        Label(root2, bg='black', fg='white', text="Book Price: {} SR".format(data[5])).place(x=59, y=208)
        Label(root2,bg='black',fg='white', text="Seller Email:{}".format(data[3])).place(x=59, y=228)
        Label(root2,bg='black',fg='white', text="Phone Number:{}".format(data[4])).place(x=59, y=248)



        def Confirm():
            tkMessageBox.showinfo(unicode("تأكيد","utf-8"),unicode(" تم تأكيد طلبك بنجاح\n"
                                           "سيتم التواصل معك من قبل مالك الكتاب\n\n"
                                           "شكرا لك !","utf-8"))
            connect = self.connect_DataBase()
            cur = connect.cursor()

            sql = "delete from {} where id = {}".format(table, id)
            cur.execute(sql)
            connect.commit()
            connect.close()
            root2.destroy()
            # self.Basic_frame()

        def Cancel():
            root2.destroy()
            # self.Basic_frame()

        def back():
            root2.destroy()
            from FrameSpecialty import Framespecialty
            Framespecialty().frame1()


        Button(root2,bg='black',fg='white', text=unicode("تأكيد", "utf-8"), command=Confirm,width=5).place(x=135, y=281)
        Button(root2,bg='black',fg='white', text=unicode("إلغاء", "utf-8"), command=Cancel,width=5).place(x=60, y=281)
        Button(root2, bg='black', fg='white', text=unicode("عودة", "utf-8"), command=back, width=5).place(x=97,y=310)
        root2.mainloop()




