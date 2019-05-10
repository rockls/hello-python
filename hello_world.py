# print("123456")
#你好
hello="haha"
print(hello.title())
print(hello.upper())
print(hello.lower())

first_name="haha"
second_name="nihao"
fll_name=first_name+""+second_name
print(fll_name)

print("\t"+fll_name)
print('\n'+fll_name)
print('\n\t'+fll_name.rstrip())
print('\n\t'+fll_name.lstrip())
print('\n\t'+fll_name.strip())
print("Languages:\n\tPython\n\tC\n\tJavaScript")

age = 23 
message = "Happy " + str(age) + "rd Birthday!" 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles) 
print(bicycles[0]) 
print(bicycles[1]) 
print(bicycles[2]) 
print(bicycles[0].title())
print(bicycles[-1]) 
print(bicycles[-2])
print(bicycles[-3])  

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles[0] = 'ducati' 
print(motorcycles) 
motorcycles.append("haha")
print(motorcycles)
motorcycles = [] 
motorcycles.insert(0,1)
motorcycles.insert(1,"23")
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 
popped_motorcycle = motorcycles.pop()
print(motorcycles) 
print(popped_motorcycle)
motorcycles.remove('honda') 
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()
print(cars) 
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
cars.reverse() 
len(cars)

magicians = ['alice', 'david', 'carolina']
for ma in magicians :
	print(ma)
	
for number in range(1,8):
	print(number)

numbers=list(range(1,8))
print(numbers)

numbers=list(range(1,8,2))
print(numbers)

s=[]
for value in range(1,11) :
	b=value**2
	s.append(b)
print(s)
print(min(s))
print(max(s))
print(sum(s))

squares=[value**2 for value in range(1,12)]
print(squares)
print(squares[1:3])
print(squares[:3])
print(squares[1:])
print(squares[-3:])
for player in squares[:3]:     
	print(player)
copy_squares=squares[:]
print(copy_squares)
squares.append(101)
print(squares)
print(copy_squares)

no_change=(100,200)
print(no_change[0])
print(no_change[1])
for value in no_change :
	print(value)
no_change=(200,40)

cars = ['audi', 'bmw', 'subaru', 'toyota'] 
for car in cars:
	if car=='audi':
		print("auti")
	else:
		print(1111)
		
print ("audi" in cars)
age_0=22
age_1=23
if  age_0 >= 21 and age_1 >= 21 :
	print("true")
else:
	print("false")
	
age=12
if age<4:
	p=0
elif age<18:
	p=1
else:
	p=2
	
a=[]
if a:
	print("非空")
else:
	print("空")
	
demo ={'color' : 'green','points' : 5}
print(demo['color'])
print(demo['points'])
demo['haha']='lele'
print(demo)
alien_0 = {} 
alien_0['color'] = 'green' 
alien_0['points'] = 5 
alien_0['points'] = 6
print(alien_0)
del alien_0['color']
print(alien_0)
favorite_languages = {     
	'jen': 'python',     
	'sarah': 'c',     
	'edward': 'ruby',     
	'phil': 'python',     
	}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".") 

user_0 = {
     'username': 'efermi',
     'first': 'enrico',
     'last': 'fermi',
     }
for key,value in user_0.items():
	print("\nkey:" + key)
	print("value:" + value)
for name in user_0.keys():     
	print(name.title()) 

for name in sorted(user_0.keys()):
	print(name.title())
for value in user_0.values():
	print(value.title())
for value in set(user_0.values()):
	print(value)
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

aliens=[]
for alien_number in range(30):
	new_alien={'color' : 'green','point' : 5,'speed' : 'slow'}
	aliens.append(new_alien)
for alien in aliens[:5]:
	print(alien)
print (str(len(aliens)))
for alien in aliens[0:3]:
	if alien['color']=='green' :
		alien['color']='yellow'
		alien['point']=3
	elif alien['color']=='yellow':
		alien['color']='red'
		alien['point']=2
	print(alien)
pizza={
	'crust' : 'thick',
	'topping' : ['mushrooms','extra cheese'],
	}
print("You ordered a " + pizza['crust'] + "-crust pizza " +     "with the following toppings:")
for topping in pizza['topping']:
	print('\t'+topping)
favorite_languages = {
     'jen': ['python', 'ruby'],
     'sarah': ['c'],
     'edward': ['ruby', 'go'],     
     'phil': ['python', 'haskell'],     
     } 
for name,value in favorite_languages.items():
	print(name+"最喜欢的语言是")
	if len(value)>1:
		for language in value:
			print(language)
	else:
		print("仅此一种")
#第七章 用户输入和while循环
message = input("tell me something: ")
print(message)
name = input("Please enter your name: ") 
print("Hello, " + name + "!") 
age=input("how old are you? ")
age=int(age)
if age>18:
	print("你太老了")
else:
	print("你很年轻")
a=1
while a<=5:
	print(a)
	a+=1
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
message = "" 
while message != 'quit':     
	message = input(prompt)   
	if message != 'quit':   
		print(message) 
		
unconfirmed_users = ['alice', 'brian', 'candace'] 
confirmed_users = [] 
while unconfirmed_users:
	 current_user = unconfirmed_users.pop()
	 print("Verifying user: " + current_user.title()) 
	 confirmed_users.append(current_user) 
print("\nThe following users have been confirmed:") 
for confirmed_user in confirmed_users:     
	print(confirmed_user.title()) 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets) 
 
while 'cat' in pets:     
	pets.remove('cat')      
print(pets) 
#第八章函数
def greet_user():
	print("hello")
greet_user()

def greet_user(username,age):
	print(username.title())
greet_user("siqi",5)

greet_user(username="siqi",age=5)

def greet_user(username,age=6):
	print(username.title()+" "+str(age))
greet_user(username="siqi")
greet_user(username="liu",age=5)

def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:         
		full_name = first_name + ' ' + middle_name + ' ' + last_name      
	else:         
		full_name = first_name + ' ' + last_name    
	return full_name.title() 
musician = get_formatted_name('jimi', 'hendrix') 
print(musician) 
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician) 

def build_person(first_name, last_name,age=""):     
	person = {'first': first_name, 'last': last_name}    
	 if age:        
		  person['age'] = age 
	return person 
musician = build_person('jimi', 'hendrix',34) 
print(musician)

#8.4







	
	




