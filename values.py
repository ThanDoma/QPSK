from math import *

f = [pi/4, pi/5, pi/6 ,pi/8, pi/9 ,pi/10, pi/12]

a_f = []
for i in range(4):
  a = int(input((f'Введите значение для {i+1} канала из набора [pi/4, pi/5, pi/6 ,pi/8, pi/9 ,pi/10, pi/12] ')))
  a_f.append(a-1)

A = []
for i in range(6):
  A.append(2*cos(f[i]-pi/4))

A_ = []
for i in range(6):
  A_.append(2*cos(-f[i]-pi/4))

A_sqrt = sqrt(2)
bg_sdvig, bg_sdvig_check = [], []
sdvig = [0, pi/2, pi, 3*pi/2]

check_1_1, check_1_2, check_1_3 = [], [], []
check_new_1_1, check_new_1_2, check_new_1_3 = [], [], []
check_2_2, check_2_3 = [], []
check_new_2_2, check_new_2_3 = [], []
check_3_3 = []
check_new_3_3 = []
B =[]
for i in range(4):
  if a_f[i]!=-1:
    bg = [[A_sqrt*(cos(f[a_f[i]]+pi/4+sdvig[i])), A_sqrt*(sin(f[a_f[i]]+pi/4+sdvig[i]))],
          [A[a_f[i]]*(cos(pi/4+sdvig[i])), A[a_f[i]]*(sin(pi/4+sdvig[i]))],
          [A_[a_f[i]]*(cos(pi/4+sdvig[i])), A_[a_f[i]]*(sin(pi/4+sdvig[i]))],
          [A_sqrt*(cos(-f[a_f[i]]+pi/4+sdvig[i])), A_sqrt*(sin(-f[a_f[i]]+pi/4+sdvig[i]))]]
    bg_sdvig.append(bg)
    
  elif a_f[i]==-1:
    bg_sdvig.append([])

for i in range(4):
  if len(bg_sdvig[i])>0:
    for j in range(4):
      B.append(round(bg_sdvig[i][j][0],7))
      B.append(round(bg_sdvig[i][j][1],7))

# Первая четверть + третья
if (len(bg_sdvig[0])>0 and len(bg_sdvig[2])>0):
  for i in range(4):
    for j in range(4):
      check_1_1.append(bg_sdvig[0][i]+bg_sdvig[2][j])

  for i in range(16):
    check_new_1_1.append(round(check_1_1[i][0],7)+round(check_1_1[i][2],7))
    check_new_1_1.append(round(check_1_1[i][1],7)+round(check_1_1[i][3],7))
    
elif (len(bg_sdvig[0])>0 and len(bg_sdvig[2])==0):
    for i in range(4):
      check_1_1.append(bg_sdvig[0][i])
    for i in range(4):
      for j in range(2):
        check_new_1_1.append(round(check_1_1[i][j],7))
  
elif (len(bg_sdvig[0])==0 and len(bg_sdvig[2])>0):
    for i in range(4):
      check_1_1.append(bg_sdvig[2][i])

    for i in range(4):
      check_new_1_1.append(round(check_1_1[i][1],7))  
else: pass

#Первая четверть + вторая
if (len(bg_sdvig[0])>0 and len(bg_sdvig[1])>0):
  for i in range(4):
    for j in range(4):
      check_1_2.append(bg_sdvig[0][i]+bg_sdvig[1][j])

  for i in range(16):
    check_new_1_2.append(round(check_1_2[i][0],7)+round(check_1_2[i][2],7))
    check_new_1_2.append(round(check_1_2[i][1],7)+round(check_1_2[i][3],7))
    
elif (len(bg_sdvig[0])>0 and len(bg_sdvig[2])==0):
    for i in range(4):
      check_1_2.append(bg_sdvig[0][i])
    for i in range(4):
      check_new_1_2.append(round(check_1_2[i][0],7))
  
elif (len(bg_sdvig[0])==0 and len(bg_sdvig[2])>0):
    for i in range(4):
      check_1_2.append(bg_sdvig[2][i])

    for i in range(4):
      check_new_1_2.append(round(check_1_2[i][1],7))  
