from whatsapp_clone import *
from whatsapp_clone.ttk import *
import random
import time
import datetime
from whatsapp_clone import messagebox
import mysql.connector


class Hospital:
     def __init__(self,root):
         self.root=root
         self.root.title("Hospital Management System")
         self.root.geometry("1540x800+0+0")

         lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
         lbltitle.pack(side=TOP,fill=X)

         #==================Dataframe==================
         DataFrame=Frame(self.root,bd=20,relief=RIDGE)
         DataFrame.place(x=0,y=130,width=1530,height=400)

         DataFrame=FrameLeft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE
                                                               font=("aerial",12,"bold"),text="patient information"
         DataFrameLeft.place(x=0,y=5,width=980,height=350)

         DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,
                                   Front=("arial",12,"bold"),text="Prescription"
          DataFrameRight.place(x=990,y=5,width=460,height=350)

         # ======================ButtonsFrame=====================================


         Buttonframe=Frame(self.root,bd=20,relief=RIDGE,)
         Buttonframe.place(x=0,y=530,width=1530,height=70)

        # =======================DetailsFrame==================

         Detailsframe=Frame(self.root,bd=20,relief=RIDGE,)
         Detailsframe.place(x=0,y=600,width=1530,height=190)

        #=======================DataFrame======================

        lblNameTablet=label(DataframeLeft,text="Name OF Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.combobox(DataframeLeft,font=("times new roman",12,"bold")
                                                                           width=33)
        comNameTablet["values"]=("Nice","corona vaccine","Acetaminophen","Adderali","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=0,column=1,sticky=W)
        txtref.Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=2,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=0,column=2,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="No of tablets:",padx=2,pady=6)
        lblNooftablets.grid(row=2,column=0,sticky=W)
        txtNooftablets=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtNooftablets.grid(row=3,column=1)

        lblLot=Label(DataFrame,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrame,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=LabelFrameLeft,font=("arial",12,"bold"),text="Expe Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblsideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblsideEffect.grid(row=8,column=0,sticky=W)
        txtsideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtsideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodpressure=Label(DataFrameLeft,font=("arial",13,"bold"),width=35,text="Blood Pressure:",padx=2,pady=6)
        lblBloodpressure.grid(row=1,column=0,sticky=W)
        txtBloodpressure=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtBloodpressure.grid(row=1,column=1)

        lblstorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lblstorage.grid(row=2,column=0,sticky=W)
        txtstorage=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtstorage.grid(row=2,column=1)

        lblMedicine=Label(DataFrameLeft,font("arial",13,"bold"),text="Medicine:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=0,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=1)

        lblpatientId=LabelId=(DataFrameLeft,font("arial",13,bold),text="patientId:",padx=2,pady=6)
        lblpatientId.grid(row=4,column=0,sticky=W)
        txtpatientId=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtpatientId.grid(row=4,column=1)

        lblNhsNumber=Label(DataFrameLeft,font("arial"12,"bold"),text="Nhs Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,font("arial",13,"bold"),text="PatientName:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=0,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font="arial",width=35)
        txtPatientName.grid(row=6,column=1)

        lblDateOfBirth=Label(DataFrameLeft,font("arial"12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=0,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=1)

        lblPatientAdress=Label(DatFrameLeft,font("arial",13,"bold"),text="PatientAdress:",padx=2,pady=6)
        lblPatientAdress.grid(row=8,column=0,sticky=W)
        txtPatientAdress=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
        txtPatientAdress.grid(row=8,column=1)


       # ================DataframeRight============







root= Tk()
ob=Hospital(root)
root.mainloop()