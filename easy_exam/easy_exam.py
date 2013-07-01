# -*- coding: utf-8-*-
import random

def randnum(n, zeros=0):
    return random.randint( pow(10,n-1)+1, pow(10, n) -1 ) * pow(10, zeros)

def shizi(num1, num2, op, zeros1=0, zeros2=0):
    #assert eq in [1, 2, '=', '≈']
    assert op in [1, 2, 3, 4, '+', '-', '*', '/']
    op_dic = {1:'+', 2:'-', 3:'*', 4:'/'}
    #eq_dic = {1:'=', 2:'≈'}
    if op in op_dic:
            op = op_dic[op]     
    #if eq in [1, 2]:
    #        eq = eq_dic[eq]
    return str(randnum(num1,zeros1)) + op + str(randnum(num2,zeros2))

def kousuanchengfa(n, eq = '='):
    ''' ( int ) -> list of string

    自动生成形如 '59*8'  或 '3*81' 的两位数乘以一位数的口算乘法习题。
    n代表生成的个数，返回习题列表。
    eq 可以为'=' 或 '≈'，1为'=' ，2为 '≈'。

    '''
    assert type(n) == type(1) and n > 0
    return [ random.choice([shizi(2,1,3),shizi(1,2,3)]) for i in range(n) ]

def bisuanchengfa(kind=0):
    ''' ( int ) -> list of string

    自动生成笔算乘法习题, 返回习题。
    
    kind表示生成的种类：　
    1 ：三位数乘两位数， 如 283 × 81 = 
    2 ：两位数乘三位数， 如 71 × 826 =
    3 ：末尾有0数的乘法， 如 820 × 821=
    4 ：末尾有0数的乘法2， 如 821 × 820=
    5 ：两个数末尾都有0的乘法， 如 140 * 320 =    
    '''
    lst = [1, 2, 3, 4, 5]
    assert kind == 0 or kind in lst

    if kind == 0:
        kind = random.choice(lst)
    if kind == 1:
        return shizi(3, 2, 3)
    elif kind == 2:
        return shizi(2, 3, 3)
    elif kind == 3:
        return shizi(2, 3, 3, 1)
    elif kind == 4:
        return shizi(3, 2, 3, 0, 1)
    elif kind == 5:
        return shizi(2, 2, 3, 1, 1)
 

def bisuanchufa(kind=0):
    ''' ( int, int ) -> list of string

    自动生成笔算除法习题。
    n代表生成的个数，返回习题列表。
    
    kind表示生成的种类：　
    1 ：商是一位数的除法， 如 716 / 91=
    2 ：商是两位数的除法， 如 716 / 51=
    0 ：混合类型
    '''
    lst = [1, 2]
    assert kind == 0 or kind in lst

    if kind == 0:
        return shizi(3, 2, 4)
    while True:
        sz = shizi(3, 2, 4)
        if kind == 1 and eval(sz) < 10:
            return sz
        if kind == 2 and eval(sz) >= 10:
            return sz


def jisuanxiti():
    ''' ( ) -> print

    出一套包含口算、估算、笔算乘法、笔算除法的习题。

    '''
    for i in  kousuanchengfa(12):
        print i,'=','\t',
    for i in range(6):
        print random.choice([shizi(2,3,3), shizi(3,2,3), shizi(2,2,3)]), '≈', '\t',
    for i in [1, 3, 5]:
        print bisuanchengfa(i),'=', '\t',
    for i in [1, 2, 2]:
        print bisuanchufa(i),'=', '\t',

def duzhengshu_help(s):
    ''' ( string ) -> string
    
    输入一个大于0，小于一万的整数（字符串格式输入，前面可以为0），输出其读法

    >>> print duzhengshu_help('0')
    零
    >>> print duzhengshu_help('1234')
    一千二百三十四
    >>> print duzhengshu_help('104')
    一百零四
    >>> print duzhengshu_help('1003')
    一千零三
    >>> print duzhengshu_help('1200')
    一千二百
    >>> print duzhengshu_help('0120')
    零一百二十
    '''
    shu = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    shuwei = ['千', '百', '十','']
    result = ''
    zero_mark = 0
    for i in range(-4, 0):
        if -i <= len(s):
            if s[i] == '0':
                if not zero_mark:
                    result += shu[int(s[i])]
                zero_mark = 1
            else:
                zero_mark = 0
                result += shu[int(s[i])] + shuwei[i]
    result = result.decode('utf-8')
    while result != '零'.decode('utf-8') and result[-1:] == '零'.decode('utf-8'):
        result = result[:-1] 
    return result

def duzhengshu(n):
    ''' ( int ) -> string
    
    输入一个大于0，小于一万亿的整数，输出其读法字符串

    >>> duzhengshu(123456789)
    '''
    assert n >= 0 and n <= 999999999999
    s = str(n)
    #yi, wan, ge = s[-12:-8], s[-8:-4], s[-4:]
    num_dic = {}
    num_dic['亿'] = s[-12:-8]
    num_dic['万'] = s[-8:-4]
    num_dic[''] = s[-4:]

    result = ''
    for i in ['亿', '万', '']:
        if num_dic[i]:
            i_s = duzhengshu_help(num_dic[i])
            result += i_s
            #print i_s, i
            if i_s != '零'.decode('utf-8'):
                result += i.decode('utf-8')

    while result != '零'.decode('utf-8') and result[-1:] == '零'.decode('utf-8'):
        result = result[:-1] 
    temp = result[0]
    for i in range(1,len(result)):
        if result[i] == result[i-1] == '零'.decode('utf-8'):
            continue
        temp += result[i]
    return temp

def randnum2(n, z):
    ''' (int, int) -> int

    随机生成一个n位数，其中有z个0，且第一个数字不为0，返回字符串格式


    '''    
    lst = [0] * z + [ random.randint(1,9) for i in range(n-z)]
    while True:
        random.shuffle(lst)
        if lst[0] != 0:
            result = 0
            for i in lst:
                result = result * 10 + i
            return result

def dushuti(n):
    ''' (int) -> print some text

    打印n个读数题，格式：
    123456789       一亿二千三百四十五万六仟七佰八拾九

    '''
    for i in range(n):
        num = randnum2(random.randint(7,10), random.randint(2,5))
        print num, '\t', duzhengshu(num)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # print duzhengshu(1456789)
    # print duzhengshu(1001234)
    # print duzhengshu(1230034)
    # print duzhengshu(100000034)
    #dushuti(8)
    print u'你好'

