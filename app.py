import tkinter as tk
from tkinter import CENTER, Button, Frame, Label, filedialog
from PIL import Image
import os



# watermark = Image.open("Watermark.png")

def openFile():
    global watermarkPath
    watermarkPath = filedialog.askopenfilename()
    window.destroy()


window=tk.Tk()
window.title('Chose file Path')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width=300
height=150

lbl1=Label(window, text="Select your watermark", fg='#000000', font=("montserrat", 10))
lbl1.pack(anchor=CENTER, pady=(15, 0))
button = Button(text="Open",command=openFile, height= 2, width=10, background='#2196f3', foreground='WHITE', border=0, cursor='hand2', font=("montserrat bold", 10))
button.pack(anchor=CENTER, pady=(5, 0))

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window.mainloop()









watermark = Image.open(watermarkPath)
watermarkHeight, watermarkWidth = watermark.size

watermarkPosition = 5
def setWatermarkPositon(val):
    global watermarkPosition
    watermarkPosition = val
    window.destroy()


window = tk.Tk()
window.resizable(False, False)
window.title('Get Position')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 313
height = 268
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
root = Frame(window, relief = 'sunken',bd = 1, bg = 'white')
root.pack(fill = 'both', expand = True, padx = 10, pady = 10)


button1 = Button(root, text='Top Left', height= 5, width=13, command= lambda: setWatermarkPositon(1), background='#2196f3', foreground='WHITE', border=0, cursor='hand2')
button1.grid(row=0, column=0)
button2 = Button(root, text='Top Middle', height= 5, width=13, command= lambda: setWatermarkPositon(2), background='#00bcd4', foreground='WHITE', border=0, cursor='hand2')
button2.grid(row=0, column=1)
button3 = Button(root, text='Top Right', height= 5, width=13, command= lambda: setWatermarkPositon(3), background='#2196f3', foreground='WHITE', border=0, cursor='hand2')
button3.grid(row=0, column=2)
button4 = Button(root, text='Middle Left', height= 5, width=13, command= lambda: setWatermarkPositon(4), background='#00bcd4', foreground='WHITE', border=0, cursor='hand2')
button4.grid(row=1, column=0)
button5 = Button(root, text='Middle', height= 5, width=13, command= lambda: setWatermarkPositon(5), background='#2196f3', foreground='WHITE', border=0, cursor='hand2')
button5.grid(row=1, column=1)
button6 = Button(root, text='Middle Right', height= 5, width=13, command= lambda: setWatermarkPositon(6), background='#00bcd4', foreground='WHITE', border=0, cursor='hand2')
button6.grid(row=1, column=2)
button7 = Button(root, text='Bottom Left', height= 5, width=13, command= lambda: setWatermarkPositon(7), background='#2196f3', foreground='WHITE', border=0, cursor='hand2')
button7.grid(row=2, column=0)
button8 = Button(root, text='Bottom Middle', height= 5, width=13, command= lambda: setWatermarkPositon(8), background='#00bcd4', foreground='WHITE', border=0, cursor='hand2')
button8.grid(row=2, column=1)
button9 = Button(root, text='Bottom Right', height= 5, width=13, command= lambda: setWatermarkPositon(9), background='#2196f3', foreground='WHITE', border=0, cursor='hand2')
button9.grid(row=2, column=2)

root.mainloop()








def askImageDerectory():
    global imageDirectory
    imageDirectory = filedialog.askdirectory()
    window.destroy()


window=tk.Tk()
window.title('Apply waremark')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width=300
height=150

lbl1=Label(window, text="Select Image folder", fg='#000000', font=("montserrat bold", 12))
lbl1.pack(anchor=CENTER, pady=(15, 0))

button = Button( window, background='#21b3e1', foreground='WHITE', highlightthickness=2, highlightcolor='WHITE', width=10, border=0, cursor='hand2', text='Select', font=('montserrat', 10, 'bold'), command=askImageDerectory )
button.pack(anchor=CENTER, pady=(10, 0))

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window.mainloop()








def addWatermark(img):

    imagetoEdit = img

    aspratio = watermark.height/watermark.width
    newWidth = int(imagetoEdit.width/4)
    newHeight = int(newWidth*aspratio)

    newWatermark = watermark.resize((newWidth, newHeight))

    if watermarkPosition==1:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/6)-(newWatermark.width/2)), int((imagetoEdit.height/6)-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==2:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/2)-(newWatermark.width/2)), int((imagetoEdit.height/6)-(newWatermark.height/2))), newWatermark)
        
    elif watermarkPosition==3:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/6)*5-(newWatermark.width/2)), int((imagetoEdit.height/6)-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==4:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/6)-(newWatermark.width/2)), int((imagetoEdit.height/2)-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==5:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/2)-(newWatermark.width/2)), int((imagetoEdit.height/2)-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==6:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/6)*5-(newWatermark.width/2)), int((imagetoEdit.height/2)-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==7:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/6)-(newWatermark.width/2)), int((imagetoEdit.height/6)*5-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==8:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/2)-(newWatermark.width/2)), int((imagetoEdit.height/6)*5-(newWatermark.height/2))), newWatermark)

    elif watermarkPosition==9:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/6)*5-(newWatermark.width/2)), int((imagetoEdit.height/6)*5-(newWatermark.height/2))), newWatermark)


    else:
        imagetoEdit.paste(newWatermark, (int((imagetoEdit.width/2)-(newWatermark.width/2)), int((imagetoEdit.height/2)-(newWatermark.height/2))), newWatermark)
    
    return imagetoEdit



folderPath = imageDirectory + "/Watermark_added_images"
if (not os.path.isdir(folderPath)):
    os.mkdir(folderPath)

files = os.listdir(imageDirectory)
extensions = ['jpg', 'jpeg', 'png']

for file in files:
    ext = file.split(".")[-1]
    if ext in extensions:
        imagetoEdit = Image.open( imageDirectory +'/' + file)
        editedImage = addWatermark(imagetoEdit)
        editedImage.save(folderPath + '/' + file)







window=tk.Tk()
window.title('Apply waremark')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width=300
height=150

lbl1=Label(window, text="Successfully Completed", fg='#000000', font=("montserrat bold", 12))
lbl1.pack(anchor=CENTER, pady=(15, 0))

button = Button( window, background='#21b3e1', foreground='WHITE', highlightthickness=2, highlightcolor='WHITE', width=10, border=0, cursor='hand2', text='OK', font=('montserrat', 10, 'bold'), command=window.destroy )
button.pack(anchor=CENTER, pady=(10, 0))

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window.mainloop()
      
