import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
import ch2
from collections import Counter

fig = plt.figure()
plt.xlabel('Width')
plt.ylabel('Height')
ax = fig.gca()

# Отображение QPSK
for i in range(len(ch2.bg_sdvig)):
    for j in range(4):
        if len(ch2.bg_sdvig[i])>0:
            x = ch2.bg_sdvig[i][j][0]
            y = ch2.bg_sdvig[i][j][1]
            ax.plot(x,y,'o', color='b')
        else: continue
    
# Отображение результата сложения I и III четвертей
if len(ch2.check_new_1_3)>0:
    if len(ch2.check_new_1_3)==8 and Counter(ch2.B)!=Counter(ch2.check_new_1_3):
        for j in range(4):
            x = ch2.check_new_1_3[i]
            y = ch2.check_new_1_3[i+1]
            ax.plot(x,y,'o', color='r')
    elif len(ch2.check_new_1_3)==32 and Counter(ch2.B)!=Counter(ch2.check_new_1_3): 
        for i in range(0,32,2):
            x = ch2.check_new_1_3[i]
            y = ch2.check_new_1_3[i+1]
            ax.plot(x,y,'o', color='r')
else: pass

# Отображение результата сложения I и II четвертей
if len(ch2.check_new_1_2)>0:
    if len(ch2.check_new_1_2)==8 and Counter(ch2.B)!=Counter(ch2.check_new_1_2):
        for j in range(4):
            x = ch2.check_new_1_2[i]
            y = ch2.check_new_1_2[i+1]
            ax.plot(x,y,'o', color='g')
    elif len(ch2.check_new_1_2)==32 and Counter(ch2.B)!=Counter(ch2.check_new_1_2): 
        for i in range(0,32,2):
            x = ch2.check_new_1_2[i]
            y = ch2.check_new_1_2[i+1]
            ax.plot(x,y,'o', color='g')
else: pass
# Отображение результата сложения I и IV четвертей
if len(ch2.check_new_1_4)>0:
    if len(ch2.check_new_1_4)==8 and Counter(ch2.B)!=Counter(ch2.check_new_1_4):
        for j in range(4):
            x = ch2.check_new_1_4[i]
            y = ch2.check_new_1_4[i+1]
            ax.plot(x,y,'o', color='y')
    elif len(ch2.check_new_1_4)==32 and Counter(ch2.B)!=Counter(ch2.check_new_1_4): 
        for i in range(0,32,2):
            x = ch2.check_new_1_4[i]
            y = ch2.check_new_1_4[i+1]
            ax.plot(x,y,'o', color='y')
else: pass
# Отображение результата сложения II и III четвертей
if len(ch2.check_new_2_3)>0:
    if len(ch2.check_new_2_3)==8 and Counter(ch2.B)!=Counter(ch2.check_new_2_3):
        for j in range(4):
            x = ch2.check_new_2_3[i]
            y = ch2.check_new_2_3[i+1]
            ax.plot(x,y,'o', color='k')
    elif len(ch2.check_new_2_3)==32 and Counter(ch2.B)!=Counter(ch2.check_new_2_3): 
        for i in range(0,32,2):
            x = ch2.check_new_2_3[i]
            y = ch2.check_new_2_3[i+1]
            ax.plot(x,y,'o', color='k')
else: pass
# Отображение результата сложения II и IV четвертей
if len(ch2.check_new_2_4)>0:
    if len(ch2.check_new_2_4)==8 and Counter(ch2.B)!=Counter(ch2.check_new_2_4):
        for j in range(4):
            x = ch2.check_new_2_4[i]
            y = ch2.check_new_2_4[i+1]
            ax.plot(x,y,'o', color='m')
    elif len(ch2.check_new_2_4)==32 and Counter(ch2.B)!=Counter(ch2.check_new_2_4): 
        for i in range(0,32,2):
            x = ch2.check_new_2_4[i]
            y = ch2.check_new_2_4[i+1]
            ax.plot(x,y,'o', color='m')
else: pass
    
# Отображение результата сложения III и IV четвертей
if len(ch2.check_new_3_4)>0:
    if len(ch2.check_new_3_4)==8 and Counter(ch2.B)!=Counter(ch2.check_new_3_4):
        for j in range(4):
            x = ch2.check_new_3_4[i]
            y = ch2.check_new_3_4[i+1]
            ax.plot(x,y,'o', color='c')
    elif len(ch2.check_new_3_4)==32 and Counter(ch2.B)!=Counter(ch2.check_new_3_4): 
        for i in range(0,32,2):
            x = ch2.check_new_3_4[i]
            y = ch2.check_new_3_4[i+1]
            ax.plot(x,y,'o', color='c')
else: pass
plt.grid()
plt.show()