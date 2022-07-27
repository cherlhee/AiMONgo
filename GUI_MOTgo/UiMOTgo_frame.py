#to change the horizontal layout of the middle frame to the verticla layout;

import time
import random
import numpy as np
import cv2


### to make images;
from PIL import Image as IMG
from PIL import ImageTk

### to make Tkinter GUI;
from tkinter import *
from tkinter import ttk


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# import funcPlus


### to make firebase database;
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
#cred= credentials.Certificate('key.json')
#firebase_admin.initialize_app(cred,{'databaseURL':'https://jcr-db-test.firebaseio.com//'})
############################################################################################













class MyGui:

    def __init__(self, root):
        self.root= root
        self.count= 0
        global countPlus

        countPlus= 1000
        print('init countplus: %f'%(countPlus))

        root.title("WKIT Ltd")
        root.geometry("1300x950+50+20")
        root.resizable(True, True)

        self.__main__()
        print('hello, kitty')






        ###to make updating screens;
    def funcUpdate(self):
        # self.count += 1
        self.count = random.random()
        # self.count= random.randint(10, 100000)
        # self.count= random.uniform(10, 100)

        lbl.config(text=str(self.count))
        root.update()







    def funcPlus(self):
        self.count += 1
        lbl.config(text=str(self.count))
        #global countPlus
        global x

        print(countPlus)
        #countPlus= 111
        x= 1
        print(x)



    def funcMinus(self):
        #global countPlus

        self.count -= 1
        lbl.config(text=str(self.count))

        count= 22222222
        print(count)

        countPlus= 222
        print(countPlus)
        print(x)

        xy= 11
        print(xy)






    def funcCamera(self):
        # global lblImg, lblImg2
        # global src
        # fname= 'lenna.png'
        # img_gray= cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        # print(img_gray.ndim, img_gray.shape, img_gray.dtype)
        # cv2.imwrite('lenna_gray.png', img_gray)
        # cv2.imshow('lenna.png')
        print('hello,opencv')


        # fname = 'lenna.jpg'
        # src = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        # src= cv2.resize(src, (640,400))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = IMG.fromarray(img)

        #to resize images;
        img= img.resize((400,400), IMG.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)


        # img= ImageTk.PhotoImage(file="lenna.jpg")
        # lblImg= Label(file= img)
        lblImg.configure(image=imgtk)
        lblImg.image = imgtk
        # lblImg.config(image=img)
        # lblImg.pack()






    def funcCameraOff(self):
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = IMG.fromarray(img)

        #to resize images;
        img= img.resize((400,400), IMG.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)

        # img= ImageTk.PhotoImage(file="lenna.jpg")
        # lblImg= Label(file= img)


        lblImg.configure(image=imgtk)
        lblImg.image = imgtk










    def __main__(self):
        global lbl, lblTwo
        # global frame1
        global lblImg
        global lblImg2
        global src




        ################################################################################################################
        # to make MENU
        ################################################################################################################

        menubr = Menu(root)

        fileMenu = Menu(menubr, tearoff=0)
        menubr.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='New')
        fileMenu.add_command(label='save')
        fileMenu.add_separator()
        fileMenu.add_command(label='exit')


        editMenu = Menu(menubr, tearoff=0)
        menubr.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Copy')
        editMenu.add_command(label='Delete')
        editMenu.add_separator()
        editMenu.add_command(label='Cut')



        # to register menubar to root window;
        root.config(menu=menubr)







        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # IMAGE DATA: FRAME-ONE
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////




        # to make notebook;
        ntbook = ttk.Notebook(root, width=1300, height=1000, padding=15)
        ntbook.pack()

        frame_1stTab = Frame(root)
        ntbook.add(frame_1stTab, text="IMAGE DATA")





        ################################################################################################################
        # top frame
        ################################################################################################################
        topFrame= Frame(frame_1stTab)
        topFrame.pack(side=TOP, fill=BOTH, expand=True)

        ##to make labels;
        lblHi = Label(topFrame, text='WKIT AI CLUSTERING')
        lblHi.config(font=('Courier', 13, 'bold'))
        lblHi.pack()
        #lblHi.grid(row=0, column=2, rowspan=2)







        ################################################################################################################
        # main frame
        ################################################################################################################
        mainFrame= Frame(frame_1stTab, padx=10, pady=10, bd=2, relief=RIDGE)
        mainFrame.pack(side=TOP, fill=BOTH, expand=True)
        #leftFrame.pack_propagate(0)








        ################################################################################################################
        # main-left frame
        ################################################################################################################
        mainLeftFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE)
        mainLeftFrame.pack(side=LEFT, fill=BOTH, expand=True)






        #---------------------------------------------------------------------------------------------------------------
        # main-left_top frame
        #------------------------------------------------------------------------------------------------------------------
        mainLeft_TopFrame= Frame(mainLeftFrame, width=50)
        #mainLeft_TopFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainLeft_TopFrame.pack(side=TOP)



        ##to make a button;
        btnPlus = Button(mainLeft_TopFrame, width=20, text='PLUS', command=self.funcPlus)
        btnPlus.pack()
        #btnPlus.grid(row=0, column=0, pady=3)


        ##to make a label;
        lbl = Label(mainLeft_TopFrame, text='DATA')
        lbl.pack()
        #lbl.grid(row=0, column=1)














        # ---------------------------------------------------------------------------------------------------------------
        # main-left_middle frame
        # ---------------------------------------------------------------------------------------------------------------
        mainLeft_MiddleFrame= Frame(mainLeftFrame)
        #mainLeftMiddleFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainLeft_MiddleFrame.pack(side=TOP)


        btnMinus = Button(mainLeft_MiddleFrame, width=20, text='MINUS', command=self.funcMinus)
        btnMinus.pack()
        #btnMinus.grid(row=1, column=0, pady=3)


        ##to make a label;
        lblTwo = Label(mainLeft_MiddleFrame, text='HELLO, CHARLIE')
        lblTwo.pack()
        #lblTwo.grid(row=1, column=1)





        # ---------------------------------------------------------------------------------------------------------------
        # mainLEFT_BOTTOM frame
        # ---------------------------------------------------------------------------------------------------------------
        mainLeft_BottomFrame= Frame(mainLeftFrame)
        mainLeft_BottomFrame.pack(side=BOTTOM)








        btnCamera = Button(mainLeft_BottomFrame, width=20, text='FILTER ON', command=self.funcCamera)
        btnCamera.pack()
        #btnCamera.grid(row=2, column=0, pady=3)


        btnCameraOff = Button(mainLeft_BottomFrame, width=20, text='FILTER OFF', command=self.funcCameraOff)
        btnCameraOff.pack()
        #btnCameraOff.grid(row=2, column=1, pady=3)










        ################################################################################################################
        # main-middle frame
        ################################################################################################################

        mainMiddleFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE)
        mainMiddleFrame.pack(side=LEFT, fill=BOTH, expand=True)
        #leftFrame.pack_propagate(0)





        # ---------------------------------------------------------------------------------------------------------------
        # main middle_TOP: frame
        # ---------------------------------------------------------------------------------------------------------------
        mainMiddle_TopFrame= Frame(mainMiddleFrame, padx=10, pady=10, bd=2, relief=RIDGE)
        #mainMiddleTopFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainMiddle_TopFrame.pack(side=TOP)



        #---------------------------------------
        # to make images;
        #---------------------------------------
        fname = 'lenna.png'
        src = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
        # src= cv2.imread(fname, cv2.IMREAD_GRAYSCALE)


        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = IMG.fromarray(img)
        #to resize images;
        img= img.resize((400,400), IMG.ANTIALIAS)
        imgcv = ImageTk.PhotoImage(image=img)




        # print(img_gray.ndim, img_gray.shape, img_gray.dtype)
        # cv2.imwrite('lenna_gray.png', img_gray)
        # img= ImageTk.PhotoImage(file="lenna.jpg")
        # img= ImageTk.PhotoImage(file="lenna.png")


        lblImg = Label(mainMiddle_TopFrame, image=imgcv)
        lblImg.configure(image=imgcv)
        lblImg.image = imgcv
        lblImg.pack(side=LEFT)
        #lblImg.grid(row=1, column=1, padx=10, pady=10)








        # ---------------------------------------------------------------------------------------------------------------
        # MAIN MIDDLE_BOTTOM: frame
        # ---------------------------------------------------------------------------------------------------------------
        mainMiddle_BottomFrame= Frame(mainMiddleFrame,padx=10, pady=10, bd=2, relief=RIDGE)
        #mainMiddleBottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
        mainMiddle_BottomFrame.pack(side=BOTTOM)







        #
        # btnCamera = Button(mainMiddleLeftFrame, width=20, text='FILTER ON', command=self.funcCamera)
        # btnCamera.pack(side=TOP, padx=5, pady=5)
        # #btnCamera.grid(row=2, column=0, pady=3)






        ### 2nd image;
        lblImg2 = Label(mainMiddle_BottomFrame, image=imgcv)
        lblImg2.configure(image=imgcv)
        lblImg2.image = imgcv
        #lblImg2.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=20)
        lblImg2.pack(side=LEFT)









        #---------------------------------------
        #to make figures;
        #---------------------------------------
        x = np.arange(1, 10, 1)
        y = 2 * (x - 5) ** 2

        fig = plt.Figure()
        # fig= plt.Figure(figsize=(5,4), dpi=100)
        fig.add_subplot(111).bar(x, y)
        # fig.add_subplot(111).plot(x,y)


        canvas = FigureCanvasTkAgg(fig, master=mainMiddle_TopFrame)
        #canvas.draw()
        #canvas.get_tk_widget().grid(row=0, column=0, padx=15)
        # canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)

        canvas.get_tk_widget().config(width=400, height=400)
        canvas.get_tk_widget().pack(side=LEFT)
        #line2.get_tk_widget().pack(side=LEFT, fill=BOTH)






        # btnCameraOff = Button(mainMiddleRightFrame, width=20, text='FILTER OFF', command=self.funcCameraOff)
        # btnCameraOff.pack(side=TOP, padx=5, pady=5)







        canvas = FigureCanvasTkAgg(fig, master=mainMiddle_BottomFrame)
        #canvas.draw()
        #canvas.get_tk_widget().grid(row=1, column=1, padx=15)

        # canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)
        canvas.get_tk_widget().config(width=400, height=400)
        # line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
        canvas.get_tk_widget().pack(side=LEFT)
















        ################################################################################################################
        # main-right frame
        ################################################################################################################
        mainRightFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE)
        mainRightFrame.pack(side=RIGHT, fill=BOTH, expand=True)
        #leftFrame.pack_propagate(0)





        # ---------------------------------------------------------------------------------------------------------------
        # main-right-top frame
        # ---------------------------------------------------------------------------------------------------------------
        mainRight_TopFrame= Frame(mainRightFrame)
        mainRight_TopFrame.pack(side=TOP)

        lblHi = Label(mainRight_TopFrame, text='graph position :')
        # lblHi.grid(row=1, column=2)
        lblHi.grid(row=0, column=0)



        #---------------------------------------
        #to make communications;
        #---------------------------------------


        ###to make radioboxes;
        btnSock = Button(mainRight_TopFrame, width=20, text='SOCKET COMM', command=self.funcCamera)
        #btnCamera.pack()
        btnSock.grid(row=0, column=1, columnspan=2, pady=3)




        lblHi = Label(mainRight_TopFrame, text='IP :')
        lblHi.grid(row=1, column=0)


        etrSock= Entry(mainRight_TopFrame, width=20)
        etrSock.grid(row=1, column=1)

        lblHi = Label(mainRight_TopFrame, text='PORT :')
        lblHi.grid(row=2, column=0)


        etrSock= Entry(mainRight_TopFrame, width=20)
        etrSock.grid(row=2, column=1)




        ###to update radar data receivedd from socket communication;
        #self.radSock()








        #####################################
        # main-right-bottom frame
        #####################################
        mainRightBottomFrame= Frame(mainRightFrame)
        mainRightBottomFrame.pack(side=BOTTOM)















        ################################################################################################################
        # bottom frame
        ################################################################################################################
        bottomFrame= Frame(frame_1stTab)
        bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        ##to make labels;
        lblHi = Label(bottomFrame, text='JCRADAR Ltd')
        lblHi.config(font=('Courier', 15, 'bold'))
        lblHi.pack(side=RIGHT)
        #lblHi.grid(row=0, column=2, rowspan=2)










        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # FRAME-TWO
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

        frame_2ndTab = Frame(root)
        ntbook.add(frame_2ndTab, text="VIDEO DATA")


        # to make label;
        lblTable = Label(frame_2ndTab, text='AIMONGO dB: tblTest')
        lblTable.config(font=('Courier', 11, 'bold'))
        lblTable.grid(row=0, column=0)


        lblTable = Label(frame_2ndTab, text='TEMPERATURE DATA')
        lblTable.config(font=('Courier', 11, 'bold'))
        lblTable.grid(row=0, column=1)


        lblTable = Label(frame_2ndTab, text='MOVING DATA')
        lblTable.config(font=('Courier', 12, 'bold'))
        lblTable.grid(row=0, column=2)











if __name__ == '__main__':
    root = Tk()
    #s = ttk.Style()
    #s.configure('TNotebook.Tab', font=('URW Gothic L', '11'))
    #s.configure('TNotebook.Tab', font=('URW Gothic L', '11', 'bold'))

    testHi= MyGui(root)

    while True:
        #for i in range(100):
        testHi.funcUpdate()
        time.sleep(0.05)


    #testHi.funcUpdate()

    root.mainloop()