else: pass

# Первая четверть + четвертая
if (len(bg_sdvig[0])>0 and len(bg_sdvig[3])>0):
  for i in range(4):
    for j in range(4):
      check_1_3.append(bg_sdvig[0][i]+bg_sdvig[3][j])

  for i in range(16):
    check_new_1_3.append(round(check_1_3[i][0],7)+round(check_1_3[i][2],7))
    check_new_1_3.append(round(check_1_3[i][1],7)+round(check_1_3[i][3],7))
    
elif (len(bg_sdvig[0])>0 and len(bg_sdvig[3])==0):
    for i in range(4):
      check_1_3.append(bg_sdvig[0][i])
    for i in range(4):
      check_new_1_3.append(round(check_1_3[i][0],7))
  
elif (len(bg_sdvig[0])==0 and len(bg_sdvig[3])>0):
    for i in range(4):
      check_1_3.append(bg_sdvig[3][i])

    for i in range(4):
      check_new_1_3.append(round(check_1_3[i][1],7))  
else: pass

# ----------------------------------------------------
# Вторая четверть + третья
if (len(bg_sdvig[1])>0 and len(bg_sdvig[2])>0):
  for i in range(4):
    for j in range(4):
      check_2_2.append(bg_sdvig[1][i]+bg_sdvig[2][j])

  for i in range(16):
    check_new_2_2.append(round(check_2_2[i][0],7)+round(check_2_2[i][2],7))
    check_new_2_2.append(round(check_2_2[i][1],7)+round(check_2_2[i][3],7))
    
elif (len(bg_sdvig[1])>0 and len(bg_sdvig[2])==0):
    for i in range(4):
      check_2_2.append(bg_sdvig[1][i])
    for i in range(4):
      check_new_2_2.append(round(check_2_2[i][0],7))
  
elif (len(bg_sdvig[1])==0 and len(bg_sdvig[2])>0):
    for i in range(4):
      check_2_2.append(bg_sdvig[2][i])

    for i in range(4):
      check_new_2_2.append(round(check_2_2[i][1],7))  
else: pass

# Вторая четверть + четвертая
if (len(bg_sdvig[1])>0 and len(bg_sdvig[3])>0):
  for i in range(4):
    for j in range(4):
      check_2_3.append(bg_sdvig[1][i]+bg_sdvig[3][j])

  for i in range(16):
    check_new_2_3.append(round(check_2_3[i][0],7)+round(check_2_3[i][2],7))
    check_new_2_3.append(round(check_2_3[i][1],7)+round(check_2_3[i][3],7))
    
elif (len(bg_sdvig[1])>0 and len(bg_sdvig[3])==0):
    for i in range(4):
      check_2_3.append(bg_sdvig[1][i])
    for i in range(4):
      check_new_2_3.append(round(check_2_3[i][0],7))
  
elif (len(bg_sdvig[1])==0 and len(bg_sdvig[3])>0):
    for i in range(4):
      check_2_3.append(bg_sdvig[3][i])

    for i in range(4):
      check_new_2_3.append(round(check_2_3[i][1],7))  
else: pass
  
# ----------------------------------------------------
# третья четверть + четвертая
if (len(bg_sdvig[2])>0 and len(bg_sdvig[3])>0):
  for i in range(4):
    for j in range(4):
      check_3_3.append(bg_sdvig[2][i]+bg_sdvig[3][j])

  for i in range(16):
    check_new_3_3.append(round(check_3_3[i][0],7)+round(check_3_3[i][2],7))
    check_new_3_3.append(round(check_3_3[i][1],7)+round(check_3_3[i][3],7))
    
elif (len(bg_sdvig[2])>0 and len(bg_sdvig[3])==0):
    for i in range(4):
      check_3_3.append(bg_sdvig[2][i])
    for i in range(4):
      check_new_3_3.append(round(check_3_3[i][0],7))
  
elif (len(bg_sdvig[2])==0 and len(bg_sdvig[3])>0):
    for i in range(4):
      check_3_3.append(bg_sdvig[3][i])

    for i in range(4):
      check_new_3_3.append(round(check_3_3[i][1],7))  
else: pass