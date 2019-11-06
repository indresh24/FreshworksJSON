import os
import json
Folder_Name=input("Enter the path....")
Input_File_Name=input("Enter input file name....")
Output_File_Name=input("Enter output file name....")
size=int(input("Enter the size of the file in bytes....."))
with open(Folder_Name+'/'+Output_File_Name+'1'+'.json','w') as textfile:
    textfile.seek(size)
    textfile.write("\0")
print("The size of the file before merging is ",os.path.getsize(Folder_Name+'/'+Output_File_Name+'1'+'.json'))
before=os.path.getsize(Folder_Name+'/'+Output_File_Name+'1'+'.json')
resultant=[]
counter=1
totalcount=0
while True:
    RESULT=Folder_Name+'/'+Input_File_Name+str(counter)+'.json'
    if os.path.exists(RESULT):
        with open(RESULT) as textfile:
            data=json.load(textfile)
            resultant.append(data)
        counter=counter+1
    else:
        break
resultJSON={}
temporary=[]
for i in resultant:
    for k,v in i.items():
        temporary.append(v)
temp=[]
x=0
for i in temporary:
    for j in range(0,len(i)):
        temp.append(temporary[x][j])
        totalcount=totalcount+1
    x=x+1
resultJSON={}
resultantroot=list(resultant[0].keys())
resultJSON[resultantroot[0]]=temp
print("The resultJSON is ...",resultJSON)
with open(Folder_Name+'/'+Output_File_Name+'1'+'.json','w') as textfile:
    json.dump(resultJSON,textfile)
print("The size of the file after merging is ",os.path.getsize(Folder_Name+'/'+Output_File_Name+'1'+'.json'))
root=list(resultJSON.keys())
root=root[0]
status="yes"
while status=="yes":
    after=os.path.getsize(Folder_Name+'/'+Output_File_Name+'1'+'.json')
    if(after>before):
        print("Some problem")
        exit(1)
    print("Which operation you would like to perform")
    print("Type 1 for update attribute")
    print("Type 2 for insert attribute")
    print("Type 3 for updating root key")
    choice=int(input())
    if choice==2:
        k=0
        l=0
        for j in range(0,totalcount):
            print("Enter the key to be inserted for ",resultJSON[root][j]["name"])
            key=input()
            print("Enter its value")
            value=input()
            resultJSON[root][j][key]=value
            k=k+1
            l=l+1
    if choice==1:
        print("The value of root is ",root)
        print("Enter the name of the employee to be updated")
        for j in range(0,totalcount):
            print(resultJSON[root][j]["name"])
        name=input()
        for j in range(0,totalcount):
            if resultJSON[root][j]['name'] == name:
                print("The avaiable operations are",list(resultJSON[root][0].keys()))
                print("Enter the category to be updated")
                category=input()
                if isinstance(resultJSON[root][j][category],str):
                    putvalue=input("Enter the value")
                    resultJSON[root][j][category]=putvalue

                else:
                    putvalue=input("Enter the value to be inserted or deleted")
                    if putvalue in resultJSON[root][j][category]:
                        resultJSON[root][j][category].remove(putvalue)
    if choice==3:
        print("Enter the value of rootkey to be updated")
        name=input()
        resultJSON[name]=resultJSON[root]
        temp=root
        root=name
        del resultJSON[temp]
    with open(Folder_Name+'/'+Output_File_Name+'1'+'.json','w') as textfile:
        json.dump(resultJSON,textfile)
    status=input("Type yes to continue")
