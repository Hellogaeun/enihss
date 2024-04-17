# 약 20문제 괄호넣기 객관식, 단답형


#python을 이용한 gui 코딩 -> 아래 세 줄이 무조건 필요 !

"""from tkinter import*

window = Tk()

window.mainloop()



from tkinter import*

window = Tk() #불러오기
window.title("윈도창 연습") #창이름
window.geomerty("400x100") #사이즈
window.resizable(width= TRUE, height= TRUE) #사이즈 FALSE = 고정, TRUE = 조절

window.mainloop()"""


"""from tkinter import*
window = Tk()

label1 = Label(window, text = "오늘 저녁 메뉴는 ~~~~")
label2 = Label(window, text = "맛있는", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "만 만 닭 강 정", bg = "yellow", width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()"""


"""from tkinter import*
window = Tk()

photo1 = PhotoImage(file = "cinnamoroll.gif")
label1 = Label(window, image = photo1)

photo2 = PhotoImage(file = "mymelody.gif")
label2 = Label(window, image = photo2)

label1.pack()
label2.pack()

window.mainloop()"""



"""from tkinter import*
window = Tk()

button1 = Button(window, text="파이썬 종료", fg = "red", command = quit)

button1.pack()

window.mainloop()"""



"""from tkinter import*
from tkinter import messagebox

# 함수 선언
def myFunc() :
    messagebox.showinfo("시나모롤 버튼", "시나모롤 짱 귀엽죠? ^^")
    
# 메인 코드
window = Tk()

photo = PhotoImage(file = "cinnamoroll.gif")
button1 = Button(window, image=photo, command = myFunc)
# 이미지를 누르면 함수 실행 명렁 코드 !

button1.pack()

window.mainloop()"""



"""from tkinter import*
from tkinter import messagebox
window = Tk()

def myFunc():
    if chk.get()==0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("","체크버튼이 켜졌어요.")

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()"""
