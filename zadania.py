# coding: utf-8
def total(*arg):
    lst = list(*arg)
    return sum(lst)
    
total((5,6.9))
total((5,6,9))
total([1,2,3,4,5])
total(range(2,7))
def scale(n,lst):
    return n*lst
    
scale(2,[1,2,3,4])
def scale(n,lst):
    out=[]
    for e in lst:
        out.append(n*e)
    return out
    
    
scale(2,[2,3,4,5])
def normalize(*args):
    lst = list(*args)
    s = sum(lst)
    out = []
    for e in lst:
        out.append(e/s)
    return out
    
normalize([1])
def normalize(*args):
    lst = list(*args)
    s = sum(lst)
    out = []
    for e in lst:
        out.append(100*e/s)
    return out
    
normalize([1])
normalize([1,2,3,4])
result = normalize([1,2,3,4])
sum(result)
def magnitude(x,y):
    return(sqrt(x**2+y**2))
    
    
    
    
magnitude(3,4)
def magnitude(x,y):
    import math
    return(sqrt(x**2+y**2))
    
    
    
    
magnitude(3,4)
import math
sqrt(4)
def magnitude(x,y):
    return((x**2+y**2)**0.5)
    
    
    
    
    
magnitude(3,4)
def dot_product(vec1,vec2):
    return vec1*vec2
    
vec1=[1,2,3]
vec2=[4,5,6]
dot_product(vec1,vec2)
def dot_product(vec1,vec2):
    vec1 = list(vec1)
    vec2 = lisst(vec2)
    return vec1*vec2
    
def dot_product(vec1,vec2):
    vec1 = list(vec1)
    vec2 = list(vec2)
    return vec1*vec2
    
dot_product(vec1,vec2)
def dot_product(vec1,vec2):
    vec1 = list(vec1)
    vec2 = list(vec2)
    for e in range(len(vec1)):
        out = vec1[e]*vec2[e]
    return out
    
    
dot_magnitue(vec1,vec2)
vec1
vec1=[1,2,3]
vec2 = [4,5,6]
def dot_product(vec1,vec2):
    for e in range(len(vec1)):
        out = vec1[e]*vec2[e]
    return out
    
    
dot_product(vec1,vec2)
dot_product([1,2],[3,4])
def factorial(n):
    if n == 1: return 1
    return factorial(n-1)*n
    
factorial(5)
get_ipython().run_line_magic('save', 'zadania')
get_ipython().run_line_magic('save', 'exec')
get_ipython().run_line_magic('save', 'zadania_execs')
