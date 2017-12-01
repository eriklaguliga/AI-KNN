import xlrd
import math
import numpy

file_location = "test.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
sheet2 = workbook.sheet_by_index(1)

def cari_jarak(j,i, x1,x2,y1,y2,k1,k2,c1,c2):
    a = (x1[j][1]-x2[i][1])**2 + (y1[j][1]-y2[i][1])**2 + (k1[j][1]-k2[i][1])**2 + (c1[j][1] - c2[i][1])**2
    akar = math.sqrt(a)
    return akar

x1 = []
x2 = []
y1 = []
y2 = []
k1 = []
k2 = []
c1 = []
c2 = []
n1 = []#hoax
n2 = []#hoax
# Untuk data Tes
for i in range(1,sheet.nrows):
    x1_temp = []
    y1_temp =[]
    k1_temp = []
    c1_temp = []
    n1_temp= []
    x1_temp.append(i)
    y1_temp.append(i)
    k1_temp.append(i)
    c1_temp.append(i)
    n1_temp.append(i)
    x1_temp.append(sheet.cell_value(i,1))
    y1_temp.append(sheet.cell_value(i,2))
    k1_temp.append(sheet.cell_value(i,3))
    c1_temp.append(sheet.cell_value(i,4))
    n1_temp.append(sheet.cell_value(i,5))
    x1.append(x1_temp)
    y1.append(y1_temp)
    k1.append(y1_temp)
    c1.append(c1_temp)
    n1.append(n1_temp)
    x

# Untuk Data Train
for i in range(1,sheet2.nrows):
     x2_temp = []
     y2_temp = []
     k2_temp = []
     c2_temp = []
     n2_temp = []
     x2_temp.append(i)
     y2_temp.append(i)
     k2_temp.append(i)
     c2_temp.append(i)
     n2_temp.append(i)
     x2.append(sheet2.cell_value(i,1))
     y2.append(sheet2.cell_value(i,2))
     k2.append(sheet2.cell_value(i,3))
     c2.append(sheet2.cell_value(i,4))
     n2.append(sheet2.cell_value(i,5))
     x2.append(x2_temp)
     y2.append(y2_temp)
     k2.append(y2_temp)
     c2.append(c2_temp)
     n2.append(n2_temp)

# for i in range(len(x2)):
#     a= []
#     for j in range(len(x1)):
#         a = cari_jarak(x1[j][1], x2[i][1], y1[j][1], y2[i][1], k1[j][1], k2[i][1], c1[j][1], c2[i][1])
#     print(a)




