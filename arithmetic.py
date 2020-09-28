import random
from fractions import Fraction

global f

def integer_score():  #生成真分数
    operation = ['+', '-', '*', '/'] #四则运算的符号
    number = random.randint(1,4)     #随机产生的表达式长度
    f = ''
    for i in range(number):
        a = random.randint(1,20)       #随机产生的表达式中的数
        rand = operation[random.randint(0, 3)]     #随机选择一个四则运算中的符号
        if rand == '/':
            b = random.randint(a,20)               #随机产生的真分数的分母
            f += str(a) + rand + str(b)               #数与符号相连
            rand = operation[random.randint(0, 2)]     #随机选择一个四则运算中的符号
            f += rand
        else:
            f += str(a) + rand
        #print(a,rand,end='')
    b = random.randint(1, 20)
    f += str(b)                     #得到完整的表达式
    return f

def respeace():   #转化为真分数
    f1 = integer_score()
    print(f1,'=',end = '')
    n = eval(f1)
    n = Fraction('{}'.format(n)).limit_denominator()    #小数转化为分数
    return n

def proper_fraction():  #真分数混合
    output()
    while(True):
        n = respeace()
        ent = input()
        if ent == 'exit' or ent == 'EXIT':
            break
        else:
            x = Fraction('{}'.format(eval(ent))).limit_denominator()
            if n == x:
                print('回答正确！')
            else:
                print('回答错误！正确答案为：',n)

def newint(fh,n1,n2):    #四则运算
	val = 0                     #结果（值）
	if fh == 0:
		val = n1+n2
	elif fh == 1:
		val = n1-n2
	elif fh == 2:
		val = n1*n2
	elif fh == 3:
		val = int(n1/n2)
	return val           #返回计算结果

def output():   #输出信息
    print('输入exit退出程序')

def main():       #主函数
    print('小学算术题（四则运算）')
    print('请选择：\nA:1-3年级题目\nB:4-6年级题目\nC:真分数混合训练')
    n = 1
    if n==1:
        top = input('请输入A B or C：\n')
        if top == 'A' or top == 'a':
            print('1-3年级训练开始：')
            grade1_3()
        elif top == 'B' or top == 'b':
            print('4-6年级训练开始：如果得到的结果有小数，请四舍五入')
            grade4_6()
        elif top == 'C' or top == 'c':
            print('真分数混合训练开始:若算的结果是小数，请用分数形式表达')
            proper_fraction()

def randomNum(n): #生成随机数
    num = [0,0,0,0,0]
    fh = [0,0,0,0,0]
    for i in range(n):                 #产生随机数
        num[i] = random.randint(1,30)
    for i in range(n-1):               #产生随机符号
        fh[i] = random.randint(0,3)
    return num,fh

def getRandom(n): #1-3年级随机数的获取条件
    randomNumber,randomSymbol = randomNum(n)
    if randomSymbol[0] == 1:  #确保减法不会出现负数
        randomNumber[0],randomNumber[1] = max(randomNumber[0],randomNumber[1]),min(randomNumber[0],randomNumber[1])
    elif randomSymbol[0] == 3:  #确保除法都可以除得尽
        while(randomNumber[0]%randomNumber[1] != 0):
            randomNumber,randomSymbol = randomNum(n)
    return randomNumber,randomSymbol

def outputFormula(n,randomNumber,randomSymbol):  #输出式子
    #randomNumber,randomSymbol = getRandom(n)
    opr = ['+','-','*','/']       #符号
    str_formula = ""
    for i in range(n):                 #输出四则运算式子
        if i < n-1:     
            str_formula += str(randomNumber[i]) + ' ' + opr[randomSymbol[i]] + ' '
        else:
            str_formula += str(randomNumber[i])
    print(str_formula,'=',end='')
    #return randomNumber,randomSymbol

def grade1_3(): #1-3年级题目
    output()
    num = 2
    while(True):
        randomNumber,randomSymbol = getRandom(num) #获取随机数
        outputFormula(num,randomNumber,randomSymbol) #输出式子
        val = newint(randomSymbol[0],randomNumber[0],randomNumber[1])
        ent = input()
        if ent == 'exit' or ent == 'EXIT':
            break
        else:
            answer = eval(ent)
            if answer == val:
                print('你真聪明，做对了哦！')
            else:
                print('很遗憾，你做错了！正确答案为：',val)

def grade4_6(): #4-6年级题目
    output()
    while(True):
        expression = getMedianExpression()
        print(expression,'=',end='')
        ent = input()
        enter = eval(ent)
        val = int(eval(calc(expression)))
        if ent == 'exit':
            break
        else:
            if enter == val:
                print('回答正确！')
            else:
                print('回答错误!正确答案为:',val)

