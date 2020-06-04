dad = []

for i in range(5):
    temp = []
    dad.append(temp)
dad[1] = [1,2,3]
print(dad)
print(len(dad))
#
#
#
#
# for i in range(len(dad)):
#     print("daddy", i)


for i in dad:
    if len(i)==0:
        print("ZERO")
    else:
        print(len(i))
    # for j in range(len(i)):
    #     print(i, "", j)
        # if i[j]==None:
        #     print("NADA")
        # else:
        #     print(len(i))