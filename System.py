import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
import values
from collections import Counter

fig = plt.figure()
plt.xlabel('Width')
plt.ylabel('Height')
ax = fig.gca()

# Отображение QPSK
for i in range(len(values.bg_sdvig)):
    for j in range(4):
        if len(values.bg_sdvig[i])>0:
            x = values.bg_sdvig[i][j][0]
            y = values.bg_sdvig[i][j][1]
            ax.plot(x,y,'o', color='b')
        else: continue
    
# Отображение результата сложения I и III четвертей
if len(values.check_new_1_1)>0:
    if len(values.check_new_1_1)==8 and Counter(values.B)!=Counter(values.check_new_1_1):
        for j in range(4):
            x = values.check_new_1_1[i]
            y = values.check_new_1_1[i+1]
            ax.plot(x,y,'o', color='r')
    elif len(values.check_new_1_1)==32 and Counter(values.B)!=Counter(values.check_new_1_1): 
        for i in range(0,32,2):
            x = values.check_new_1_1[i]
            y = values.check_new_1_1[i+1]
            ax.plot(x,y,'o', color='r')
else: pass

# Отображение результата сложения I и II четвертей
if len(values.check_new_1_2)>0:
    if len(values.check_new_1_2)==8 and Counter(values.B)!=Counter(values.check_new_1_2):
        for j in range(4):
            x = values.check_new_1_2[i]
            y = values.check_new_1_2[i+1]
            ax.plot(x,y,'o', color='g')
    elif len(values.check_new_1_2)==32 and Counter(values.B)!=Counter(values.check_new_1_2): 
        for i in range(0,32,2):
            x = values.check_new_1_2[i]
            y = values.check_new_1_2[i+1]
            ax.plot(x,y,'o', color='g')
else: pass
# Отображение результата сложения I и IV четвертей
if len(values.check_new_1_3)>0:
    if len(values.check_new_1_3)==8 and Counter(values.B)!=Counter(values.check_new_1_3):
        for j in range(4):
            x = values.check_new_1_3[i]
            y = values.check_new_1_3[i+1]
            ax.plot(x,y,'o', color='y')
    elif len(values.check_new_1_3)==32 and Counter(values.B)!=Counter(values.check_new_1_3): 
        for i in range(0,32,2):
            x = values.check_new_1_3[i]
            y = values.check_new_1_3[i+1]
            ax.plot(x,y,'o', color='y')
else: pass
# Отображение результата сложения II и III четвертей
if len(values.check_new_2_2)>0:
    if len(values.check_new_2_2)==8 and Counter(values.B)!=Counter(values.check_new_2_2):
        for j in range(4):
            x = values.check_new_2_2[i]
            y = values.check_new_2_2[i+1]
            ax.plot(x,y,'o', color='k')
    elif len(values.check_new_2_2)==32 and Counter(values.B)!=Counter(values.check_new_2_2): 
        for i in range(0,32,2):
            x = values.check_new_2_2[i]
            y = values.check_new_2_2[i+1]
            ax.plot(x,y,'o', color='k')
else: pass
# Отображение результата сложения II и IV четвертей
if len(values.check_new_2_3)>0:
    if len(values.check_new_2_3)==8 and Counter(values.B)!=Counter(values.check_new_2_3):
        for j in range(4):
            x = values.check_new_2_3[i]
            y = values.check_new_2_3[i+1]
            ax.plot(x,y,'o', color='m')
    elif len(values.check_new_2_3)==32 and Counter(values.B)!=Counter(values.check_new_2_3): 
        for i in range(0,32,2):
            x = values.check_new_2_3[i]
            y = values.check_new_2_3[i+1]
            ax.plot(x,y,'o', color='m')
else: pass
    
# Отображение результата сложения III и IV четвертей
if len(values.check_new_3_3)>0:
    if len(values.check_new_3_3)==8 and Counter(values.B)!=Counter(values.check_new_3_3):
        for j in range(4):
            x = values.check_new_3_3[i]
            y = values.check_new_3_3[i+1]
            ax.plot(x,y,'o', color='c')
    elif len(values.check_new_3_3)==32 and Counter(values.B)!=Counter(values.check_new_3_3): 
        for i in range(0,32,2):
            x = values.check_new_3_3[i]
            y = values.check_new_3_3[i+1]
            ax.plot(x,y,'o', color='c')
else: pass
plt.grid()
plt.show()