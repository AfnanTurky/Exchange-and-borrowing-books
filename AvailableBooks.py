#-*- coding: utf-8 -*-
import base64
import cStringIO
import io
from io import BytesIO
import pymysql
from Tkinter import Tk, Scrollbar, Canvas, RIGHT, Y, LabelFrame, Frame, Label, Button, E
import PIL
from PIL import ImageTk,Image


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class AvailableBooks():
    tableName=''
    tableindex=0

    def connect(self):
        conn=pymysql.connect(user="root",password="",host="localhost",database="university")
        return conn


    #=====================================================================================================
    # this method take book simple information from data base( name , image, and price) for specific field
    # send from zainab work (frame 1)
    def show(self,field):

        if(field==1):
            self.tableName ="Islamic1"
        elif(field==2):
            self.tableName ="Arabic"
        elif(field==3):
            self.tableName="English"
        elif(field==4):
            self.tableName ="Islamic2"
        elif(field==5):
            self.tableName ="Socialscience"
        elif(field==6):
            self.tableName ="Computerscience"
        elif (field==7):
            self.tableName ="mediaandCommunication"
        elif(field==8):
            self.tableName ="Islamic3"
        elif(field==9):
            self.tableName ="science"
        elif(field==10):
            self.tableName ="Business"
        elif(field==11):
            self.tableName ="Medical"
        elif(field==12):
            self.tableName ="Engineering"
        elif(field==13):
            self.tableName="primary"

        self.tableindex=field
        sql="select `Book_name`, `Book_image`, `Book_price` from {}".format(self.tableName)
        data=[]
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            data=cur.fetchall()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print 'For Select instruction: ',e

        conn.close()
        # for i in data:
        #     print i
        if len(data)==0:
            self.displayFrame('NoBooks')
        else:

            self.displayFrame(data)

        # this method display the frame containing all book information for field specified in show method
    def displayFrame(self,data):
        root = Tk()
        root.title('Book Bank')
        root.geometry("380x620")
        yscrollbar = Scrollbar(root)
        canvas = Canvas(root, background="cadetblue4", yscrollcommand=yscrollbar.set)  # BG="#D2D2D2"



        yscrollbar.config(command=canvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        # Create the frame which will hold the widgets
        canvas.pack(fill="both", expand=1)

        # im = PhotoImage(file='/Users/RaMD/PycharmProjects/Exchange_Borrowing_Books/wall2.gif')

        lf = LabelFrame(canvas, text=unicode("قائمة الكتب", "utf-8"), bg='cadetblue4', fg='gray99').grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=80,
                                                                                                             pady=50)  # pack(expand=1, padx=20, pady=30, ipadx=20, ipady=18)
        frame = Frame(lf)

        im = Image.open('wall3.jpg')
        img = ImageTk.PhotoImage(image=im)
        # canvas.create_image(0, 0, anchor=NE, image=img)
        Label(canvas, image=img).grid(row=0, column=0)
        Label(root, text=unicode("الكتب المتوفرة", "utf-8"), bg='black', fg="white", width=40).place(x=0,y=0)

        # method for book pic botton
        def take(id,tableName):
            root.destroy()
            from Frame4_randa import BOOK_PROGRAM
            BOOK_PROGRAM().show(id,tableName)

        def insert(tableName,tableIndex):
            print('entered ')
            root.destroy()
            from insertFrame import database
            database().show(tableName,tableIndex)

        def back():
            root.destroy()
            from FrameSpecialty import Framespecialty
            Framespecialty().frame1()


        if (data)=='NoBooks':
            Label(canvas,text=unicode("لا يوجد كتب ! ", "utf-8")).place(x=150,y=90)
        else:
            im = list(range(len(data)))

            # this loop place book name image and price thaat gots from database
            for i in range(len(data)):
                #print data[i][1]

                 #to change image size

                im1 = img.resize((150, 150), PIL.Image.ANTIALIAS)
                im[i] = ImageTk.PhotoImage(im1)

                Button(frame,text=unicode(" اسم الكتاب: ", "utf-8") + str(data[i][0]) + '\n' + unicode(" سعر الكتاب: ","utf-8") + str(data[i][2])
                               , compound='top', image=im[i], command=lambda i=i: take(i,self.tableName)).pack()


            # استعارة الكتاب

        # seller button
        Button(canvas, text=unicode(" اضافة كتاب: ", "utf-8"), command=lambda :insert(self.tableName,self.tableindex)).place(x=230,y=300)  # .pack(side=BOTTOM,anchor=SE)#,padx=107,pady=5
        Button(canvas, text=unicode(" عودة إلى قائمة التخصصات: ", "utf-8"), command=back).place(x=195,y=350)  # .pack(side=BOTTOM,anchor=SW)#,padx=90,pady=5

        root.update()
        canvas.create_window(0, 0, window=frame, anchor=E)
        canvas.config(scrollregion=canvas.bbox("all"))
        root.mainloop()




