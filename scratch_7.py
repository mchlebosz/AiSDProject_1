import random
import time
#malejące
ilości = []
malejące=[[]]
for i in range(0,10):
    k=int(input())
    ilości.append(k)
print(ilości)
for i in range(len(ilości)):
    for j in range(ilości[i]):
        n=j
        malejące[-1].append(n)
    malejące[-1].sort(reverse=True)
    malejące.append([])
malejące.pop(-1)
#rosnące
rosnące=[[]]
for i in range(len(ilości)):
    for j in range(ilości[i]):
        n=j
        rosnące[-1].append(n)
    rosnące.append([])
rosnące.pop(-1)
#los
losowe = [[]]
for i in range(len(ilości)):
    for j in range(ilości[i]):
        n = random.randint(1, 100000)
        losowe[-1].append(n)
    losowe.append([])
losowe.pop(-1)
#stałe
stałe=[[]]
o=random.randint(1,100000)
for i in range(len(ilości)):
    for j in range(ilości[i]):
        stałe[-1].append(o)
    stałe.append([])
stałe.pop(-1)
#Akszt
A=[[]]
x=1
for i in range(len(ilości)):
    for j in range(ilości[i]):
        if j<ilości[i]/2:
            A[-1].append(j)
        else:
            A[-1].append(ilości[i]-x)
            x=x+1
    x=1
    A.append([])
A.pop(-1)
#insertion
def insetrsort(list):
    for i in range(1,len(list)):
        j=i-1
        while list[j]>list[j+1] and j>=0:
            a=list[j]
            list[j]=list[j+1]
            list[j+1]=a
            j=j-1
#selection
def selectionSort(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                a=lista[i]
                lista[i]=lista[j]
                lista[j]=a
#shellsort
def shell_sort(list):
    size = len(list)
    gap=size//2
    while gap>0:
        for i in range(gap, size):
            zaczep=list[i]
            j=i

            while j>=gap and list[j-gap]> zaczep:
                list[j]= list[j-gap]
                j-=gap
            list[j]= zaczep
        gap=gap//2
M=[losowe,malejące,rosnące,stałe,A]
timesins=[[]]
for j in range(len(M)):
    for i in range(0,10):
        start_all = time.time()
        start = time.time()
        insetrsort(M[j][i])
        end = time.time()
        end_all = time.time()
        timesins[-1].append(end - start)
    timesins.append([])
timesins.pop(-1)
timessel=[[]]
for j in range(len(M)):
    for i in range(0,10):
        start_all = time.time()
        start = time.time()
        selectionSort(M[j][i])
        end = time.time()
        end_all = time.time()
        timessel[-1].append(end - start)
    timessel.append([])
timessel.pop(-1)
timesshell=[[]]
for j in range(len(M)):
    for i in range(0,10):
        start_all = time.time()
        start = time.time()
        shell_sort(M[j][i])
        end = time.time()
        end_all = time.time()
        timesshell[-1].append(end - start)
    timesshell.append([])
timesshell.pop(-1)

print(timesins)
print(timessel)
print(timesshell)
from openpyxl import Workbook
wb = Workbook()
sheet= wb.active
sheet1=wb.active
for i in range(len(timessel)):
    sheet.append(timessel[i])
for i in range(len(timesins)):
    sheet1.append(timesins[i])
for i in range(len(timesshell)):
    sheet.append(timesshell[i])
wb.save("danedowykresó.xlsx")