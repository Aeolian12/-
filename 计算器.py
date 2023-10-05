import tkinter
root = tkinter.Tk()
root.minsize(300,300)
steplist=[]

#显示数字
num=tkinter.StringVar()
num.set('0')

#显示结果

label=tkinter.Label(root,textvariable= num, bg='white',font=('黑体',20),anchor='e')
label.place(x=10,y=10,width=280,height=30)


#按钮操作

#数字
def pressnum(no):
    oldno=num.get()
    if no.isdigit() and oldno.isdigit():
       if oldno=='0':
        num.set(no)
       else:
        num.set(oldno+no)
    else:
        num.set(no)


#运算

def presscal(sym1,sym2):
    global steplist
    steplist.append(num.get())
    steplist.append(sym1)
    num.set(sym2)


#等于
def pressequ():
    global steplist
    steplist.append(num.get())
    result=eval(''.join(steplist))

    num.set(result)
    steplist=[]

#归零

def presszero():
    num.set(0)
    steplist=[]


#撤回

def presswith():
    global steplist
    num.set(num.get()[:-1])

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



root.mainloop()
