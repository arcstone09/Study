from LinkedStack import LinkedStack

def postfixCalculator(p):
    stack = LinkedStack()
    flag = False
    for i in p:
        if isOperator(i):
            stack.push(operation(stack.pop(), stack.pop(), i))
            flag = False
        elif i.isdigit() :
            curr_num = ord(i) - ord('0')
            if flag:  
                stack.push(curr_num + 10 * stack.pop())
            else :
                stack.push(curr_num)
            flag = True
        else :
            flag = False
    
    return stack.top()

def isOperator(ch):
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(opr2:int, opr1:int, ch):
    return {'+': opr1 + opr2, '-': opr1 - opr2, '*':opr1 * opr2, '/': opr1 // opr2}[ch]

postfix = '700 3 47 + 6 * - 4 /'
print(postfixCalculator(postfix))

