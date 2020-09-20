import random
from fractions import Fraction

def newint(fh,n1,n2):    #四则运算
	# opr = ['+','-','*','/']     #设定运算符号
	#fh = random.randint(0,3)    #选择符号
	val = 0                     #结果（值）
	if fh == 0:
		val = n1+n2
	elif fh == 1:
		#n1,n2 = max(n1,n2),min(n1,n2)
		val = n1-n2
	elif fh == 2:
		val = n1*n2
	elif fh == 3:
		val = int(n1/n2)
	#print(n1,opr[fh],n2)
	return val

def newfra():     #真分数四则运算
    opr = ['+', '-', '*', '/']
    fh = random.randint(0, 3)    #随机选择符号
    t1 = random.randint(1, 10)   #生成1-10之间的随机数
    t2 = random.randint(t1, 10)  #生成t1-10之间的随机数
    n1 = Fraction(t1, t2)        #生成一个真分数
    t1 = random.randint(1, 10)
    t2 = random.randint(t1, 10)
    n2 = Fraction(t1, t2)
    val = 0
    if fh == 0:
        val = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        val = n1 - n2
    elif fh == 2:
        val = n1 * n2
    elif fh == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        val = n1 / n2
    print(n1, opr[fh], n2, '= ', end='')
    print('')
    return val

def main():       #主函数
    print('小学算术题（四则运算）')
    n = 1
    if n==1:
        print('input "0000" to Quit')
        while True:
            fh = random.randint(0, 4)
            if fh == 0:
                print('真分数运算：')
                rjg = newfra()
                jg = input()
                if jg == '0000':
                    break;
                sr = Fraction(jg)
                if sr == rjg:
                    print('right')
                else:
                    print('error. the Tight answer is', rjg)
                print('')
            else:
                print('整数运算')
                rjg = suanfa()
                jg = input()
                if jg == '0000':
                    break;
                sr = int(jg)
                if sr == rjg:
                    print('right')
                else:
                    print('error. the Tight answer is', rjg)
                print('')

#调试
def suanfa():
    n = random.randint(2,5)
    # print('随机生成个数：',n)
    num = [0,0,0,0,0]
    fh = [0,0,0,0,0]
    opr = ['+','-','*','/']
    count = 0
    val = 0                            #值

    for i in range(n):                 #产生随机数
        num[i] = random.randint(1,10)

    for i in range(n-1):               #产生随机符号
        fh[i] = random.randint(0,3)

    for i in range(n):                 #除法不出现小数
        #print(opr[fh[i]])
        if i < n-1:
            #if fh[i] == 1:
                #num[i],num[i+1] = max(num[i],num[i+1]),min(num[i],num[i+1])
            if fh[i] == 3:
                num[i],num[i+1] = max(num[i],num[i+1]),min(num[i],num[i+1])
                while (num[i]%num[i+1] != 0):
                    #num[i] = random.randint(1,10)
                    num[i+1] = random.randint(1,10)
                    #print("numlen", len(num) , " " , i+1)
                    num[i],num[i+1] = max(num[i],num[i+1]),min(num[i],num[i+1])

    str_formula = ""
    for i in range(n):                 #输出四则运算式子
        if i < n-1:     
            str_formula += str(num[i]) + opr[fh[i]]
        else:
            str_formula += str(num[i]) + '='
    print(str_formula)
    
    i = 0
    p = 0
    while(p<n-1):    #乘除法
        #print('i=',i)
        p = p+1
        if fh[i] == 2 or fh[i] == 3:
            num[i] = newint(fh[i],num[i],num[i+1])
            #print('i=',i,'num[i]=',num[i])
            del num[i+1]
            del fh[i]
            #print(i,num[i+1])
            count+=1
            i = i-1
            #print('i=',i+1, 'p', p,'num[i]=',num[i+1], str(num))
        i=i+1
        #print('p=',p)

    n = n-count
    # print('')
    val = newint(fh[0],num[0],num[1])
    for i in range(n-2):   #加减法
        # print(val,opr[fh[i+1]],num[i+2])
        val = newint(fh[i+1],val,num[i+2])
        # print(val)

    #print('值：', int(eval(str_formula)))
    #print('值：', val)
    return val

if __name__ == '__main__':
    main()
    