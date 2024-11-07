#class

class firstone() :

  def __init__(self, st_name, st_email, st_phone):
    self.name = st_name
    self.email = st_email
    self.phone = st_phone

  def give_stdetails(self):
    return self.name, self.email, self.phone

rohit = firstone('rohit', 'rohir@gmail.com', 43848746467)
print(rohit.give_stdetails())
rohit.name = 'vikash'
print(rohit.name)
print(rohit.phone)
print(rohit.email)
print(rohit.give_stdetails())


#polymorphism


class data_science:
  def msg_one(self):
    print('data science')

class ml_learing:
  def msg_one(self):
    print('ml learing')

def class_parcer(p):
  for i in p:
    i.msg_one()
a,b=data_science(),ml_learing()
q = [a,b]
class_parcer(q)
class test :
  def __init__(self, name, age):
    self.name = name
    self.age = age
a = test('rohit', 23)
a.name = 'rahul'
print(a.name)
class car:
  def __init__(self, year,make,model,speed):
    self.__year1 = year
    self.__make1 = make
    self.__model1 = model
    self.__speed1 = 0
a = car (2024, 'tata', 'harrier', 30)
print(a._car__year1)

class car:
  def __init__(self, year,make,model,speed):
    self.__year1 = year
    self.__make1 = make
    self.__model1 = model
    self.__speed1 = 0

  def set_speed(self, speed):
    self.__speed1 = 0 if speed < 0 else speed

  def get_speed(self):
    return self.__speed1  
  def return_car(self):
    return self.__year1, self.__make1, self.__model1, self.__speed1


a = car (2024, 'tata', 'harrier', 30)
a.set_speed(100)
print(a.get_speed())
print(a.return_car())

class bank_account:
  def __init__(self, balance):
    self.__account_balance = balance 

  def deposit(self, amount):
    self.__account_balance = self.__account_balance + amount

  def withdraw (self, money):
    if money < self.__account_balance:
      self.__account_balance = self.__account_balance - money
      return 'ok withdraw money'
    else:
      return 'not enough money to withdraw'
  def get_balance(self):
    return self.__account_balance

a = bank_account(1000)
a.deposit(100)
print(a.withdraw(200))
##a.withdraw(500)
print(a.get_balance())
print(a.withdraw(2000))
class inheritanse:
  def msg(self):
    return 'this is inheritance'

class child(inheritanse):
  pass

a=child()
print (a.msg())


def deco1 (func):
  def my_message():
    print('this is decorator')
    print('this is decorator and common use')
    func()
    print ('this is just a message')
  return my_message

@deco1
def my_func():
  print('this is my function', 6+8)
my_func()


class _method :
  def __init__(self, name,email_id):
     self.name1 = name
     self.email_id1 = email_id

  
  @classmethod 
  def class_method(cls, name,email_id):
    return cls(name,email_id)

  
  def give_details(self):
    return self.name1, self.email_id1

cl1=_method.class_method('rohit', 'rohit@gmail.com')
print(cl1.name1)
print(cl1.email_id1)

class _method :
  mob_num = 455848339485
  msg = 'this is a message'
  def __init__(self, name,email_id):
     self.name1 = name
     self.email_id1 = email_id
  @classmethod
  def chan_mob_num(cls, mo_num):
    cls.mob_num = mo_num


  @classmethod 
  def class_method(cls, name,email_id):
    return cls(name,email_id)


  def give_details(self):
    return self.name1, self.email_id1 , _method.mob_num

cl1=_method.class_method('rohit', 'rohit@gmail.com') #354635757)
print(cl1.name1)
print(cl1.email_id1)
print(_method.chan_mob_num(638909))


print(cl1.give_details())
print(_method.mob_num)
print(_method.msg)


class _method :
  mob_num = 455848339485
  msg = 'this is a message'
  def __init__(self, name,email_id):
     self.name1 = name
     self.email_id1 = email_id
  @classmethod
  def chan_mob_num(cls, mo_num):
    cls.mob_num = mo_num


  @classmethod 
  def class_method(cls, name,email_id):
    return cls(name,email_id)


  def give_details(self):
    return self.name1, self.email_id1 , _method.mob_num

  f = open ('test.txt', 'w')
  f.write('this is a test file')
  f.close()
  f = open ('test.txt', 'r')

  print(f.read())
  f.seek(4)
  print(f.readlines())
  import os
  print( os.path.getsize('test.txt'))
import io
with open('test.txt1','wb') as f:
  file = io.BufferedWriter(f)
  file.write(b'hello world \n')
  file.write(b'hello mr.rohit')
  file.flush()

print ('hello mr. rohit! how r u ? ')

import logging 
logging.basicConfig (filename = 'my.log', level = logging.INFO, format = '%(asctime)s %(message)s')
logging.info('log this line of execution')
logging.info('this is my logging infomation')
logging.critical('this is my logging and critical infomation')
logging.error('this is my logging and error infomation')
logging.warning('this is my logging and warning infomation')
logging.shutdown()

import threading 
import time
def first_thread(id):
  for i in range (10):
    print ('test1 %d printing %d' %(id,i))
    time.sleep(1)
first_thread(1)
thread1=[threading.Thread (target = first_thread, args = (i,)) for i in range (3)]
for t in thread1:
  t.start() 




import multiprocessing 
def my_process():
  print ('this is my multiprocessing programe')
if __name__ == '__main__' :
  m = multiprocessing.Process(target = my_process)
  print ('this is my main program')
  m.start()
  m.join()
  

  

  
