def make(func,arg1,arg2):
    result=[]
    for i in range(4):
        if arg1[i]==0:
            if arg2[i]==0:
                result[i]=func[0]
            else: result[i]=func[1]
        elif arg2[i]==0:
            result[i]=func[2]
        else: result[i]=func[3]
    return result



table=[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
vvod=[9]
R_old1=[]
R_old2=[]
R_new=[]
for i in vvod:
    R_old1.append(table[i])
    R_old2.append(table[i])
R_old2.append(table[3])
R_old2.append(table[5])

for i in R_old1:
    for j in R_old2:
        for k in R_old2:
            R_new.append(make(i,j,k))

print(R_old1)
print("hello world")

#if R_old==R_new: break()
#for func in R-New://in range
#    or el in table:
#		if func==tabele:
#	check[