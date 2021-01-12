from collections import deque

#1. Reversing a String using Stack

class stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container==-1)
    def size(self):
        return len(self.container)
string="Inception"
s=stack()
str=""
for i in string:
    s.push(i)
for i in range(s.size()):
    str+=s.pop()
print(str)

# 2. Checking if the brackets in the string is balanced or not

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size() == 0


"[a+b]*(x+2y)*{gg+kk}"

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
