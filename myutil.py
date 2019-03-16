#!/user/bin/env python
# -*- coding: utf-8 -*-

import os,shutil,sys,re

# rootPath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../.."))
rootPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
dirAppPlayList = os.listdir(os.path.realpath(os.path.join(rootPath, '../..')))
dirAppPlay = os.path.realpath(os.path.join(rootPath, '../..'))

FILE = __file__
LINE = sys._getframe().f_lineno

def path_join(*args):
    '''
    # 路径拼接
    - *args:输入某个文件的路径的组成部分
    - 返回拼接好的路径
    '''
    result = ''
    for i in args:
        result = os.path.join(result, i)
    return result

def file_copy(src, dst):
    '''
    # 文件或文件夹复制
    - src:输入路径
    - dst:输出路径
    '''
    if os.path.isfile(src):
        try:
            shutil.copyfile(src, dst)
        except Exception as ex:
            print('file_copy' + str(ex))
    elif os.path.isdir(src):
        if os.path.exists(dst):
            print(dst, '存在先删除')
            shutil.rmtree(dst)

        try:
            shutil.copytree(src, dst)
        except Exception as ex:
            print(__file__, str(ex))

def file_select(pattern, filePath, flags=0):
    '''
    # 通过正则表达式筛选文件或文件夹
    - pattern:正则表达式
    - filePath:要匹配的字符串
    - flags:正则表达式修饰符
    '''
    if re.search(pattern, filePath, flags):
        return filePath
    else:
        return None

def getNeedChannels(channel_type=0):
    '''
    # 获取目标渠道
    - channel_type:匹配模式：0 全渠道
    '''
    channels_list = []
    root_paht = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    if channel_type == 0:
        for file in os.listdir(root_paht):
            if re.search('Proj.Android', file):
                channels_list.append(file)

    return channels_list

    

def test_func():
    pathList = os.listdir(os.path.realpath(os.path.join(rootPath, '../..')))
    for i in pathList:
        filePath = os.path.realpath(i)
        if file_select('Proj.Android', filePath):
            print(filePath)



# def copy_func(srcPath, dstPath):
    
