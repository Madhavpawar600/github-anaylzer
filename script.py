from requests import get
import time
import json
import threading
#from mutliprocessing import Pool
from pprint import pprint
from auth import username,password

##response=get("https://api.github.com/")
##print(response)
##username=input("enter your username")
##password=input("enter your password")
t=time.time()
login=get('https://api.github.com/user', auth=(username,password)).json()



aa=get('https://api.github.com/users/'+login['login']+'/repos',auth=(username,password)).json()
fork=[]
repos=[]
visitors=[]
unqvst=[]
clones=[]

for i in range(0,len(aa)):
    repos.append(aa[i]['name'])
    fork.append(aa[i]['forks_count'])


def views(repos):
    for i in range(0,len(repos)):
        cc=get('https://api.github.com/repos/'+login['login']+ '/' +repos[i]+'/traffic/views', auth=(username,password)).json()
        visitors.append(cc['count'])
        unqvst.append(cc['uniques'])

def clone(repos):
    for i in range(0,len(repos)):
        vc=get('https://api.github.com/repos/'+login['login']+ '/' +repos[i]+'/traffic/clones', auth=(username,password)).json()
        clones.append(vc['count'])

t1=threading.Thread(target=views ,args=(repos,))
t2=threading.Thread(target=clone, args=(repos,))

t1.start()
t2.start()

t1.join()
t2.join()


print('Username:',login['login'])
print('Bio:',login['bio'])
print('Followers:',login['followers'])
print('Following:',login['following'])
print(repos)
print("forks->",fork)    
print('clone-:',clones)
print('visitors-',visitors)
print('unique->',unqvst)
print("done",time.time() -t)

