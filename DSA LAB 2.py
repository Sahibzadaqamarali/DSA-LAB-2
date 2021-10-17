#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Qamar ali
#200901107
#CS-01-B

#IMPORTING DEQUE
from collections import deque
class balanced:
    stack=[]
    def _init_(self):
        self.stack=deque()
    def push(self,paren):
        self.stack.append(paren)
    def pop(self):
        return self.stack.pop()
    
#FUNCTION FOR CHECKING EQUATION     
    def check_balanced(self,equation):   
        for paren in equation:
            if paren in ["(","{","["]:
                self.push(paren)
            else:
                if not self.stack: 
                    return False 
                parenthesis=self.pop()
                if parenthesis=="(":
                    if paren!=")":
                        return False
                if parenthesis=="{":
                    if paren!="}":
                        return False
                if parenthesis=="[":
                    if paren!="]":
                        return False
        if self.stack:
            return False
        return True
b=balanced()
#Taking user inputs
paren=input("Enter equation: ")
if b.check_balanced(paren):
#Giving Output
        print(paren,"- Equation is  Balanced")
else:
        print(paren,"- Equation is  Unbalanced")


# In[ ]:





# In[ ]:




