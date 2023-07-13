from tkinter import *
import qrcode
def d():
    d =data.get()
    version=v.get
    f=file.get()
    qr = qrcode.QRCode(version ,box_size=10,border = 5)
    qr.add_data(d)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',back_color = 'white')
    img.save(r'C:\Users\DHAIRYA\Desktop\project\{f}.png') 
    
root=Tk()
root.title("QRCODE GENERATOR")
root.geometry('500x300')
Label(root,text='Data: ',font=("Arial", 20)).grid(row=0)
Label(root,text='Version: ',font=("Arial", 20)).grid(row=1)
Label(root,text='QR code file name: ',font=("Arial", 20)).grid(row=2)
data=StringVar()
v=IntVar()
file=StringVar()
Entry(root,textvariable=data,font=("Arial", 20)).grid(row=0,column=1)
Entry(root,textvariable=v,font=("Arial", 20)).grid(row=1,column=1)
Entry(root,textvariable=file,font=("Arial", 20)).grid(row=2,column=1)
Button(root,text='Generte',command=d).grid(row=5)

