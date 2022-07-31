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

from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames, askopenfile
from tkinter import messagebox
import os


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
        root.geometry("1400x1100+20+20")
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






    # to load image file;
    def funcImageOpen(self):
        self.count += 1
        lbl.config(text=str(self.count))
        #global countPlus
        global x

        print(countPlus)
        #countPlus= 111
        x= 1
        print(x)








        # to select files;

        try:

            filenames = askopenfilenames(initialdir="D:/___r_d/AI/GUI_MOTgo/image/", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))

            if filenames:
                for filename in filenames:
                    # to delete directory name;
                    filename = filename.split('/')
                    # print(filenames[-1])
                    lbxFile.insert(0, filename[-1])


        except:
            messagebox.showerror("Error","Error happens")





    def funclbxSelect(event):
        print('hello,kitty')




    def funcImageLoad(self):
        #global countPlus

        self.count -= 1
        lbl.config(text=str(self.count))

        count= 22222222
        print(count)

        countPlus= 222
        print(countPlus)


        xy= 11
        print(xy)



        imgLoaded = ImageTk.PhotoImage(file="image/dirac.jpg")
        # imgLoaded = imgLoaded.(800,800), IMG.ANTIALIAS)
        lblOriginImg.configure(image=imgLoaded)
        lblOriginImg.image = imgLoaded






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
        global lblOriginImg
        global lbxFile

        global src




        # to let listbox show its images;
        def funclbxSelect(event):
            print('hello,kitty')





            imgLstbox = lbxFile.get(lbxFile.curselection())
            print(imgLstbox)




            # currentPath = os.getcwd()
            # imgPath = currentPath + "\image"
            # print(imgPath)


            currentPath = os.getcwd()
            imgPath = "./image/"
            print(imgPath)

            # loadingFile = os.path.join(imgPath, imgLstbox)
            # print(loadingFile)
            loadingFile = imgPath + imgLstbox
            print(loadingFile)

            # imgLoaded = ImageTk.PhotoImage(file="image/dirac.jpg")
            imgLoaded = ImageTk.PhotoImage(file=loadingFile)
            # imgLoaded = imgLoaded((800,800), IMG.ANTIALIAS)
            lblOriginImg.configure(image=imgLoaded)
            lblOriginImg.image = imgLoaded






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








        ##to make labels;
        lblHi = Label(root, padx= 50, text='WKIT-AI-CLUSTERING')
        lblHi.config(font=('Courier', 18, 'bold'))
        lblHi.pack(side=TOP)




        # ### to make images;
        # img= ImageTk.PhotoImage(file="image/wk-logo.JPG")
        # #img= ImageTk.PhotoImage(file="lenna.png")
        # lblLogo= Label(topFrame, image= img)
        # lblLogo.image= img
        # # lblLogo.pack(side=RIGHT)
        # lblLogo.grid(row=0, column=3)



        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # IMAGE DATA: FRAME-ONE
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////


        # to make notebook;
        # ntbook = ttk.Notebook(root, width=1300, height=1000, padding=15)
        ntbook = ttk.Notebook(root)
        ntbook.pack(padx=10)

        # frame_1stTab = Frame(root)
        frame_1stTab = Frame(ntbook)
        ntbook.add(frame_1stTab, text="IMAGE DATA")


















        ################################################################################################################
        # top frame
        ################################################################################################################
        # topFrame= Frame(frame_1stTab, bg='skyblue3')
        topFrame= Frame(frame_1stTab, bg='skyblue3')
        # topFrame.pack(side=TOP, fill=BOTH, expand=True)
        topFrame.pack(side=TOP, fill=BOTH)







        # ##to make file open;
        iconOpen = ImageTk.PhotoImage(file="icon/folder-open-line.png")
        btnOpen = Button(topFrame, image=iconOpen, command=self.funcImageOpen)
        btnOpen.image = iconOpen
        btnOpen.grid(row=0, column=0, pady=10, padx=10)



        # ##to make file delete;
        iconDelete = ImageTk.PhotoImage(file="icon/delete-bin-line.png")
        btnDelete = Button(topFrame, image=iconDelete, command=self.funcImageOpen)
        btnDelete.image = iconDelete
        btnDelete.grid(row=0, column=1, pady=10, padx=10)



        # to make play button;
        # iconPlay = ImageTk.PhotoImage(file="icon/folder-open-line.png")
        iconPlay = PhotoImage(file="icon/play-line.png")
        lblPlay = Label(topFrame, image=iconPlay)
        lblPlay.image = iconPlay
        lblPlay.grid(row=0, column=2, pady=10, padx=10)





















        ##to make forward button;
        iconForward = PhotoImage(file="./icon/speed-line.png")
        # lblMail = Label(topFrame, image=iconMail, text="mail image")
        lblForward = Label(topFrame, image=iconForward)
        lblForward.image = iconForward
        lblForward.grid(row=0, column=3, pady=10, padx=10)


        ##to make backward button;
        iconBackward = PhotoImage(file="./icon/rewind-line.png")
        lblBackward = Label(topFrame, image=iconBackward)
        lblBackward.image = iconBackward
        lblBackward.grid(row=0, column=4, pady=10, padx=10)


        ##to make labels;
        iconSave = PhotoImage(file="./icon/save-3-line.png")
        lblSave = Label(topFrame, image=iconSave)
        lblSave.image = iconSave
        lblSave.grid(row=0, column=5, pady=10, padx=10)



















        ################################################################################################################
        # main frame
        ################################################################################################################
        mainFrame= Frame(frame_1stTab, padx=10, pady=10, bd=2, relief=RIDGE)
        # mainFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainFrame.pack(side=TOP)
        #leftFrame.pack_propagate(0)








        ################################################################################################################
        # main-left frame
        ################################################################################################################
        mainLeftFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE)
        mainLeftFrame.pack(side=LEFT, fill=BOTH, expand=True)
        # mainLeftFrame.pack(side=LEFT)





        #---------------------------------------------------------------------------------------------------------------
        # main-left_top frame
        #------------------------------------------------------------------------------------------------------------------
        mainLeft_TopFrame= Frame(mainLeftFrame, width=50)
        # mainLeft_TopFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainLeft_TopFrame.pack(side=TOP)



        ##to make a button;
        btnPlus = Button(mainLeft_TopFrame, text='Image OPEN', command=self.funcImageOpen)
        btnPlus.pack()
        #btnPlus.grid(row=0, column=0, pady=3)


        # to make file list
        lbxFile = Listbox(mainLeft_TopFrame, height=40)
        lbxFile.bind('<Double-1>', funclbxSelect)
        lbxFile.pack()

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


        btnImgLoad = Button(mainLeft_MiddleFrame, width=20, text='Image LOAD', command=self.funcImageLoad)
        btnImgLoad.pack()
        #btnMinus.grid(row=1, column=0, pady=3)


        ##to make a label;
        lblTwo = Label(mainLeft_MiddleFrame, text='HELLO, CHARLIE')
        lblTwo.pack()
        #lblTwo.grid(row=1, column=1)





        # ---------------------------------------------------------------------------------------------------------------
        # mainLEFT_BOTTOM frame
        # ---------------------------------------------------------------------------------------------------------------
        mainLeft_BottomFrame= Frame(mainLeftFrame)
        mainLeft_BottomFrame.pack(side=TOP)




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





        # ---------------------------------------------------------------------------------------------------------------
        # MAIN MIDDLE_BOTTOM: frame
        # ---------------------------------------------------------------------------------------------------------------
        mainMiddle_BottomFrame= Frame(mainMiddleFrame,padx=10, pady=10, bd=2, relief=RIDGE)
        #mainMiddleBottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
        mainMiddle_BottomFrame.pack(side=BOTTOM)





        # #---------------------------------------
        # # to make images;
        # #---------------------------------------
        # fname = 'image/ai-concept.jpg'
        # fname = 'image/deep-learning.jpg'
        fname = 'image/ai2.jpg'


        src = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
        # src= cv2.imread(fname, cv2.IMREAD_GRAYSCALE)


        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = IMG.fromarray(img)
        # to resize images;
        img= img.resize((800,800), IMG.ANTIALIAS)
        imgcv = ImageTk.PhotoImage(image=img)



        ### 2nd image;
        lblOriginImg = Label(mainMiddle_BottomFrame, image=imgcv)
        # lblImg2.configure(image=imgcv)
        lblOriginImg.image = imgcv
        #lblImg2.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=20)
        lblOriginImg.pack(side=LEFT)









        #---------------------------------------
        #to make figures;
        #---------------------------------------
        x = np.arange(1, 10, 1)
        y = 2 * (x - 5) ** 2

        fig = plt.Figure()
        # fig= plt.Figure(figsize=(5,4), dpi=100)
        fig.add_subplot(111).bar(x, y)
        # fig.add_subplot(111).plot(x,y)











        # canvas = FigureCanvasTkAgg(fig, master=mainMiddle_BottomFrame)
        # #canvas.draw()
        # #canvas.get_tk_widget().grid(row=1, column=1, padx=15)
        #
        # # canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)
        # canvas.get_tk_widget().config(width=400, height=400)
        # # line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
        # canvas.get_tk_widget().pack(side=LEFT)
















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
        # bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
        bottomFrame.pack(side=TOP)


        # ##to make labels;
        # lblHi = Label(bottomFrame, text='JCRADAR Ltd')
        # lblHi.config(font=('Courier', 15, 'bold'))
        # lblHi.pack(side=RIGHT)
        # #lblHi.grid(row=0, column=2, rowspan=2)


        ### to make images;
        img= ImageTk.PhotoImage(file="image/wk-logo.JPG")
        #img= ImageTk.PhotoImage(file="lenna.png")
        lblLogo= Label(bottomFrame, image= img)
        lblLogo.image= img
        lblLogo.pack(side=TOP)
        # lblLogo.grid(row=0, column=3)






        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # FRAME-TWO
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////

        frame_2ndTab = Frame(ntbook)
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