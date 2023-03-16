import matplotlib.pyplot as plt
import numpy as np

liste=[]

def main():
    _input=makeList()
    formatted=format(_input)
    datas=[np.mean(formatted),np.std(formatted),len(formatted)]
    print(datas)
    graphIT(formatted)
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
            #if j==1000:
             #   break
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
    Yaxis=l
    for i in range(len(l)):
        Xaxis.append(i+1)
        #print(i)
    plt.bar(Xaxis,Yaxis)
    plt.show()




print(main())
