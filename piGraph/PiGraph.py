import matplotlib.pyplot as plt
import numpy as np

liste=[]

def main():
    _input=makeList()
    Single=singleFormatting(_input)
    #formatted=format(_input) #points made with every two ciphers of pi
    #FuncPoints=SinF(formatted) #points with sin function apllied
    data=mostFrequent(Single,1)
    datas=[np.mean(data),np.std(data),len(data),mostFrequent(Single,1)[-1]]
    print(datas)
    graphIT(data)
    return datas

def makeList():
    j=0
    with open("one-millionAfter.txt", mode="r",encoding="utf-8") as f:
        for line in f:
            j+=1
            l=list(line)
            for i in range(len(l)//2):
                liste.append((l[0],l[1]))
                l.pop(0)
                l.pop(0)
            if j==1000000: #uncomment to stop it before
                break


    return liste


def format(l):
    points=[]
    for x in l:
        if x[0]=="0":
            points.append(int(x[1]))
        else:
            points.append(int(x[0]+x[1]))
    return points


def graphIT(l):
    Xaxis=[]
    Yaxis=[]
    for i in range(len(l)):
        Yaxis.append(l[i][1])
        Xaxis.append(l[i][0])
        #print(i)
    plt.bar(Xaxis,Yaxis)
    plt.show()


def SinF(l):
    r=[]
    for x in l:
        r.append(np.sin(x))
    return r
def singleFormatting(l):
    r=[]
    for x in  l:
        r.append(int(x[0]))
        r.append(int(x[1]))
    return r

def mostFrequent(l,i):
    res=0
    e=[]
    if i==1:
        r=range(10)
    if i==2:
        r=range(100)
    for x in r:
        e.append((x,l.count(x)))
    return list(sorted(e,key=lambda k : k[0]))




    




print(main())
