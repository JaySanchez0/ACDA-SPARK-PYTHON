import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
def showUsers(keys):
    win = tk.Tk()
    win.title="Usuarios"
    win.geometry("300x300")
    l = tk.Label(win,text="Usuarios")
    l.grid(row=0,column=1,pady=2)
    for i in range(len(keys)):
        lb = tk.Label(win,text=str(i+1))
        lb.grid(row=i+1,column=1)
        lb = tk.Label(win,text=keys[i])
        lb.grid(row=i+1,column=2)
def graph(keys, values):
    print(keys)
    print(values)
    fig, ax = plt.subplots()
    rects1 = ax.bar(keys,values, label="Example two", color='r')
    ax.set_ylim(0,max(values)+10)
    ax.set_ylabel('Frequency')
    ax.set_title('Usuarios que mas escriben tweets')
    ax.set_xticklabels([1,2,3,4,5,6,7,8,9,10])
    showUsers(keys)
    plt.show()
def loadData():
    file = open("outputs/output3.txt")
    di = dict()
    dat = file.readline()
    while dat:
        data = dat.replace("(u","").replace("\n","").replace(",","").replace(")","").replace("(","").split(" ")
        try:
            di[data[0]]
        except KeyError:
            di[data[0]]=0
        di[data[0]]+=int(data[1])
        dat = file.readline()
    l1 = list(di.keys()).copy()
    l2 = list(di.values()).copy()
    keys = []
    values = []
    for i in range(10):
        keyMax = None
        for key in di.keys():
            if keyMax==None or di[key]>di[keyMax]:
                keyMax = key
        keys.append(keyMax)
        values.append(di[keyMax])
        di[keyMax] = -1
                
    graph(keys,values)
loadData()
