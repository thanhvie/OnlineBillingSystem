from tkinter import *
import tkinter.messagebox
import random
import time
import datetime

root=Tk()
root.geometry("1350x650+0+0")
root.title("Billing Systems")

Tops=Frame(root,width=1350,height=100,bd=8,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=320,bd=8,relief="raise")
f2a.pack(side=BOTTOM)

f1aa=Frame(f1a,width=400,height=430,bd=8,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400,height=430,bd=8,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=330,bd=8,relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450,height=330,bd=8,relief="raise")
f2ab.pack(side=RIGHT)

lblInfo=Label(Tops,font=('arial',60,'bold'),text="            Online Billing System          ",
              bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

#====================Calculator====================#
text_Input = StringVar()
operator=""
PaymentRef=StringVar()
Carpets = StringVar()
Blinds = StringVar()
Fabric = StringVar()
HomeDelivery = StringVar()
DateOfOrder = StringVar()
CostOfCarpets = StringVar()
CostOfFabric = StringVar()
CostOfBlinds=StringVar()
CostOfDelivery=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()

Carpets.set(0)
Blinds.set(0)
Fabric.set(0)
HomeDelivery.set(0)
DateOfOrder.set(time.strftime("%d/%m/%Y"))

def CostOfOrder():
    CarpetPrice = float(Carpets.get())
    BlindsPrice = float(Blinds.get())
    FabricPrice = float(Fabric.get())
    DeliveryPrice = float(HomeDelivery.get())

    CarpetCost = '$'+ str('%.2f'%((CarpetPrice*10)))
    CostOfCarpets.set(CarpetCost)

    BlindsCost = '$' + str('%.2f' % ((BlindsPrice * 9)))
    CostOfBlinds.set(BlindsCost)

    FabricCost = '$' + str('%.2f' % ((FabricPrice * 8)))
    CostOfFabric.set(FabricCost)

    DeliveryCost = '$' + str('%.2f' % ((DeliveryPrice * 5)))
    CostOfDelivery.set(DeliveryCost)

    x = random.randint(10000000, 19999999)
    randomRef = str(x)
    PaymentRef.set("BILL" + randomRef)

    Cost = ((CarpetPrice*15.49)
                     + (BlindsPrice * 7.49)
                     + (FabricPrice * 5.50)
                     + (DeliveryPrice * 4.50))

    ToC = '$' + '%.2f'%(Cost)

    SubTotal.set(ToC)

    Tax = '$' + '%.2f'%(Cost * 0.05)
    PaidTax.set(Tax)

    ToP = '$' + '%.2f'%(Cost + Cost *0.05)
    TotalCost.set(ToP)

def iExit():
    qExit = tkinter.messagebox.askyesno("Billing system", "Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return
def iReset():
    PaymentRef.set("")
    Carpets.set(0)
    Blinds.set(0)
    Fabric.set(0)
    HomeDelivery.set(0)
    CostOfCarpets.set("")
    CostOfFabric.set("")
    CostOfBlinds.set("")
    CostOfDelivery.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    DateOfOrder.set(time.strftime("%d/%m/%Y"))

def PayReference():
    x = random.randint(10000000, 19999999)
    randomRef = str(x)
    PaymentRef.set("BILL" + randomRef)

#definition for button calculator
def btnClick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""




txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=40,insertwidth=6
                 ,justify=RIGHT)
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='7',
            command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='8',
            command=lambda: btnClick(8)).grid(row=1,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='9',
            command=lambda: btnClick(9)).grid(row=1,column=2)
btnPlus=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='+',
               command=lambda: btnClick('+')).grid(row=1,column=3)
#-------------------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='4',
            command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='5',
            command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='6',
            command=lambda: btnClick(6)).grid(row=3,column=2)
btnSub=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='-',
              command=lambda: btnClick('-')).grid(row=3,column=3)
#--------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='1',
            command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='2',
            command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='3',
            command=lambda: btnClick(3)).grid(row=4,column=2)
btnMul=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='*',
              command=lambda: btnClick('*')).grid(row=4,column=3)
#--------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='0',
            command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='C',
                command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='=',
                 command=btnEqualsInput).grid(row=5,column=2)
btnDiv=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text='/',
              command=lambda: btnClick('/')).grid(row=5,column=3)
#--------------------------------------------Order Information f1aa-----------------------------------------------

lblRef=Label(f1aa,font=('arial',16,'bold'),text="Sales Reference",bd=16,justify=LEFT)
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa,font=('arial',16,'bold'),textvariable=PaymentRef,bd=10,justify=LEFT
             ,insertwidth=2)
txtRef.grid(row=0,column=1)

