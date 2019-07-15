Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:/Yashi/B.Tech/Courses/Python/BasicsOfPython/MyFirstPythonProgram.py 
Hello Python
>>> 
=============================== RESTART: Shell ===============================
>>> #working with the shell
>>> #simple operations on numbers
>>> 10+2
12
>>> 50+40-35
55
>>> 12*10
120
>>> 96/12
8.0
>>> 15/0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    15/0
ZeroDivisionError: division by zero
>>> #(//)floor division gives only integer value of quotient
>>> 78//5
15
>>> 78%5
3
>>> #(**)operator is used for exponentiation
>>> 5**3
125
>>> #Built in format() function
>>> #without using format function
>>> float(16/3)
5.333333333333333
>>> #with using format function
>>> format(float(16/3),'.2f')
'5.33'
>>> #format function can be used to insert comma in number
>>> format(123456, ',')
'123,456'
>>> #operations on string
>>> 'Hello'
'Hello'
>>> "Helo"
'Helo'
>>> "Hello"
'Hello'
>>> #string in single quote or double quote its one and the same
>>> #triple qoutes can be used to specify multi line strings
>>> '''Hello'''
'Hello'
>>> #Python concatenate two strings which are placed side by side
>>> print('Beautiful Weather.....''Seems it would rain')
Beautiful Weather.....Seems it would rain
>>> #working with escape sequence
>>> print('What's your name?')
      
SyntaxError: invalid syntax
>>> #this can be solved by using (\)
>>> print('What\'s your name')
What's your name
>>> print("\")
      
SyntaxError: EOL while scanning string literal
>>> print("\\")
\
>>> print('\"')
"
>>> #print new line
>>> print("\n")


>>> #print new tab
>>> print('\t')
	
>>> #If you want to print raw string
>>> print(r'What\'s your name')
What\'s your name
>>> print("What's your name?")
What's your name?
>>> #string formatting
>>> format('Hello', '<30')
'Hello                         '
>>> format('Hello', '>50')
'                                             Hello'
>>> format('Hello', '^70')
'                                Hello                                 '
>>> #generally format function uses spaces to fill the specified width but we can use any other character to fill that width
>>> format('Hello', '-^70')
'--------------------------------Hello---------------------------------'
>>> format('Hello', '@<70')
'Hello@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
>>> format('Hello', '*>70')
'*****************************************************************Hello'
>>> 
