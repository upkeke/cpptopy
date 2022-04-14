# 环境

C++ mingw32 g++ 9.2.0

python 3.8.3

swig



# 步骤

1. 写好cpp文件后，在cmd输入指令 swig -c++ -python example.i   
2. 然后python setup.py build
3. 在在build\lib 文件夹下的_example .pyd 移动到python文件夹的libs文件下，之后所有py都可以引用这个包

# 注意事项

1. 目前方向引用的这个包只在pycharm编辑器下有代码自动补全的功能，VSCode下没有代码补全
2. 如果有多个python解释器，在步骤2中可以指定解释器，比如 py -3.8 setup.py build,用什么解释器build的就只能在对应的解释器环境下运行
3. 