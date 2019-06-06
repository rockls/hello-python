#8.4
def greet_users(names):     
	#"""向列表中的每位用户都发出简单的问候"""     
	for name in names:         
		msg = "Hello, " + name.title() + "!"         
		print(msg) 
usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames) 

# 首先创建一个列表，其中包含一些要打印的设计 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 
# 模拟打印每个设计，直到没有未打印的设计为止 
#  打印每个设计后，都将其移到列表completed_models中 
while unprinted_designs:     
	current_design = unprinted_designs.pop()          
	#模拟根据设计制作3D打印模型的过程     
	print("Printing model: " + current_design)     
	completed_models.append(current_design)      
# 显示打印好的所有模型 
print("\nThe following models have been printed:") 
for completed_model in completed_models:     
	print(completed_model) 
	
#function_name ( list_name [:]) 这样函数所做的任何修改都只影响副本，而丝毫不影响原件

#8.5 传递任意数量的实参 
def make_pizza(*toppings):     
	#"""打印顾客点的所有配料"""     
	print(toppings)          
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese') 
#8.5.1
def make_pizza(size, *toppings):      
	#"""概述要制作的比萨"""     
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")      
	for topping in toppings:          
		print("- " + topping)           
make_pizza(16, 'pepperoni')  
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
#8.5.2
def build_profile(first, last, **user_info):     
	#"""创建一个字典，其中包含我们知道的有关用户的一切"""     
	profile = {}   
	profile['first_name'] = first     
	profile['last_name'] = last     
	for key, value in user_info.items(): 
		profile[key] = value     
	return profile 
 
user_profile = build_profile('albert', 'einstein',location='princeton', field='physics') 
print(user_profile)

#8.6
#导入类
import pizza

pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#导入特定的函数
from pizza import make_pizza
#from module_name import function_0 , function_1 , function_2

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 

# 使用as 给函数指定别名 
from pizza import make_pizza as mp 

mp(16, 'pepperoni') 
mp(12, 'mushrooms', 'green peppers', 'extra cheese') 

#使用as 给类指定别名 
import pizza as p 
 
p.make_pizza(16, 'pepperoni') 
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 

#导入模块中的所有函数 （不建议）
from pizza import * 
 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 

#8.7 函数编写指南 
#应给函数指定描述性名称，且只在其中使用小写字母和下 划线。描述性名称可帮助你和别人明白代码想要做什么。给模块（类）命名时也应遵循上述约定
#给形参指定默认值时，等号两边不要有空格： def function_name ( parameter_0 , parameter_1 =' default value ') 
#可使用两个空行将相邻的函数分开
#所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整 个程序。 

#9 类
class Dog():
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.odometer_reading = 0 
		
	def sit(self):
		print(self.name.title()+"is now sitting.")
		
	def roll_over(self):
		print(self.name.title()+"rolled over!")
    
my_dog = Dog('white',6)
my_dog.sit()
my_dog.roll_over()	

class Battery():
	def __init__(self,friend='summer'):
		self.friend=friend
	
	def read_friend(self):
		return self.friend
		
#继承
class Taidi(Dog):
	def __init__(self, name, age):
		super().__init__(name, age)
		self.battery = Battery() 	
			
#重写
	def sit(self):
		print(self.name.title()+"is now 继承.")
		
taidi = Taidi('yellow',2)
taidi.sit()
taidi.name='阿福'
taidi.sit()
print(taidi.battery.read_friend())

#10 文件与异常
with open('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
		
with open(r'C:\Users\siki\Desktop\python_work\text_files\filename.txt') as file_object:
	contents = file_object.read()
	print(contents)

pi_string = ''
with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
print(lines)
for line in lines:
	pi_string+=line.rstrip()
	print(line.rstrip())
print(pi_string)
print(len(pi_string))
#前五位
print(pi_string[:5])
#删除前两位
print(pi_string[2:])

#如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入（'w'）模式打开文 件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件
#Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数 str()将其转换为字符串格式
#读取模 式（'r'）、写入模式（'w'）、附加模式（'a'）
with open('pi_digits.txt','w') as file_object:
	file_object.write('i love programming')
	file_object.write("I love programming.\n")     
	file_object.write("I love creating new games.\n") 
	
with open('pi_digits.txt', 'a') as file_object:     
	file_object.write("I also love finding meaning in large datasets.\n")     
	file_object.write("I love creating apps that can run in a browser.\n") 
	
#抛出异常
try :
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!") 
else:
	print('正确的')

filename = 'alice.txt' 

try:
	with open(filename) as f_obj:     
		contents = f_obj.read() 
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."     
	print(msg) 
	#Python有一个pass语句，可在代码块中使用它来让Python什么都不要做
	pass

title = "Alice in wonderland"
a=title.split()
print(a)

#10.4 存储数据
import json

numbers=[1,2,3,4,5,11]
filename='numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers,f_obj)
	
with open(filename) as f_obj:
	numbers=json.load(f_obj)
print(numbers)

#11.1 测试函数

def 








	
	

	


















	

 






 
 
