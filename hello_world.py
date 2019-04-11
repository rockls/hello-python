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


	
	




