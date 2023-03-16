startCount=5 ; odd = 1
for i in range(1,startCount) :
  if i == 1 :
    print(' '*(startCount-i),"*")
  else :
    space = ' '*(odd)
    print(' '*(startCount-i),"*"+space+"*")
    odd += 2

startCount=5 ; odd = startCount+2
for i in range(startCount,0,-1) :
  if i == 1 :
    print(' '*(startCount-i),"*")
  else :
    space = ' '*(odd)
    print(' '*(startCount-i),"*"+space+"*")
    odd -= 2