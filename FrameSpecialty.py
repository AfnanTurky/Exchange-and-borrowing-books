# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image,ImageTk

class Framespecialty():
    def frame1(self):
        root=Tk()
        root.title('Book Bank')
        root.geometry("367x600")

        #Rawan part:
        canvas=Canvas(root)
        im = Image.open('wall3.jpg')
        img = ImageTk.PhotoImage(image=im)
        canvas.create_image(0,0,anchor=NW,image=img)
        canvas.pack(fill=BOTH,expand=1)
        Label(canvas, text=unicode("جامعة الإمام محمد بن سعود الإسلامية","utf-8"), bg='black', fg="white", width=50).pack(pady=30)
        #----------------------------



        lf = LabelFrame(canvas, text=unicode("قائمة الكليات", "utf-8"), bg='cadetblue4', fg='gray99')
        # lf.pack(expand=1, padx=20, pady=30, ipadx=0, ipady=20)
        lf.place(x=50,y=260)

        #Scrollbar
        # s=Scrollbar(lf,orient=VERTCAL)
        # s.grid(row=1,column=1,sticky=N+S+W,padx=0,pady=50)
        scrollbar = Scrollbar(lf, orient=VERTICAL, )
        scrollbar.pack(side=RIGHT, fill=Y)

        #List of Specializations:
        list1=Listbox(lf,yscrollcommand=scrollbar.set, height=5,selectmode=SINGLE,bg='gray79',fg='gray39')




        list1.insert(1,unicode("كلية الشريعة","utf-8"))
        list1.insert(2,unicode("كليةاللغة العربية","utf-8"))
        list1.insert(3,unicode("كلية اللغات الترجمة","utf-8"))
        list1.insert(4,unicode("كلية أصول الدين","utf-8"))
        list1.insert(5,unicode("كلية العلوم الاجتماعية","utf-8"))
        list1.insert(6,unicode("كلية علوم الحاسب والمعلومات","utf-8"))
        list1.insert(7,unicode("كلية الإعلام والاتصال","utf-8"))
        list1.insert(8,unicode("كلية الدعوة", "utf-8"))
        list1.insert(9,unicode("كلية العلوم", "utf-8"))
        list1.insert(10,unicode("كلية الاقتصاد والعلوم الإدارية","utf-8"))
        list1.insert(11,unicode("كلية الطب","utf-8"))
        list1.insert(12,unicode("كلية الهندسة", "utf-8"))
        list1.insert(13,unicode("البرامج التحضيرية", "utf-8"))

        list1.pack(padx=40, pady=30)
        scrollbar.config(command=list1.yview)
        #function select
        def whatselect():
            p=list1.curselection()
            root.destroy()
            from AvailableBooks import AvailableBooks
            AvailableBooks().show(p[0]+1)


        #Button search
        buttonOK=Button(canvas,text=unicode("بحث","utf-8"),command=whatselect,background='black',foreground='white')
        buttonOK.place(x=165,y=520)



        root.mainloop()



if __name__ == '__main__':
    Framespecialty().frame1()
