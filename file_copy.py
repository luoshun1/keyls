#!/user/bin/env python
# -*- coding: utf-8 -*-

import os,shutil,sys,logging,re

def getDirAndCopyFile(sourcePath,targetPath):

    if not os.path.exists(sourcePath):
        return
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
        
    #遍历文件夹
    for fileName in os.listdir(sourcePath):
        #拼接原文件或者文件夹的绝对路径
        absourcePath = os.path.join(sourcePath, fileName)
        #拼接目标文件或者文件加的绝对路径
        abstargetPath = os.path.join(targetPath, fileName)
        #判断原文件的绝对路径是目录还是文件
        if os.path.isdir(absourcePath):
            #是目录就创建相应的目标目录
            os.makedirs(abstargetPath)
            #递归调用getDirAndCopyFile()函数
            getDirAndCopyFile(absourcePath,abstargetPath)
        #是文件就进行复制
        if os.path.isfile(absourcePath):
            rbf = open(absourcePath,"rb")
            wbf = open(abstargetPath,"wb")
            while True:
                content = rbf.readline(1024*1024)
                if len(content)==0:
                    break
                wbf.write(content)
                wbf.flush()
            rbf.close()
            wbf.close()

def copyFile(srcPath, dstPath):

    if not os.path.exists(srcPath):
        print('srcPath isn\'t exists ------')
        return
    if not os.path.exists(dstPath):
        print('dstPath is not exists ------')
        return

    # 遍历文件夹
    for fileName in os.listdir(srcPath):
        # 拼接源文件或者文件夹的绝对路径
        absourcePath = os.path.join(srcPath, fileName)
        # 拼接目标文件或者文件夹的绝对路径
        abstargetPath = os.path.join(dstPath, fileName)
        # 判断目标文件或文件夹是否存在
        if os.path.exists(abstargetPath):
            break
            # 判断源文件是文件还是文件夹
        if os.path.isdir(absourcePath):
            copyFile(absourcePath, abstargetPath)
        elif os.path.isfile(absourcePath):
            print('----- start copy to ', abstargetPath)
            shutil.copy(absourcePath, abstargetPath)

def getDir():
    rootPaht = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    return rootPaht

def doSomething():
    sourcePaht = os.path.abspath(os.path.join(os.path.dirname(__file__), 'common'))
    # print(sourcePaht)
    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    # print('-------', rootPath)
    for fileName in os.listdir(rootPath):
        # print(fileName, '-----')
        if re.search('Proj.Android', fileName):
            # copyFile('abcd', fileName)
            tagPath = os.path.abspath(fileName)
            # print(tagPath)
            # copyFile(sourcePaht, tagPath)


# doSomething()