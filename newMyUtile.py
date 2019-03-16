# -*- coding: utf-8 -*-

import os,shutil,sys,logging,re

def getProjList():
    """获取所有Proj.Android开头的文件的路径.

    return:
        所有Proj.Android开头的文件的绝对路径的list.
    """
    projPathList = [];
    for fileName in os.listdir('../../'):
        if re.search('Proj.Android', fileName):
            filepath = os.path.join(os.path.abspath('../../'), fileName);
            projPathList.append(filepath);
    return projPathList;

def getCpsProjList():
    """获取所有Proj.Android.Mini开头的文件的路径。
    
    return：
        所有Proj.Android.Mini开头的文件夹的绝对路径。
    """
    projList = getProjList();
    cpsProjList = [];
    for filePath in projList:
        if re.search('Proj.Android.Mini', filePath):
            cpsProjList.append(filePath);
    return cpsProjList;

def copyFile(srcPath, dstPath, type=0, flag=0):
    """递归复制文件.

    srcPath:
        源文件所在路径
    dstPath:
        目标文件所在路径
    type:
        复制方式：0:不管什么情况都复制。1:目标文件存在时复制。2:目标文件存在时跳过。
    """
    for srcFile in os.listdir(srcPath):
        absSrcFile = os.path.join(srcPath, srcFile)
        absDstFile = os.path.join(dstPath, srcFile)
        if os.path.isdir(absSrcFile):
            copyFile(absSrcFile, absDstFile, type)
        elif os.path.isfile(absSrcFile):
            if ((type == 1 and not os.path.exists(dstPath)) or
                    (type == 2 and os.path.exists(dstPath))):
                    continue;
            if not os.path.exists(dstPath):
                os.makedirs(dstPath);
            
            print("%s --> %s" % (absSrcFile, dstPath))
            shutil.copy(absSrcFile, dstPath);

def copyFilePro(srcPath, dstPathList, type=0):
    """递归复制文件.

    srcPath:
        源文件所在路径
    dstPathList:
        多个目标文件所在路径
    type:
        复制方式：0:不管什么情况都复制。1:目标文件存在时复制。2:目标文件存在时跳过。
    """
    if isinstance(dstPathList, list):
        flag = 0
        for dstPath in dstPathList:
            flag = flag + 1
            copyFile(srcPath, dstPath, type)
        print("copyFilePro flag = %d" % flag)

def deleteFile(src, dstList):
    """删除文件或文件夹
    
    src:
        源文件相对路径
    dstList:
        多个目标文件绝对路径
    """
    print('-----%s-----' % src)
    flag = 0
    for projPath in dstList:
        dst = os.path.join(projPath, src);
        if os.path.exists(dst):
            flag = flag + 1
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            else:
                os.remove(dst)
    print("deleteFile flag = %d" % flag);