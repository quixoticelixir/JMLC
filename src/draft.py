import os

print('#1')
print(os.getcwd())
# print(os.path.basename(__file__))
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
print('#2')
a = os.path.dirname(os.path.realpath(__file__)) #+ '/output/' + self.start_date + '_' + \
                        # self.end_date + '/'
print(a)

print('#3')
b = os.path.dirname(os.path.abspath(__file__))
print(b)

print('#4')
print(os.path.abspath(''))

print('#5')
print(os.path.realpath(''))