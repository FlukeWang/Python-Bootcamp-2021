# GUI Translater.py

from tkinter import * 
# จาก librayชื่อ tkinter, * คือ ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk # ttk is theme of ttk
# * is already import all but what is tkk
# * is import only main file


#---------Google Translate------------
from googletrans import Translator
translator = Translator() # สร้างฟังชั่นแปลภาษา

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry ('500x300') #กว้าง x สูง 
GUI.title('Translator by Fluke Wang')

#---------Config------------
FONT = ('Arial',20)

#---------Label------------
L = ttk.Label(GUI,text='Input Your Vocab',font=FONT)
L.pack() # .pack show จากบนลงล่าง

#---------Entry(Vocab)------------
v_vocab = StringVar() #กล่องเก็บข้อความ
E1 = ttk.Entry(GUI, textvariable = v_vocab,font=FONT,width=50)
E1.pack(pady=20) # pady = ห่างแนว y 


# ------Button(translate)---------
def Translate() :
    vocab = v_vocab.get() # .get คือให้แสดงผลออกมา
    #คำสั่งเปิดกล่อง v_vocab
    meaning = translator.translate(vocab,dest='zh-tw') # dest(ination) จุดหมายปลายทางภาษาที่เราจะแปล
    print(vocab + ':' + meaning.text)
    print( meaning.pronunciation)
    v_result.set(vocab + ':' + meaning.text) # สั่งโชว์ใน GUI 
    
B1 = ttk.Button(GUI, text = 'Translate',command=Translate) # ttk=theme 
#สร้างปุ่มขึ้นมา, GUI หมายถึง หน้าต่างหลัก (code ข้างบน)
B1.pack (ipadx=20,ipady=10)# show ปุ่มขึ้นมา วางจากบนลงล่าง
#ipadx = internal pading แนวแกน x หน่วย pixel

#---------Label------------
L = ttk.Label(GUI,text='Meaning',font=FONT)
L.pack() # .pack show จากบนลงล่าง

#---------Result------------
v_result = StringVar() #กล่องเก็บคำแปล
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT,foreground='blue')
# in Label we don't use color we use foreground
# textvariable means ข้อความที่เปลี่ยนแปลงได้ตลอด
R1.pack()




GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด #บรรทัดสุดท้ายเท่านั้น

