Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> b='boob'
>>> 2*b
'boobboob'
>>> type('')
<class 'str'>
>>> str'12'
SyntaxError: invalid syntax
>>> int('12')
12
>>> str(12)
'12'
>>> type(b)
<class 'str'>
>>> type('b')
<class 'str'>
>>> type(12)
<class 'int'>
>>> str('12')
'12'
>>> type('12')
<class 'str'>
>>> b+str(12)
'boob12'
>>> 
================== RESTART: /Users/yandang/Documents/hello.py ==================
Hello world!
>>> 
================== RESTART: /Users/yandang/Documents/hello.py ==================
Hello world!
What is your name?
================== RESTART: /Users/yandang/Documents/input.py ==================
Hello world!
What is your name?
================== RESTART: /Users/yandang/Documents/input.py ==================
Hello world!
What is your name?
================== RESTART: /Users/yandang/Documents/input.py ==================
Hello world!
Whatisyourname?
Hello !Haveaniceday.
>>> 
>>> 
>>> 
>>> 1==1
True
>>> 2!=1
True
>>> 2<1
False
>>> 'Tim'<'Tom'
True
>>> 'Apple'>'Banana'
False
>>> 'A'<'a'
True
>>> type(True)
<class 'bool'>
>>> 
==================== RESTART: /Users/yandang/Documents/if.py ===================
Hello world!
Whatisyourname?
==================== RESTART: /Users/yandang/Documents/if.py ===================
What is your name?
==================== RESTART: /Users/yandang/Documents/if.py ===================
What is your name?
Traceback (most recent call last):
  File "/Users/yandang/Documents/if.py", line 7, in <module>
    Print("Hello, name")
NameError: name 'Print' is not defined
>>> name=input("What is your name?")

if name=="Tim":
    print("Greetings, Tim the Enchanter")
else:
    Print("Hello, name")




What is your name?
>>> 
>>> 
>>> Tim
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    Tim
NameError: name 'Tim' is not defined
>>> Yan
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Yan
NameError: name 'Yan' is not defined
>>> name==Tim
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    name==Tim
NameError: name 'Tim' is not defined
>>> name=="Tim"
False
>>> What is your name? Tim
SyntaxError: invalid syntax
>>> Tim
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Tim
NameError: name 'Tim' is not defined
>>> What is your name? Tim
SyntaxError: invalid syntax
>>> 
=============== RESTART: /Users/yandang/Documents/if_elif_else.py ==============
What is your name? Tim
Hello  Tim
>>> 
>>> 
>>> 
=============== RESTART: /Users/yandang/Documents/if_elif_else.py ==============
What is your name?Brian
Bad luck, Brian
>>> 
=============== RESTART: /Users/yandang/Documents/if_elif_else.py ==============
What is your name?Aurthur, King of the Britons
Hello Aurthur, King of the Britons
>>> 
=============== RESTART: /Users/yandang/Documents/if_elif_else.py ==============
What is your name? Tin
Hello  Tin
>>> 
=============== RESTART: /Users/yandang/Documents/if_elif_else.py ==============
What is your name?Tim
Greetings, Tim the Enchanter
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Tim
Hello Tim.
What do you want to talk about? Java
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction_while.py", line 13, in <module>
    while topic!="nothing":
NameError: name 'topic' is not defined
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Brian
Hello Brian.
What do you want to talk about? Python
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction_while.py", line 13, in <module>
    while topic !="nothing":
NameError: name 'topic' is not defined
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Jim
Hello Jim.
What do you want to talk about? Java
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction_while.py", line 13, in <module>
    while topic !="nothing":
NameError: name 'topic' is not defined
>>> 
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Dang
Hello Dang.
What do you want to talk about?
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction_while.py", line 13, in <module>
    while topic !="nothing":
NameError: name 'topic' is not defined
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Jim
Hello Jim.
What do you want to talk about?java
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction_while.py", line 13, in <module>
    while topic =="nothing":
NameError: name 'topic' is not defined
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Tim
Hello Tim.
What do you want to talk about? Python
Do you like Python? yes
Why do you think that? it's interesting
I also think that  it's interesting
Do you like Python?yyes
Why do you think that?its goof
I also think that its goof
Do you like Python?no
Why do you think that?
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? ali
Hello ali.
What do you want to talk about? boobs
Do you like boobs? yes
Why do you think that? they are soft
I also think that  they are soft
Do you like boobs?
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? ahmad
Hello ahmad.
What do you want to talk about? sex
Do you like sex? yes
Why do you think that?they felt good
I also think that they felt good
What do you want to talk about?cocnut
Do you likecocnut? no
Why do you think that? yes
I also think that  yes
What do you want to talk about? jj
Do you like jj?
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? yandang
Hello yandang.
What do you want to talk about? nuts
Okay. Goodbye, yandang!
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Brian
Hello Brian.
What do you want to talk about? Biran
Okay. Goodbye, Brian!
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Brian
Hello Brian.
What do you want to talk about? kkj
Okay. Goodbye, Brian!
>>> 
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Ken
Hello Ken.
What do you want to talk about? armpit
Do you like armpit? no
Why do you think that? they are smelly
I also think that  they are smelly
What do you want to talk about?
============ RESTART: /Users/yandang/Documents/interaction_while.py ============
What is your name? Tim
Hello Tim.
What do you want to talk about?
============ RESTART: /Users/yandang/Documents/interaction_break.py ============
What is your name? Tim
Hello Tim.
What do you want to talk about? hen
Do you like hen? yes
Why do you think that? they can lay eggs
I also think that  they can lay eggs
What do you want to talk about?
============ RESTART: /Users/yandang/Documents/interaction_break.py ============
What is your name? Tim
Hello Tim.
What do you want to talk about?
============ RESTART: /Users/yandang/Documents/interaction_break.py ============
What is your name? Brian
Hello Brian.
What do you want to talk about?
============ RESTART: /Users/yandang/Documents/interaction_break.py ============
What is your name? da
Hello da.
Do you like university? yeah
Why do you think that? its basically export service
That's very intersting.
What do you want to talk about?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? amgmo
Hello amgmo.
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction.py", line 9, in <module>
    discuss("university?")