def getMedianExpression():  #生成中值表达式
    n = random.randint(3,5)
    randomNumber,randomSymbol = randomNum(n)
    opr = ['+','-','*','/']
    str_formula = ""
    ct = 0
    nu = 0
    np = 0
    s = 0
    for i in range(n-1):
        if randomSymbol[i] == 2 or randomSymbol[i] == 3:
            s = 1
            break
    if s == 1:
        for i in range(n):                 #输出四则运算式子
            if i < n-1:     
                if (opr[randomSymbol[i]] == '+' and nu == 0) or (opr[randomSymbol[i]] == '-' and nu == 0):
                    str_formula += '(' + str(randomNumber[i]) + opr[randomSymbol[i]]
                    ct = 1
                    nu = 1
                elif (opr[randomSymbol[i]] == '*' and np == 0) or (opr[randomSymbol[i]] == '/' and np == 0):
                    if ct == 1:
                        str_formula += str(randomNumber[i]) + ')' + opr[randomSymbol[i]]
                        ct = 0
                        np = 1
                    else:
                        str_formula += str(randomNumber[i]) + opr[randomSymbol[i]]
                else:
                    str_formula += str(randomNumber[i]) + opr[randomSymbol[i]]
            else:
                if (opr[randomSymbol[i-1]] == '+'and np==0) or (opr[randomSymbol[i-1]] == '-' and np == 0):
                    str_formula += str(randomNumber[i]) + ')'
                elif opr[randomSymbol[i-1]] == '*' or opr[randomSymbol[i-1]] == '/':
                    str_formula += str(randomNumber[i])
                else:
                    str_formula += str(randomNumber[i]) 
        #print(str_formula)
    else:
        for i in range(n):
            if i < n-1:
                str_formula += str(randomNumber[i]) + opr[randomSymbol[i]]
            else:
                str_formula += str(randomNumber[i])
        #print(str_formula)
    
    return str_formula

def calcRevPolishNotation(numList = []):#中缀表达式转后缀表达式步骤
    '''
    1.遇到操作数：添加到后缀表达式中或直接输出
    2.栈空时：遇到运算符，直接入栈
    3.遇到左括号：将其入栈
    4.遇到右括号：执行出栈操作，输出到后缀表达式，直到弹出的是左括号（注意：左括号不输出到后缀表达式）
    5.遇到其他运算符：弹出所有优先级大于或等于该运算符的栈顶元素，然后将该运算符入栈
    6.将栈中剩余内容依次弹出后缀表达式
    '''

    zhan = []
    i = 0
    while i < len(numList):
        re = 0
        if(numList[i].isdigit()):
            zhan.append(numList[i])        # 执行第1步
        else:
            a = float(zhan.pop())          # 执行第2步
            b = float(zhan.pop())
            if(numList[i] == '+'):
                re = b + a
            elif(numList[i] == '-'):
                re = b - a
            elif (numList[i] == '*'):
                re = b * a
            elif (numList[i] == '/'):
                re = b / a
            zhan.append(str(re))
        i += 1
    return zhan.pop()                      # 执行第3步

def zhongToList(str = ''): #中缀表达式字符串转换为列表
    i = 0
    numStr = ''
    flag = False
    numList = []
    while i < len(str):
        if(str[i].isdigit()):
            numStr += str[i]
            flag = True
        else:
            if(flag):
                numList.append(numStr)
                numStr = ''
                flag = False
            numList.append(str[i])
        i += 1
    if(flag):
        numList.append(numStr)
    return numList

def listToHou(numList = []):#中缀表达式转后缀表达式，所有表达式都是列表存储的
    level = {'(':0, '+':1, '-':1, '*':2, '/':2}
    stack = []
    RevPolishNotation = []
    i = 0
    while i < len(numList):
        if(numList[i].isdigit()):
            RevPolishNotation.append(numList[i])        # 执行第1步
        else:
            if(len(stack) == 0 or numList[i] == '('):
                stack.append(numList[i])                # 执行第2，3步
            elif(numList[i] == ')'):
                while True:                             # 执行第4步
                    out = stack.pop()
                    if(out != '('):
                        RevPolishNotation.append(out)
                    else:
                        break
            else:
                while True:                             # 执行第5步
                    if(len(stack) != 0 and level[stack[-1]] >= level[numList[i]]):
                        out = stack.pop()
                        RevPolishNotation.append(out)
                    else:
                        stack.append(numList[i])
                        break
        i += 1
    while True:                                         # 执行第六步
        if(len(stack) != 0):
            out = stack.pop()
            RevPolishNotation.append(out)
        else:
            break
    return RevPolishNotation

def calc(str = ''):#中缀表达式求值
    return calcRevPolishNotation(listToHou(zhongToList(str)))

if __name__ == "__main__":
    main()