#Question No 2
#last two digits of your student Id for printing the shape.
row=10
for i in range(1,row,2):
  for k in range(row-1,i,-2):
    print(" ",end=" ")
  for j in range(0,i):
    if(j+1==i-j):
      print("9",end=" ")
    elif(i+1==row):
      print("9",end=" ")
    else:
      print("0",end=" ")
  print()    
for i in range(row-1,0,-2):
  if(i != row-1):
    for k in range(i,row-1,2):
      print(" ",end=" ")
    for j in range(0,i):
      if(j+1==i-j):
        print("9",end=" ")
      else:
        print("0",end=" ")
    print()