import tkinter
import math
root = tkinter.Tk()
root.minsize(320,350)
steplist=[]
numberornot=1
highornot=0
#显示数字
num=tkinter.StringVar()
num.set('')

#显示结果

label=tkinter.Label(root,textvariable= num, bg='white',font=('黑体',20),anchor='e')
label.place(x=10,y=10,width=300,height=30)


#按钮操作

#数字
def pressnum(no):
    global numberornot
    global highornot
    highornot = 0
    numberornot=1
    oldno=num.get()
    if oldno.isdigit():
       if oldno=='0':
        num.set(no)
       else:
        num.set(oldno+no)
    else:
        num.set(no)

#high
def presshigh(sym1,sym2):
    global numberornot
    global steplist
    if numberornot==1:
        steplist.append(num.get())
    steplist.append(sym1)
    num.set(sym2)

    print(steplist)

#pi
def presspi():
    global numberornot
    global highornot
    if numberornot == 1:
        numberornot=0
        num.set('pi')
        steplist.append(str(math.pi))

#运算

def presscal(sym1,sym2):
    global numberornot
    global steplist
    if numberornot==1 :
        numberornot = 0

        steplist.append(num.get())
        steplist.append(sym1)
        num.set(sym2)


    print(steplist)


#等于
def pressequ():
    global numberornot
    global highornot
    highornot = 0
    if numberornot==1:
        numberornot = 0
        global steplist
        steplist.append(num.get())
        for i in range(len(steplist)):
            if steplist[i] == 'pi':
                steplist[i] = ''
        for b in range(len(steplist)):
            if steplist[b] == 'sin':
                steplist[b + 1] = str(math.sin(float(steplist[b + 1])))
                steplist[b] = ''
            elif steplist[b] == 'cos':
                steplist[b + 1] = str(math.cos(float(steplist[b + 1])))
                steplist[b] = ''
            elif steplist[b] == 'exp':
                steplist[b + 1] = str(math.exp(float(steplist[b + 1])))
                steplist[b] = ''
            elif steplist[b] == 'ln':
                steplist[b + 1] = str(math.log(float(steplist[b + 1])))
                steplist[b] = ''
        print(steplist)
        result = eval(''.join(steplist))

        num.set(result)
        steplist = []


#归零

def presszero():
    global steplist
    global highornot
    highornot = 0
    num.set(0)
    steplist=[]



#撤回

def presswith():
    global steplist
    global numberornot
    global highornot
    highornot = 0
    num.set(num.get()[:-1])
    if numberornot==0:
        steplist.pop()
        if steplist[-1].isdigit():
            numberornot=1


#按钮
btn7=tkinter.Button(root,text='7',command= lambda : pressnum('7'))
btn7.place(x=10,y=50,width=50,height=50)

btn8=tkinter.Button(root,text='8',command= lambda : pressnum('8'))
btn8.place(x=60,y=50,width=50,height=50)

btn9=tkinter.Button(root,text='9',command= lambda : pressnum('9'))
btn9.place(x=110,y=50,width=50,height=50)

btn4=tkinter.Button(root,text='4',command= lambda : pressnum('4'))
btn4.place(x=10,y=100,width=50,height=50)

btn5=tkinter.Button(root,text='5',command= lambda : pressnum('5'))
btn5.place(x=60,y=100,width=50,height=50)

btn6=tkinter.Button(root,text='6',command= lambda : pressnum('6'))
btn6.place(x=110,y=100,width=50,height=50)

btn1=tkinter.Button(root,text='1',command= lambda : pressnum('1'))
btn1.place(x=10,y=150,width=50,height=50)

btn2=tkinter.Button(root,text='2',command= lambda : pressnum('2'))
btn2.place(x=60,y=150,width=50,height=50)

btn3=tkinter.Button(root,text='3',command= lambda : pressnum('3'))
btn3.place(x=110,y=150,width=50,height=50)

btnadd=tkinter.Button(root,text='+',command= lambda : presscal('+','+'))
btnadd.place(x=160,y=50,width=50,height=100)

btnsub=tkinter.Button(root,text='-',command= lambda : presscal('-','-'))
btnsub.place(x=210,y=50,width=50,height=100)

btnmul=tkinter.Button(root,text='x',command= lambda : presscal('*','x'))
btnmul.place(x=160,y=150,width=50,height=100)

btndiv=tkinter.Button(root,text='÷',command= lambda : presscal('/','÷'))
btndiv.place(x=210,y=150,width=50,height=100)

btnzero=tkinter.Button(root,text='归零',command= presszero)
btnzero.place(x=260,y=150,width=50,height=100)

btn0=tkinter.Button(root,text='0',command= lambda : pressnum('0'))
btn0.place(x=10,y=200,width=100,height=50)

btnequ=tkinter.Button(root,text='=',command = pressequ)
btnequ.place(x=110,y=200,width=50,height=50)

btnwit=tkinter.Button(root,text='←',command= presswith)
btnwit.place(x=260,y=50,width=50,height=100)

btnsin=tkinter.Button(root,text='sin',command= lambda : presshigh('sin','sin'))
btnsin.place(x=160,y=250,width=50,height=50)

btncos=tkinter.Button(root,text='cos',command= lambda : presshigh('cos','cos'))
btncos.place(x=210,y=250,width=50,height=50)

btnexp=tkinter.Button(root,text='exp',command= lambda : presshigh('exp','exp'))
btnexp.place(x=110,y=250,width=50,height=50)

btnln=tkinter.Button(root,text='ln',command= lambda : presshigh('ln','ln'))
btnln.place(x=60,y=250,width=50,height=50)

btnpi=tkinter.Button(root,text='π',command=presspi)
btnpi.place(x=10,y=250,width=50,height=50)

root.mainloop()
