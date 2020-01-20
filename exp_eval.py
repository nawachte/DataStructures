#
#Name: Nicholas Wachter
#Student ID: 016170774
#Date (last modified): 4/23/19
#
# Lab 11
# Section 12
# Purpose of Lab: to use practice using stacks through modifying prefix and infix equations
# and solving postfix equations

from stack_array import Stack
import sys

class PostfixFormatException(Exception):
    pass

#int int str -> int
#do math takes two numbers and an operator(formatted as a string) and performs the operations
#of the string formatted operator
def doMath(num1, num2, op):
    if op == '+':
        return num1+num2
    if op == '-':
        return num2-num1
    if op == '*':
        return num1*num2
    if op == '/':
        if num1 == 0:
            raise ValueError
        return num2/num1
    if op == '**':
        return num2**num1
    try:
        if op == '>>':
            return num2 >> num1
        if op == '<<':
            return num2 << num1
    except:
        raise PostfixFormatException('Illegal bit shift operand')

#str -> int
#takes an equation as a string. test if it is valid. for every character if it is an num add it to the stack
#if it is an operator perform the operation with the top two numbers in the stack. return the final number
#in the stack when the end of the string is reached
def postfix_eval(input_str):
    inputList = input_str.split()
    postStack = Stack(30)
    for character in inputList:
        try:
            float(character)
        except:
            if character not in ['<<','>>','**','*','/','+','-']:
                raise PostfixFormatException("Invalid token")
            else:
                pass
    for item in inputList:
        try:
            postStack.push(int(item))
        except ValueError:
            try:
                postStack.push(float(item))
            except:
                if postStack.size() >= 2:
                    postStack.push(doMath(postStack.pop(),postStack.pop(),item))
                else:
                    raise PostfixFormatException('Insufficient operands')
    if postStack.size() != 1:
        raise PostfixFormatException("Too many operands")
    return postStack.pop()

#print(postfix_eval('6 3 + 7 3 * - 2 +'))

#str str -> bool
#checkPrec takes two operators and returns False if the first one has precidence and returns
#True if the second one has precidence
def checkPrec(o1, o2):
    o1prec = 0
    o2prec = 0
    if o2 == '<<' or o2 == '>>':
        o1prec = 1
    if o1 == '<<' or o1 == '>>':
        o1prec = 1
    if o2 == '**':
        o2prec = 2
    if o1 == '**':
        o1prec = 2
    if o2 == '*' or o2 == '/':
        o2prec = 3
    if o1 == '*' or o1 == '/':
        o1prec = 3
    if o2 == '+' or o2 == '-':
        o2prec = 4
    if o1 == '+' or o1 == '-':
        o1prec = 4
    if o1!= '**':
        if o2prec >= o1prec:
            return True
    else:
        if o2prec > o1prec:
            return True
    return False

#str -> str
#takes an equation as a string. if it is a number add it to the return string if it is an open parenthesis
#add it to the stack if it is closed then add all the items in the stack to the string until you reach the
#open parenthesis. remove it. if it is an operator check the precidence with the last added op to the stack
#and add whichever has precidence at the end of the string return all ops in the stack to the string
#return the string
def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""
    inputList = input_str.split()
    rpnString = ''
    infixStack = Stack(30)
    for item in inputList:
        try:
            if item.isdigit() == True:
                num = int(item)
            else:
                num = float(item)
            rpnString += item + ' '
        except:
            if item == '(':
                infixStack.push(item)
            elif item == ')':
                while infixStack.peek() != '(':
                    rpnString += infixStack.pop() + ' '
                infixStack.pop()
            else:
                if infixStack.size() > 0:
                    o1 = item
                    o2 = infixStack.peek()
                    if checkPrec(o1,o2) == False and o2!='(':
                        rpnString += item + ' '+infixStack.pop() + ' '
                    else:
                        rpnString += infixStack.pop() + ' '
                        infixStack.push(item)
                else:
                    infixStack.push(item)
    for i in range(infixStack.size()):
        rpnString += infixStack.pop() + ' '
    rpnString = rpnString[:-1]
    return rpnString

#print(infix_to_postfix('1 + 2 * 3 - 4'))

#str -> str
#take equation as a string for each item in the string if it is a number push it on to the stack
#for operators concatenate the top two values(equations or nums) from the stack and the operator and
#concatenate that to the returnString at the end return the return string
def prefix_to_postfix(input_str):
    inputList = input_str.split()
    inputList = inputList[::-1]
    prefixStack = Stack(30)
    for item in inputList:
        try:
            prefixStack.push(int(item))
        except:
            try:
                prefixStack.push(float(item))
            except:
                op1 = str(prefixStack.pop())
                op2 = str(prefixStack.pop())
                if op1[-1] == ' ':
                    op1 = op1[:-1]
                if op2[-1] == ' ':
                    op2 = op2[:-1]
                opString = op1 + ' ' + op2 + ' ' + str(item) + ' '
                prefixStack.push(opString)
    returnString = str(prefixStack.pop())
    if returnString[-1] == ' ':
        returnString = returnString[:-1]
    return returnString


#################################

def getPrecVal(op):
    precVal = 0
    if op in ['<<','>>']:
        precVal = 4
    if op == '**':
        preVal = 3
    if op in ['*','/']:
        precVal = 2
    if op in ['+','-']:
        precVal = 1
    return precVal

def testInfix(inputString):
    inputList = inputString.split()
    rpnString = ''
    infixStack = Stack(30)
    for item in inputList:
        if item.isdigit():
            rpnString += item
        else:
            try:
                rpnString += str(float(item))
            except:
                pass
        if infixStack.size() > 0:
            o1 = item
            o2 = infixStack.peek()
            if o1 != '**':
                if getPrecVal(o1) <= getPrecVal(o2) and infixStack.size() > 0:
                    rpnString += infixStack.pop()
            elif o1 == '**':
                if getPrecVal(o1) < getPrecVal(o2) and infixStack.size() > 0:
                    rpnString += infixStack.pop()
            infixStack.push(item)
    for i in range(infixStack.size()):
        rpnString += infixStack.pop()
    return rpnString

print(testInfix('1 + 2 * 3 - 4'))