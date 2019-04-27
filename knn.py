import pandas as pd
import math


file=open("Testdata.txt","r")
Temp=file.read()
arr=Temp.split("\n")
Testdata=[]
for line in arr:
    Testdata.append(line.split(","))
file=open("Traindata.txt","r")
Temp=file.read()
arr=Temp.split("\n")
Traindata=[]
for line in arr:
    Traindata.append(line.split(","))
def calculate_distance(test , train):
    d=0
    for i in range(0,len(test),1):
        d+=((float(test[i])-float(train[i]))**2)
    return math.sqrt(d)

def calculate_distances_for_one_row(k,test):
    distances=[]
    for i in range(0,len(Traindata),1):
        distances.append((calculate_distance(test,Traindata[i][:-1]),i))
        distances.sort(reverse=False)
        knn=distances[:k]
    index=[]
    labels=[]
    for i,j in knn:
        index.append(j)
    index.sort()
    for j in index:
        labels.append(Traindata[j][-1])
    count=[]
    for j in labels:
        count.append(labels.count(j))
    label=count.index(max(count))
    return labels[label]


def knn(k):
    Accuracy=0
    print("K value : ", k)
    for i in range(len(Testdata)):
        label=calculate_distances_for_one_row(k,Testdata[i][:-1])
        print("Predicated class : ",label,"     Actual Class : ",Testdata[i][-1] )
        if label==Testdata[i][-1]:
            Accuracy+=1
    print("Number of correctly classified instances: " , Accuracy,)
    print("Total number of instances: ",len(Testdata))
    Accuracy/=float(len(Testdata))
    print("Accuracy : " , Accuracy)


for i in range(1,10,1):
    knn(i)


