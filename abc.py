import os

arquivo = open('user','r',20)
buff1 = arquivo.read(50)
arquivo.seek(0,0)
buff2 = arquivo.read(100)
print(buff1)
print('--------------')
print(buff2)