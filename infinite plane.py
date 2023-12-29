from tkinter import *
from PIL import ImageTk, Image

def charge_move(event):
    x = int(canvas.coords(circle1)[0])-600
    x_new = scale_int.get()
    if x_new<=x:
        canvas.move(circle1, -x+scale_int.get(), 0)
        canvas.move(circle2, x-scale_int.get(), 0)
        lab = Label(wp,text='image charge position='+str(-x_new))
        lab.grid(row=25, column= 0)
    else:
        canvas.move(circle1, scale_int.get()-x, 0)
        canvas.move(circle2, -scale_int.get()+x, 0)
        
        lab = Label(wp,text='image charge position='+str(-x_new))
        lab.grid(row=25, column= 0)
    
def newq(event):
    q_img = Label(wp,text='induced charge(q\')='+str(-int(q.get()))+'C')
    q_img.grid(row=30, column= 0)

#tkinter stuff
wp = Tk()
wp.geometry('1000x1000')
wp.title('Infinite Plane Model')
canvas = Canvas(wp, bg='white')
canvas.config(width=1000, height=500)
canvas.create_rectangle((450,0,550,200000000), fill='blue')
q = Entry(wp, width=50)
q.insert(0, "Insert q in terms of coulombs")

q.bind('<Return>', newq)

#canvas
org1 = Image.open('real.png').resize((240,130))
org2 = Image.open('image.png').resize((240,130))
img1 = ImageTk.PhotoImage(org1)
img2 = ImageTk.PhotoImage(org2)
circle1 = canvas.create_image(600,250,image=img1)
circle2 = canvas.create_image(400,250,image=img2)


scale_int = IntVar(value=10)
scale = Scale(wp, command= charge_move, from_=0, to = 500, length = 500, orient='horizontal',variable=scale_int)

canvas.grid(row=0,column= 0)
scale.grid(row=20, column=0)
q.grid()


wp.mainloop()