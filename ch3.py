from math import *

def start(Modul):

  f = [pi/4, pi/5, pi/6 ,pi/8, pi/9 ,pi/10, pi/12]

  # Список выбранных сдвигов
  a_f = []
  
  for i in range(4):
    
    a_f.append(int(Modul[i])-1)

  A = []
  for i in range(6):
    A.append(2*cos(f[i]-pi/4))

  A_ = []
  for i in range(6):
    A_.append(2*cos(-f[i]-pi/4))

  A_sqrt = sqrt(2)
  bg_sdvig, bg_sdvig_check = [], []
  sdvig = [0, pi/2, pi, 3*pi/2]

  # Списки для хранения даннных
  check_1_2_3, check_1_2_4, check_1_3_4, check_2_3_4 = [], [], [], []
  check_new_1_2_3, check_new_1_2_4, check_new_1_3_4, check_new_2_3_4 = [], [], [], []

  for i in range(4):
    if a_f[i]!=-1:
      bg = [[A_sqrt*(cos(f[a_f[i]]+pi/4+sdvig[i])), A_sqrt*(sin(f[a_f[i]]+pi/4+sdvig[i]))],
            [A[a_f[i]]*(cos(pi/4+sdvig[i])), A[a_f[i]]*(sin(pi/4+sdvig[i]))],
            [A_[a_f[i]]*(cos(pi/4+sdvig[i])), A_[a_f[i]]*(sin(pi/4+sdvig[i]))],
            [A_sqrt*(cos(-f[a_f[i]]+pi/4+sdvig[i])), A_sqrt*(sin(-f[a_f[i]]+pi/4+sdvig[i]))]]
      bg_sdvig.append(bg)
      
    elif a_f[i]==-1:
      bg_sdvig.append([])

  # Первая четверть + вторая + третья
  if (len(bg_sdvig[0])>0 and len(bg_sdvig[1])>0 and len(bg_sdvig[2])>0):
    for i in range(4):
      for j in range(4):
        for k in range(4):
          check_1_2_3.append(bg_sdvig[0][i]+bg_sdvig[1][j]+bg_sdvig[2][k])

    for i in range(64):
      check_new_1_2_3.append(round(check_1_2_3[i][0],7)+round(check_1_2_3[i][2],7)+round(check_1_2_3[i][4],7))
      check_new_1_2_3.append(round(check_1_2_3[i][1],7)+round(check_1_2_3[i][3],7)+round(check_1_2_3[i][5],7))
  else: pass

  # Первая четверть + вторая + четвертая
  if (len(bg_sdvig[0])>0 and len(bg_sdvig[1])>0 and len(bg_sdvig[3])>0):
    for i in range(4):
      for j in range(4):
        for k in range(4):
          check_1_2_4.append(bg_sdvig[0][i]+bg_sdvig[1][j]+bg_sdvig[3][k])

    for i in range(64):
      check_new_1_2_4.append(round(check_1_2_4[i][0],7)+round(check_1_2_4[i][2],7)+round(check_1_2_4[i][4],7))
      check_new_1_2_4.append(round(check_1_2_4[i][1],7)+round(check_1_2_4[i][3],7)+round(check_1_2_4[i][5],7))
  else: pass

  # Первая четверть + третья + четвертая
  if (len(bg_sdvig[0])>0 and len(bg_sdvig[2])>0 and len(bg_sdvig[3])>0):
    for i in range(4):
      for j in range(4):
        for k in range(4):
          check_1_3_4.append(bg_sdvig[0][i]+bg_sdvig[2][j]+bg_sdvig[3][k])

    for i in range(64):
      check_new_1_3_4.append(round(check_1_3_4[i][0],7)+round(check_1_3_4[i][2],7)+round(check_1_3_4[i][4],7))
      check_new_1_3_4.append(round(check_1_3_4[i][1],7)+round(check_1_3_4[i][3],7)+round(check_1_3_4[i][5],7))
  else: pass

  # Вторая четверть + третья + четвертая
  if (len(bg_sdvig[1])>0 and len(bg_sdvig[2])>0 and len(bg_sdvig[3])>0):
    for i in range(4):
      for j in range(4):
        for k in range(4):
          check_2_3_4.append(bg_sdvig[1][i]+bg_sdvig[2][j]+bg_sdvig[3][k])

    for i in range(64):
      check_new_2_3_4.append(round(check_2_3_4[i][0],7)+round(check_2_3_4[i][2],7)+round(check_2_3_4[i][4],7))
      check_new_2_3_4.append(round(check_2_3_4[i][1],7)+round(check_2_3_4[i][3],7)+round(check_2_3_4[i][5],7))
  else: pass
  
  return bg_sdvig, check_new_1_2_3, check_new_1_2_4, check_new_1_3_4, check_new_2_3_4, a_f