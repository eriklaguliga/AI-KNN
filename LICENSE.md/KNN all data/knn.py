import xlrd
import pandas as pd
import math

xls_files = pd.ExcelFile('Dataset Tugas 3 AI 1718.xlsx')
c =xls_files.parse('DataTrain')
d = xls_files.parse('DataTest')
train = []
test = []

#datatrain
for i in range(0,len(c)):
    tmp = []
    tmp.append(c["Like"][i])
    tmp.append(c["Provokasi"][i])
    tmp.append(c["Komentar"][i])
    tmp.append(c["Emosi"][i])
    tmp.append(c["Hoax"][i])
    train.append(tmp)
#datatest
sihoax = []
for i in range(0,len(d)):
    tmp = []
    tmp.append(d["Like"][i])
    tmp.append(d["Provokasi"][i])
    tmp.append(d["Komentar"][i])
    tmp.append(d["Emosi"][i])
    tmp.append(d["Hoax"][i])
    sihoax.append(d["Hoax"][i])
    test.append(tmp)

i = 0
sort = []
best = []
label =[]
while(i < len(test)):#test
    observer = test[i]
    arrdistance=[]

    for j in range(len(train)):
        temp=[]
        distance = 0
        for k in range(len(train[j])-1):
            distance = distance +( (observer[k]-train[j][k])**2)
        temp.append(math.sqrt(distance))
        temp.append(train[j][len(train[j])-1])
        arrdistance.append(temp)
        sort = sorted(arrdistance, key=lambda x: x[0], reverse=False)[0:11]
    hoax = 0
    tidak = 0
    print(i)
    for kk in range(0,len(sort)):
        #print(sort[kk])
        if(sort[kk][1]==1):
            hoax = hoax+1
        else:
            tidak = tidak+1
    #print(hoax)
    #print(tidak)
    if(hoax>tidak):
        label.append(1)
    else:
        label.append(0)
    i = i+1
    #print(i)
for i in range(len(label)):
    print("No.",i,"hasil:",label[i])

count = 0
for i in range(0,len(label)):
    if(label[i] == sihoax[i]):
        count = count +1


accurate = (count/len(label))*100
print("akurasi",accurate,"%")










