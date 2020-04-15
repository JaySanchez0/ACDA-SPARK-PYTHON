import matplotlib.pyplot as plt
def graph(keys, values):
    plt.bar(keys,values, label="Example two", color='g')
    plt.show()
def loadData():
    file = open("outputs/output1.txt")
    di = dict()
    dat = file.readline()
    while dat:
        data = dat.replace("(u","").replace("\n","").replace(",","").replace(")","").split(" ")
        try:
            di[data[0]]
        except KeyError:
            di[data[0]]=0
        di[data[0]]+=int(data[1])
        dat = file.readline()
    graph(list(di.keys()),list(di.values()))
loadData()
