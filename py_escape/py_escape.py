# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 07:27:41 2016

Because Python is so easy, I did the prompt in it as well.

@author: Eric
"""

import re

def escape (s):
    s = re.sub(r'(\\)',r'\\\\',s)
    s = re.sub(r'(<)',r'\<',s)
    s = re.sub(r'(>)',r'\>',s)
    return s
    
s = '<hello> world\\'
print(s)
print(escape(s))
