# Question 1
alist=[]  # A

alist.append("apple") # B

# C , Two diferent solutions
blist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
blist=[0]*20

# d
clist=alist+blist
print(clist)

# e, multiple solutions
clast=clist.pop()
print(clast)

clast=clist[len(clist)-1]
print(clast)
# 
# clast=clist[20]
# print(clast)

