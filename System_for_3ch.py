import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
import ch3
from collections import Counter

fig = plt.figure()
plt.xlabel('Width')
plt.ylabel('Height')
ax = fig.gca()

# Отображение QPSK
for i in range(len(ch3.bg_sdvig)):
    for j in range(4):
        if len(ch3.bg_sdvig[i])>0:
            x = ch3.bg_sdvig[i][j][0]
            y = ch3.bg_sdvig[i][j][1]
            ax.plot(x,y,'o', color='b')
        else: continue
    
# Отображение результата сложения I, II, III четвертей
if len(ch3.check_new_1_2_3)>0:
    if len(ch3.check_new_1_2_3)==8 and Counter(ch3.B)!=Counter(ch3.check_new_1_2_3):
        for j in range(4):
            x = ch3.check_new_1_2_3[i]
            y = ch3.check_new_1_2_3[i+1]
            ax.plot(x,y,'o', color='r')
    elif len(ch3.check_new_1_2_3)==128 and Counter(ch3.B)!=Counter(ch3.check_new_1_2_3): 
        for i in range(0,128,2):
            x = ch3.check_new_1_2_3[i]
            y = ch3.check_new_1_2_3[i+1] 
            ax.plot(x,y,'o', color='r')
else: pass
# Отображение результата сложения I, II, IV четвертей
if len(ch3.check_new_1_2_4)>0:
    if len(ch3.check_new_1_2_4)==8 and Counter(ch3.B)!=Counter(ch3.check_new_1_2_4):
        for j in range(4):
            x = ch3.check_new_1_2_4[i]
            y = ch3.check_new_1_2_4[i+1]
            ax.plot(x,y,'o', color='k')
    elif len(ch3.check_new_1_2_4)==128 and Counter(ch3.B)!=Counter(ch3.check_new_1_2_4): 
        for i in range(0,128,2):
            x = ch3.check_new_1_2_4[i]
            y = ch3.check_new_1_2_4[i+1] 
            ax.plot(x,y,'o', color='k')
else: pass
# Отображение результата сложения I, III, IV четвертей
if len(ch3.check_new_1_3_4)>0:
    if len(ch3.check_new_1_3_4)==8 and Counter(ch3.B)!=Counter(ch3.check_new_1_3_4):
        for j in range(4):
            x = ch3.check_new_1_3_4[i]
            y = ch3.check_new_1_3_4[i+1]
            ax.plot(x,y,'o', color='y')
    elif len(ch3.check_new_1_3_4)==128 and Counter(ch3.B)!=Counter(ch3.check_new_1_3_4): 
        for i in range(0,128,2):
            x = ch3.check_new_1_3_4[i]
            y = ch3.check_new_1_3_4[i+1] 
            ax.plot(x,y,'o', color='y')
else: pass
# Отображение результата сложения II, III, IV четвертей
if len(ch3.check_new_2_3_4)>0:
    if len(ch3.check_new_2_3_4)==8 and Counter(ch3.B)!=Counter(ch3.check_new_2_3_4):
        for j in range(4):
            x = ch3.check_new_2_3_4[i]
            y = ch3.check_new_2_3_4[i+1]
            ax.plot(x,y,'o', color='m')
    elif len(ch3.check_new_2_3_4)==128 and Counter(ch3.B)!=Counter(ch3.check_new_2_3_4): 
        for i in range(0,128,2):
            x = ch3.check_new_2_3_4[i]
            y = ch3.check_new_2_3_4[i+1] 
            ax.plot(x,y,'o', color='m')
else: pass

plt.grid()
plt.show()