NameError: name 'discuss' is not defined
>>> 
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? ali
Hello ali.
Do you likeuniversity??
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? ali
Hello ali.
Do you likeuniversity? yes
That's very intersting.
What do you want to talk about? loli
Do you like loli? yes
I also think that Why do you think that?
What do you want to talk about?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? lal
Hello lal.
Do you like university? yes
Why do you think that? no
That's very intersting.
What do you want to talk about? ff
Do you like  ff?ff
Why do you think that?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? amy
Hello amy.
Do you like university? yes
Why do you think that? hh
That's very intersting.
What do you want to talk about?boobs
Do you like boobs? yes
Why do you think that? doft
I also think that  doft
What do you want to talk about? nothing
Do you like  nothing?j
Why do you think that?j
I also think that j
What do you want to talk about? 
Do you like  ?h
Why do you think that?
I also think that 
What do you want to talk about? nothing
Do you like  nothing?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? Tim
Hello Tim.
Do you like university? yes
Why do you think that? no
That's very intersting.
What do you want to talk about? ff
Do you like  ff?yes
Why do you think that?s
I also think that s
What do you want to talk about?nothing
Okay. Goodbye, Tim!
>>> 
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? mm
Hello mm.
Do you like university? yes
Why do you think that? no
That's very intersting.
What do you want to talk about?f
Do you like f? j
Why do you think that?j
I also think that j
What do you want to talk about? nothing
Do you like  nothing?jj
Why do you think that?j
I also think that j
What do you want to talk about?nothing
Okay. Goodbye, mm!
>>> name = "ken"
>>> name
'ken'
>>> 
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name?Ken
HelloKen.
Do you like university?yes
Why do you think that?jj
a:jj
That's very intersting.
What do you want to talk about?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? Brian 
Hello Brian .
Do you like university?j
Why do you think that?j
That's very intersting.
What do you want to talk about?j
Do you like j?
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction.py", line 21, in <module>
    response=discuss(topic)
  File "/Users/yandang/Documents/interaction.py", line 10, in discuss
    like=input("Do you like "+topic+"?")
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? Tim
Hello Tim.
Do you like university?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? Tim
name: Tim
Hello Tim.
Do you like university?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name?Tim
name:Tim
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction.py", line 4, in <module>
    name:Tim
NameError: name 'Tim' is not defined
>>> 
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name?Tim
Greetings, Tim the Enchanter
Do you like university?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? Brian
Bad luck, Brian
Do you like university?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? h
Helloh.
Do you like university?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? j
Hello j.
Do you like university?
Why do you think that?
That's very intersting.
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
=============== RESTART: /Users/yandang/Documents/interaction.py ===============
What is your name? Brian
Bad luck, Brian
Do you like university?
Why do you think that?
That's very intersting.
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Do you like ?
Why do you think that?
I also think that 
What do you want to talk about?
Traceback (most recent call last):
  File "/Users/yandang/Documents/interaction.py", line 20, in <module>
    topic =input("What do you want to talk about?")
KeyboardInterrupt
>>> 7//2
3
>>> 7%2
1
>>> 10/5
2.0
>>> 10%5==0
True
>>> def is_prime(n):
	"""Returns True iff n is prime

	is_prime(int)->bool
	precondition:n>1

	"""
	i=2
	while i<n:
		if n%i==0:
			return False
		i=i+1
		return True
	
KeyboardInterrupt
>>> is_prime(2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    is_prime(2)
NameError: name 'is_prime' is not defined
>>> is_prime(3)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    is_prime(3)
NameError: name 'is_prime' is not defined
>>> is_prime(2)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    is_prime(2)
NameError: name 'is_prime' is not defined
>>> is prime(4)
SyntaxError: invalid syntax
>>> is_prime(4)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    is_prime(4)
NameError: name 'is_prime' is not defined
>>> is_prime(101)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    is_prime(101)
NameError: name 'is_prime' is not defined
>>> print(is_prime)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(is_prime)
NameError: name 'is_prime' is not defined
>>> 
KeyboardInterrupt
>>> def is_prime(n):
	"""Returns True iff n is prime

	is_prime(int)->bool
	precondition:n>1

	"""
	i=2
	while i<n:
		if n%i==0:
			return False
		i=i+1
		return True

	
>>> is_prime(2)
>>> is_prime(2)
>>> is_prime(4)
False
>>> is_prime(101)
True
>>> >>> def is_prime(n):
	"""Returns True iff n is prime

	is_prime(int)->bool
	precondition:n>1

	"""
	if n==2:
	return True

	elif n%2==0:
	return False
	sqrt_n=math.sqrt(n)
	i=3
	while i<=sqrt_n:
		if n%i==0:
			return False
		i=i+2
		return True

	      
	
SyntaxError: invalid syntax
>>> is_prime(2)
>>> 
>>> is_prime(9)
True
>>> def is_prime(n):
	"""Returns True iff n is prime

	is_prime(int)->bool
	precondition:n>1

	"""
	if n==2:
	return True

	elif n%2==0:
	return False
	sqrt_n=math.sqrt(n)
	i=3
	while i<=sqrt_n:
		if n%i==0:
			return False
		i=i+2
		return True
