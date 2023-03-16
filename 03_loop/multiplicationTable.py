for i in range(2,9,3) :
  for j in range(1,10) :
    print("{} X {} = {:2}".format(i,j,i*j),end='\t')
    if i+2 < 10 :
      print("{} X {} = {:2}".format(i+1,j,(i+1)*j),end='\t')
      print("{} X {} = {:2}".format(i+2,j,(i+2)*j))
    else :
      print("{} X {} = {:2}".format(i+1,j,(i+1)*j))
  print()