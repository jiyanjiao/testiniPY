#from .__init__ import *
from A import Member
import sys
#print(sys.path)
import os
from zongA.A11A import A11
#获取项目路径下的目录

#os.chdir('D:\\pycharm\\testiniPY\\11\\A11B.py')

#打印出项目路径下的目录
for file in os.listdir(os.getcwd()):
     print(file)
sys.path.append('D:\\pycharm\\testiniPY\\11\\A11A.py')
print('系统路径为',sys.path)
m = Member()
print(m.getname())
A11()



