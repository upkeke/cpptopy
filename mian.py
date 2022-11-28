from ctypes import*
import os
# https://blog.csdn.net/qq809326636/article/details/80517455

#os.add_dll_directory(r'E:\C++\202211\PyDllTest\pyFile\build')
# python 只能在指定目录搜寻动态链接库，
# cpp生成的动态链接库在build文件夹下面，暂时找不到直接输入相对路径的方法
# 这个是先获得py文件所在的绝对路径，然后拼接上子目录 build
os.add_dll_directory(os.path.join(os.getcwd(),"build"))

dll = cdll.LoadLibrary('libpydll.dll');
dll.hello()


