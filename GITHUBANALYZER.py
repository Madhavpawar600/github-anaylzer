from requests import get
import time
import json
import threading
import base64
import requests
from urllib.request import urlopen
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
##from auth import username,password
from tkinter import *
from PIL import Image,ImageTk
import urllib.parse
import urllib.request
import io
from io import BytesIO
import time
un=str()
pa=str()

#--------------------------------------------
un=str()
pa=str()
def login():
    un=E1.get()
    pa=E2.get()
    top1=Tk()
    top1.geometry('1600x1600')
    top1.configure(background='white')
    login=get('https://api.github.com/user', auth=(un,pa)).json()
    aa=get('https://api.github.com/users/'+login['login']+'/repos',auth=(un,pa)).json()
    fork=[]
    repos=[]
    visitors=[]
    unqvst=[]
    clones=[]
##    url=aa[1]['owner']['avatar_url']
##    print('url',url)
    for i in range(0,len(aa)):
        repos.append(aa[i]['name'])
        fork.append(aa[i]['forks_count'])
    def views(repos):
        for i in range(0,len(repos)):
            cc=get('https://api.github.com/repos/'+login['login']+ '/' +repos[i]+'/traffic/views', auth=(un,pa)).json()
            visitors.append(cc['count'])
            unqvst.append(cc['uniques'])
    def clone(repos):
        for i in range(0,len(repos)):
            vc=get('https://api.github.com/repos/'+login['login']+ '/' +repos[i]+'/traffic/clones', auth=(un,pa)).json()
            clones.append(vc['count'])
    t1=threading.Thread(target=views ,args=(repos,))
    t2=threading.Thread(target=clone, args=(repos,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


##    for i in range(5):
##        for j in range(4):
##            e = Label(top1,text='%d.%d'%(i,j),relief=RIDGE)
##            e.grid(row=i, column=j, sticky=NSEW)
##            e.insert(END, '%d.%d' % (i, j))
##            cols.append(e)
##        rows.append(cols)



    
    L1=Label(top1,text='Welcome '+str(un),relief=RIDGE)     #relief=BRIDGE   to bound with box to each item
    L1.grid(row=0, column=0,sticky=NSEW)

    L1=Label(top1,text='SNo.',relief=RIDGE)
    L1.grid(row=1, column=1,sticky=NSEW)                         #sticky=NSEW    to divide equally by line
    L1=Label(top1,text='Repo Names             ',relief=RIDGE)
    L1.grid(row=1, column=2,sticky=NSEW)
    L1=Label(top1,text='Clones     ',relief=RIDGE)
    L1.grid(row=1, column=3,sticky=NSEW)
    L1=Label(top1,text='Forks     ',relief=RIDGE)
    L1.grid(row=1, column=4,sticky=NSEW)
    L1=Label(top1,text='Unique Visitors     ',relief=RIDGE)
    L1.grid(row=1, column=5,sticky=NSEW)
    L1=Label(top1,text='Total Visitors     ',relief=RIDGE)
    L1.grid(row=1, column=6,sticky=NSEW)
    for j in range(7):
        for i in range(len(repos)):
##            L1=Label(top1,text=' '*40,relief=RIDGE)
##            L1.grid(row=i+2, column=0,sticky=NSEW)
            L1=Label(top1,text=i+1,relief=RIDGE)
            L1.grid(row=i+2, column=1,sticky=NSEW)
            L1=Label(top1,text=repos[i],relief=RIDGE)
            L1.grid(row=i+2, column=2,sticky=NSEW)
            L1=Label(top1,text=clones[i],relief=RIDGE)
            L1.grid(row=i+2, column=3,sticky=NSEW)
            L1=Label(top1,text=fork[i],relief=RIDGE)
            L1.grid(row=i+2, column=4,sticky=NSEW)
            L1=Label(top1,text=unqvst[i],relief=RIDGE)
            L1.grid(row=i+2, column=5,sticky=NSEW)
            L1=Label(top1,text=visitors[i],relief=RIDGE)
            L1.grid(row=i+2, column=6,sticky=NSEW)
    def showGraph():
        plt.bar(repos,visitors)
        plt.show()
    k=len(repos)
    b2=Button(top1,text='Show Graph',bg='blue',command=showGraph)
    b2.grid(row=k+2, column=3)



##    url=aa[1]['owner']['avatar_url']
##    response = requests.get(url)
##    img = Image.open(BytesIO(response.content))
##    render = ImageTk.PhotoImage(img)
##    img = Label(top1,image=render)
##    img.image = render
##    img.grid(row=0,column=0)
    top1.mainloop()
    
    



top=Tk()
top.geometry('1600x1600')
top.configure(background='white')

L1=Label(top,text='User Name')
L1.grid(row=0, column=0)
##L1.pack(side=LEFT)
E1=Entry(top,bd=5)
E1.grid(row=0, column=1)
##E1.pack(side=RIGHT)


L2=Label(top,text='Password')
L2.grid(row=1, column=0)
##L1.pack(side=RIGHT)
E2=Entry(top,show='*',bd=5)
E2.grid(row=1, column=1)
##E1.pack(side=RIGHT)

b1=Button(top,text='Login',bg='blue',command=login)
b1.grid(row=2, column=1)
##b1.pack(side=LEFT)


top.mainloop()
