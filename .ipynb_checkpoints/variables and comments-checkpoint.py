Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num1,num2,num3=10,20,30
>>> print(num1)
10
>>> print(num2)
20
>>> print(num1,num2)
10 20
>>> print(id(num1))
140712803861912
>>> num1=num2=num3=10
>>> print(num2)
10
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a,b)
20 10
>>> print(a)
20
>>> print(b)
10
>>> a,b=10,20
>>> print(id(a),id(b))
140712803861912 140712803862232
>>> a,b=b,a
>>> print(id(a),id(b))
140712803862232 140712803861912
