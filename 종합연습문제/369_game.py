import os
import numpy as np

for i in range(1,101) :
    t_length = len(str(i).split("3"))
    s_length = len(str(i).split("6"))
    n_legnth = len(str(i).split("9"))

    if t_length + s_length + n_legnth > 3+1 :
        print(i,end='\t')
        print("X" * (t_length + s_length + n_legnth - 3))