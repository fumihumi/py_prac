from  tkinter import *

root = Tk()


# b0 = Button(root,text ='hello')
# b1 = Button(root,text = 'world')

# b0.pack(side=LEFT)
# b1.pack(side=LEFT)

# cnt = 1
# for j in range(3):
#   f = Frame(root)
#   f.pack()
#   for i in range(2):
#     # i= Button(f,text= i)
#     i = Label(f,text = cnt)
#     i.pack(side=LEFT)
#     cnt += 1

# def clicked(e):
#   print(e.widget['text'])
#   tmp = int(e.widget['text']) * 2
#   e.widget['text'] = str(tmp)

# for i in range(25):
#   b = Button(root, text = str(i + 1), width = 10 , font = ('',12))
#   b.grid(row = i //5 , column = i % 5)
#   b.bind("<Button-1>" , clicked)


count  = 1

def clicked(e):
  global count
  count += 1
  if (count % 2) == 0:
    e.widget['text'] = '◎'
  else:
    e.widget['text'] ='✖'
    
for i in range(9):
  b = Button(root, text= '', width = 10 , font = ('',12))
  b.grid(row = i //3 , column = i % 3)
  b.bind("<Button-1>" , clicked)


root.mainloop()