lblCarpets=Label(f1aa,font=('arial',16,'bold'),text="Carpets",bd=16,anchor='w')
lblCarpets.grid(row=1,column=0)
txtCarpets=Entry(f1aa,font=('arial',16,'bold'),textvariable=Carpets,bd=10,justify=LEFT
             ,insertwidth=2)
txtCarpets.grid(row=1,column=1)

lblFabric=Label(f1aa,font=('arial',16,'bold'),text="Fabric",bd=16,anchor='w')
lblFabric.grid(row=2,column=0)
txtFabric=Entry(f1aa,font=('arial',16,'bold'),textvariable=Fabric,bd=10,justify=LEFT
             ,insertwidth=2)
txtFabric.grid(row=2,column=1)

lblBlinds=Label(f1aa,font=('arial',16,'bold'),text="Blinds",bd=16,anchor='w')
lblBlinds.grid(row=3,column=0)
txtBlinds=Entry(f1aa,font=('arial',16,'bold'),textvariable=Blinds,bd=10,justify=LEFT
             ,insertwidth=2)
txtBlinds.grid(row=3,column=1)

lblHomeDelivery=Label(f1aa,font=('arial',16,'bold'),text="Home Delivery",bd=16,anchor='w')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1aa,font=('arial',16,'bold'),textvariable=HomeDelivery,bd=10,justify=LEFT
             ,insertwidth=2)
txtHomeDelivery.grid(row=4,column=1)

#---------------------------------Order Information f1ab---------------------------------#

lblDateOfOrder=Label(f1ab,font=('arial',16,'bold'),text="Order Date",bd=16,anchor='w')
lblDateOfOrder.grid(row=0,column=0)
txtDateOfOrder=Entry(f1ab,font=('arial',16,'bold'),textvariable=DateOfOrder,bd=10,justify=LEFT
             ,width=12)
txtDateOfOrder.grid(row=0,column=1)

lblCostOfCarpets=Label(f1ab,font=('arial',16,'bold'),text="Cost of Carpets",bd=16,anchor='w')
lblCostOfCarpets.grid(row=1,column=0)
txtCostOfCarpets=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostOfCarpets,bd=10,justify=LEFT
             ,width=12)
txtCostOfCarpets.grid(row=1,column=1)

lblCostOfFabric=Label(f1ab,font=('arial',16,'bold'),text="Cost of Fabric",bd=16,anchor='w')
lblCostOfFabric.grid(row=2,column=0)
txtCostOfFabric=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostOfFabric,bd=10,justify=LEFT
             ,width=12)
txtCostOfFabric.grid(row=2,column=1)

lblCostOfBlinds=Label(f1ab,font=('arial',16,'bold'),text="Cost of Blinds",bd=16,anchor='w')
lblCostOfBlinds.grid(row=3,column=0)
txtCostOfBlinds=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostOfBlinds,bd=10,justify=LEFT
             ,width=12)
txtCostOfBlinds.grid(row=3,column=1)

lblCostOfDelivery=Label(f1ab,font=('arial',16,'bold'),text="Cost of Delivery",bd=16,anchor='w')
lblCostOfDelivery.grid(row=4,column=0)
txtCostOfDelivery=Entry(f1ab,font=('arial',16,'bold'),textvariable=CostOfDelivery,bd=10,justify=LEFT
             ,width=12)
txtCostOfDelivery.grid(row=4,column=1)

#---------------------------------Order Information f2aa---------------------------------#
lblPaidTax=Label(f2aa,font=('arial',16,'bold'),text="Paid Tax",bd=8,anchor='w')
lblPaidTax.grid(row=2,column=0)
txtPaidTax=Entry(f2aa,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,justify=LEFT
             ,insertwidth=2)
txtPaidTax.grid(row=2,column=1)

lblSubTotal=Label(f2aa,font=('arial',16,'bold'),text="Sub Total",bd=8,anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal=Entry(f2aa,font=('arial',16,'bold'),textvariable=SubTotal,bd=8,justify=LEFT
             ,insertwidth=2)
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(f2aa,font=('arial',16,'bold'),text="Total Cost",bd=8,anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost=Entry(f2aa,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,justify=LEFT
             ,insertwidth=2)
txtTotalCost.grid(row=4,column=1)

#---------------------------------Order Information Buttons---------------------------------#
btnTotal=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=15,
                text="Total Cost",command = CostOfOrder).grid(row=0,column=0)

btnSaleRef=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=15,
                text="Sale Ref",command=PayReference).grid(row=0,column=1)

btnReset=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=15,
                text="Reset",command=iReset).grid(row=1,column=0)
btnExit=Button(f2ab,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=15,
                text="Exit",command=iExit).grid(row=1,column=1)
#-------------------------------------------------------------------------------------------#




root.mainloop()