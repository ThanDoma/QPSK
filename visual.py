from tkinter import *
from tkinter import ttk
import checking_prohibited_comb_ch2 as cp_2
import checking_prohibited_comb_ch3 as cp_3
import System_for_2ch as sch2
import System_for_3ch as sch3
import ch2
import ch3

import numpy as np

class Example(Frame):
 
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("")
        self.pack(fill=BOTH, expand=1)
        global lbl
        lbl = Label(root, width = 100, text="")
        lbl.pack()
        super().__init__()
        self.initUI()
        
    

    def initUI(self):
      frame = Frame(
      root,
      padx = 10,
      pady = 10
      )
      
      frame.pack(fill=BOTH, expand=True)
      
      height_lb = Label(
      frame,
      text="Введите количество каналов"
      )
      height_lb.grid(row=3, column=1)
      
      weight_lb = Label(
      frame,
      text="Введите индексы модуляции",
      )
      weight_lb.grid(row=4, column=1)
      
      weight_lb = Label(
      frame,
      text="Макс. допустимое растояние",
      )
      weight_lb.grid(row=5, column=1)
      
      Channels = Entry(
      frame,
      )
      Channels.grid(row=3, column=2)
      
      Mi = Entry(
      frame,
      )
      Mi.grid(row=4, column=2, pady=5)
      
      Distance = Entry(
      frame,
      )
      Distance.grid(row=5, column=2)
      
      self.pack(fill=BOTH, expand=True)
      
      def caption(event):
            Ch = int(Channels.get())
            Modul = list(Mi.get())
            
            global bg_sdvig, a_f, dist
            
            if int(Ch)==2:
                
              global check_new_1_2, check_new_1_3, check_new_1_4, check_new_2_3, check_new_2_4, check_new_3_4
              bg_sdvig, check_new_1_2, check_new_1_3, check_new_1_4, check_new_2_3, check_new_2_4, check_new_3_4, a_f = ch2.start(Modul)
              dist = float(Distance.get())
              
              new_quarter_1_2, new_quarter_1_3, new_quarter_1_4, new_quarter_2_3, new_quarter_2_4, new_quarter_3_4 = cp_2.check(check_new_1_2, check_new_1_3, check_new_1_4, check_new_2_3, check_new_2_4, check_new_3_4, dist)
              
              sch2.final(new_quarter_1_2, new_quarter_1_3, new_quarter_1_4, new_quarter_2_3, new_quarter_2_4, new_quarter_3_4, bg_sdvig, a_f)
              
            elif int(Ch)==3:
              global check_new_1_2_3, check_new_1_2_4, check_new_1_3_4, check_new_2_3_4
              
              bg_sdvig, check_new_1_2_3, check_new_1_2_4, check_new_1_3_4, check_new_2_3_4, a_f = ch3.start(Modul)
              
              dist = float(Distance.get())
              
              new_quarter_1_2_3, new_quarter_1_3_4, new_quarter_1_2_4, new_quarter_2_3_4 = cp_3.check(check_new_1_2_3, check_new_1_2_4, check_new_1_3_4, check_new_2_3_4, dist)
              
              sch3.final(new_quarter_1_2_3, new_quarter_1_3_4, new_quarter_1_2_4, new_quarter_2_3_4, bg_sdvig, a_f)
              
      root.bind('<Control-z>', exit_)
      Channels.bind('<Return>', caption)
      Mi.bind('<Return>', caption)
      Distance.bind('<Return>', caption)
      
def exit_(event):
        root.destroy()

def main():
  global root
  root = Tk()
  root.geometry('400x300')
  ex = Example(root)
  root.bind('<Control-z>', exit_)
  root.mainloop()

if __name__ == '__main__':
    main()