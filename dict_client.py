"""
dict 客户端

功能: 根据用户输入,发送请求,得到结果
结构:  一级界面 --> 注册  登录  退出
      二级界面 --> 查单词  历史记录  注销
"""
 
from socket import *
from getpass import getpass  # 运行使用终端
import sys
# 服务器地址
ADDR = ('127.0.0.1',8000)
# 功能函数都需要套接字,定义为全局变量
s = socket()
s.connect(ADDR)

# 二级
def login():
  while True:
    print("""
    ==============Welcome==============
      1.查单词      2.历史记录     3.注销
    ===================================
    """)
    cmd = input("输入选项:")
    if cmd == '1':
      do_register()
    elif cmd == '2':
      do_login()
    elif cmd == '3':
      return
    else:
      print("请输入正确选项")

# 注册函数
def do_register():
  while True:
    name = input("User:")
    passwd = getpass()
    passwd_ = getpass('Again:')

    if (' ' in name) or (' ' in passwd):
      print("用户名或密码不能有空格")
      continue
    if passwd != passwd_:
      print("两次密码不一致")
      continue

    msg = "R %s %s"%(name,passwd)
    s.send(msg.encode()) # 发送请求
    data = s.recv(128).decode() # 接收反馈信息
    if data == 'OK':
      print("注册成功")
      login()
    else:
      print("注册失败")
    return

# 登录函数
def do_login():
  while True:
    name = input("User:")
    passwd = getpass()

    if (' ' in name) or (' ' in passwd):
      print("用户名或密码不能有空格")
      continue

    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode()) # 发送请求
    data = s.recv(128).decode() # 接收反馈信息
    if data == 'OK':
      print("登录成功")
      login()
    else:
      print("登录失败")
    return


# 搭建客户端网络
def main():
  while True:
    print("""
    ==============Welcome==============
      1.注册      2. 登录       3.退出
    ===================================
    """)
    cmd = input("输入选项:")
    if cmd == '1':
      do_register()
    elif cmd == '2':
      do_login()
    elif cmd == '3':
      s.send(b'E')
      sys.exit("谢谢使用")
    else:
      print("请输入正确选项")

if __name__ == "__main__":
  main()










