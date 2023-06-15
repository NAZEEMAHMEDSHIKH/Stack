def stack():
    stack=[]
    return stack

def Isempty(stack):
    return len (stack)==0

def push(stack,item):
    stack.append(item)
    print("pushed item:" +item)

def pop(stack):
    if (Isempty(stack)):
        return "stack is empty"
    return stack.pop()

stack=stack()
push (stack, str(1))
push (stack, str(2))
push (stack, str(3))
push (stack, str(4))
print ("poped item:" +pop(stack))
print ("stack after poping an element:" +str(stack))

