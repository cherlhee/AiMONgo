# guiMOTgo_frame_ver3-1.py - to connect automatically the right entry;to make AI-function to recognize person;
# guiMOTgo_frame_3rd.py - to make AI-function to recognize person;

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

from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames, askopenfile, asksaveasfilename
from tkinter import messagebox
import os
from tkinter import scrolledtext

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
        root.geometry("1920x1080+20+20")
        root.resizable(True, True)
        # root.resizable(False, False)


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
            # filenames = askopenfilenames(initialdir="D:/___r_d/AI/GUI_MOTgo/image/", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
            # filenames = askopenfilenames(initialdir="D:/__AI/GUI_MOTgo/image/", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
            filenames = askopenfilenames(initialdir="D:/__AI/GUI_MOTgo/image/", filetypes=(("jpg", "*.jpg"),("jpeg","*.jpeg"),("png", "*.png"), ("all files", "*.*")))
            if filenames:
                for filename in filenames:
                    # to delete directory name;
                    filename = filename.split('/')
                    # print(filenames[-1])
                    lbxFile.insert(0, filename[-1])
        except:
            messagebox.showerror("Error","Error happens")





    def funcListboxDelete(self):
        print('hello,kitty')

        imgLstbox = lbxFile.get(lbxFile.curselection())
        print(imgLstbox)

        # to delete all items
        # lbxFile.delete(0, 'end')
        # to delete from 0 to anchor
        # lbxFile.delete(0, ANCHOR)
        # to delete from anchor to anchor
        lbxFile.delete(ANCHOR, ANCHOR)


    def funcSaveAs(self):
        print('hello,saveas')

        filename = asksaveasfilename(initialdir="/", title="Select file",
                                                filetypes=(("text files", "*.txt"),
                                                           ("all files", "*.*")))

        # with open(filename,'w',encoding='utf-8') as f:
        #     #to test initially;
        #     #f.write('hello, kitty')
        #     #to save the edit result by users;
        #     ptrSeekError= self.txtSeekError.get('1.0', END)
        #     f.write(ptrSeekError)









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







        # to load values to widgets;
        # lblRightframe_countPeople.config(text=str(self.count))
        # etrRightframe_countPeople.config(text=str(self.count))

        etrRightframe_countPeople.delete(0, END)
        etrRightframe_countPeople.insert(END, str(self.count))






    def seekPeopleYolo3(self):
        print('hello, yolov3')

        # to load Yolo;
        net = cv2.dnn.readNet("yolov3/yolov3.weights", "yolov3/yolov3.cfg")

        classes = []
        with open("yolov3/coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()

        # have to modify the format of layer_names;hard to understand the errors;
        # output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

        colors = np.random.uniform(0, 255, size=(len(classes), 3))






        FNAME = loadingFile
        print(FNAME)
        print(type(loadingFile))

        img = cv2.imread(FNAME, cv2.IMREAD_UNCHANGED)
        # cv2.imshow('jcr', imgcv2)
        # cv2.waitKey(0)





        # img = cv2.resize(img, None, fx=0.4, fy=0.4)
        img = cv2.resize(img, None, fx=1, fy=1)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)

        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

        # cv2.imshow("Image", img)


        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = IMG.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        lblOriginImg.config(image=imgtk)
        lblOriginImg.image=imgtk









    def __main__(self):
        global lbl, lblTwo
        # global frame1
        global lblImg
        global lblImg2
        global lblOriginImg
        global lbxFile

        global src

        # to make rightframe widgets to global variables;
        global lblRightframe_countPeople
        global etrRightframe_countPeople



        # to let listbox show its images;
        def funclbxSelect(event):

            global loadingFile


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





            # to know whether loadingFile is cv2 image;
            # imgcv2 = np.array(imgLoaded)
            # imgcv2 = cv2.cvtColor(imgcv2, cv2.COLOR_RGB2BGR)


            # FNAME = loadingFile
            # imgcv2 = cv2.imread(FNAME, cv2.IMREAD_UNCHANGED)
            # cv2.imshow('jcr', imgcv2)
            # cv2.waitKey(0)








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

        frame_1stTab = Frame(root, width=1920, height=1080)
        frame_1stTab.pack()
        frame_1stTab.pack_propagate(False)


        # frame_1stTab = Frame(ntbook)
        ntbook.add(frame_1stTab, text="IMAGE DATA")

















        ################################################################################################################
        ################################################################################################################
        # top frame
        ################################################################################################################
        ################################################################################################################

        # topFrame= Frame(frame_1stTab, bg='skyblue3')
        topFrame= Frame(frame_1stTab, bg='skyblue3')
        # topFrame.pack(side=TOP, fill=BOTH, expand=True)
        topFrame.pack(side=TOP, fill=BOTH)
        # topFrame.pack_propagate(False)






        # ##to make file open;
        iconOpen = ImageTk.PhotoImage(file="./icon/folder-open-line.png")
        btnOpen = Button(topFrame, image=iconOpen, command=self.funcImageOpen)
        btnOpen.image = iconOpen
        btnOpen.grid(row=0, column=0, pady=10, padx=10)





        # ##to make file delete;
        iconDelete = ImageTk.PhotoImage(file="icon/delete-bin-line.png")
        btnDelete = Button(topFrame, image=iconDelete, command=self.funcListboxDelete)
        btnDelete.image = iconDelete
        btnDelete.grid(row=0, column=1, pady=10, padx=10)



        # to make play button;
        iconPlay = ImageTk.PhotoImage(file="icon/play-line.png")
        btnPlay = Button(topFrame, image=iconPlay, command=self.seekPeopleYolo3)
        btnPlay.image = iconPlay
        btnPlay.grid(row=0, column=2, pady=10, padx=10)

















        ##to make forward button;
        iconForward = PhotoImage(file="./icon/speed-line.png")
        # lblMail = Label(topFrame, image=iconMail, text="mail image")
        lblForward = Label(topFrame, image=iconForward)
        lblForward.image = iconForward
        lblForward.grid(row=0, column=5, pady=10, padx=10)


        ##to make backward button;
        iconBackward = PhotoImage(file="./icon/rewind-line.png")
        lblBackward = Label(topFrame, image=iconBackward)
        lblBackward.image = iconBackward
        lblBackward.grid(row=0, column=6, pady=10, padx=10)


        ##to make labels;
        iconSave = PhotoImage(file="./icon/save-3-line.png")
        lblSave = Label(topFrame, image=iconSave)
        lblSave.image = iconSave
        lblSave.grid(row=0, column=7, pady=10, padx=10)


















        ################################################################################################################
        ################################################################################################################
        # main frame
        ################################################################################################################
        ################################################################################################################

        mainFrame= Frame(frame_1stTab, padx=10, pady=10, bd=2, relief=RIDGE, width=1920, height=800)
        # mainFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainFrame.pack(side=TOP)
        mainFrame.pack_propagate(False)








        ################################################################################################################
        # main-left frame
        ################################################################################################################
        mainLeftFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE, width=200, height=800)
        mainLeftFrame.pack(side=LEFT)
        # mainLeftFrame.pack(side=LEFT)
        mainLeftFrame.pack_propagate(False)





        #---------------------------------------------------------------------------------------------------------------
        # main-left_top frame
        #------------------------------------------------------------------------------------------------------------------
        mainLeft_TopFrame= Frame(mainLeftFrame)
        # mainLeft_TopFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainLeft_TopFrame.pack(side=TOP)



        ##to make a button;
        btnPlus = Button(mainLeft_TopFrame, text='Image OPEN', command=self.funcImageOpen)
        btnPlus.pack()
        #btnPlus.grid(row=0, column=0, pady=3)


        # to make file list
        sbar = Scrollbar(mainLeft_TopFrame)
        sbar.pack(side='right', fill='y')


        lbxFile = Listbox(mainLeft_TopFrame, selectmode='extended', yscrollcommand=sbar.set, height=30)
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




        # btnCamera = Button(mainLeft_BottomFrame, width=20, text='FILTER ON', command=self.funcCamera)
        # btnCamera.pack()
        # #btnCamera.grid(row=2, column=0, pady=3)
        #
        #
        # btnCameraOff = Button(mainLeft_BottomFrame, width=20, text='FILTER OFF', command=self.funcCameraOff)
        # btnCameraOff.pack()
        # #btnCameraOff.grid(row=2, column=1, pady=3)
        #
        #
        #
        #









        ################################################################################################################
        # main-middle frame
        ################################################################################################################

        mainMiddleFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE, width=1000, height=800)
        mainMiddleFrame.pack(side=LEFT, fill=BOTH, expand=True)
        mainLeftFrame.pack_propagate(False)





        # ---------------------------------------------------------------------------------------------------------------
        # main middle_TOP: frame
        # ---------------------------------------------------------------------------------------------------------------
        mainMiddle_TopFrame= Frame(mainMiddleFrame, padx=10, pady=10, bd=2, relief=RIDGE)
        #mainMiddleTopFrame.pack(side=TOP, fill=BOTH, expand=True)
        mainMiddle_TopFrame.pack(side=TOP)





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
        lblOriginImg = Label(mainMiddle_TopFrame, image=imgcv)
        # lblImg2.configure(image=imgcv)
        lblOriginImg.image = imgcv
        #lblImg2.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=20)
        lblOriginImg.pack(side=TOP)









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



        # ---------------------------------------------------------------------------------------------------------------
        # MAIN MIDDLE_BOTTOM: frame
        # ---------------------------------------------------------------------------------------------------------------
        mainMiddle_BottomFrame= Frame(mainMiddleFrame,padx=10, pady=10, bd=2, relief=RIDGE)
        #mainMiddleBottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
        mainMiddle_BottomFrame.pack(side=BOTTOM)












        ################################################################################################################
        # main-right frame
        ################################################################################################################
        mainRightFrame= Frame(mainFrame, padx=10, pady=10, bd=2, relief=RIDGE, width=200, height=800)
        mainRightFrame.pack(side=LEFT)
        mainRightFrame.pack_propagate(False)





        # ---------------------------------------------------------------------------------------------------------------
        # main-right-top frame
        # ---------------------------------------------------------------------------------------------------------------

        mainRight_TopFrame= Frame(mainRightFrame)
        mainRight_TopFrame.pack(side=TOP)






        lblRightframe_countPeople = Label(mainRight_TopFrame, text='PEOPLE COUNT :')
        lblRightframe_countPeople.pack()


        etrRightframe_countPeople= Entry(mainRight_TopFrame, width=20)
        etrRightframe_countPeople.pack()

        lblHi = Label(mainRight_TopFrame, text='GROUP COUNT :')
        lblHi.pack()


        etrSock= Entry(mainRight_TopFrame, width=20)
        etrSock.pack()




        lblHi = Label(mainRight_TopFrame, text='GROUP DIRECTION :')
        # lblHi.grid(row=1, column=2)
        lblHi.pack()

        etrSock= Entry(mainRight_TopFrame, width=20)
        etrSock.pack()



        lblHi = Label(mainRight_TopFrame, text='GROUP VELOCITY :')
        # lblHi.grid(row=1, column=2)
        lblHi.pack()

        etrSock= Entry(mainRight_TopFrame, width=20)
        etrSock.pack()


        lblHi = Label(mainRight_TopFrame, text='ANOTATED CONTENTS')
        # lblHi.grid(row=1, column=2)
        lblHi.pack(pady=10)


        # textTranslate = scrolledtext.ScrolledText(mainRight_TopFrame)
        # textTranslate.grid(row=9, column=0)
        self.text= scrolledtext.ScrolledText(mainRight_TopFrame)
        self.text.pack()


        #to make communications;
        ###to make radioboxes;
        btnSock = Button(mainRight_TopFrame, width=20, text='SAVE AS', command=self.funcSaveAs)
        #btnCamera.pack()
        btnSock.pack(pady=10)



        # ---------------------------------------------------------------------------------------------------------------
        # main-right-bottom frame
        # ---------------------------------------------------------------------------------------------------------------

        mainRightBottomFrame= Frame(mainRightFrame)
        mainRightBottomFrame.pack(side=BOTTOM)














        ################################################################################################################
        ################################################################################################################
        # bottom frame
        ################################################################################################################
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