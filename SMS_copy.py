#!/user/bin/env python
# -*- coding: utf-8 -*-

import os,shutil,sys,logging,re

def getProjList():
    projPathList = [];
    for fileName in os.listdir('../../'):
        if re.search('Proj.Android', fileName):
            filepath = os.path.join(os.path.abspath('../../'), fileName);
            projPathList.append(filepath);
    return projPathList;

def getDstPathList(proof):
    dstPathList = [];
    projPathList = getProjList();
    print
    for path in projPathList:
        dstfileName = os.path.join(path, proof);
        if os.path.exists(dstfileName):
            dstPathList.append(path)
    return dstPathList

def copyFile(srcPath, dstPath):
    for srcFile in os.listdir(srcPath):
        absSrcFile = os.path.join(srcPath, srcFile)
        absDstFile = os.path.join(dstPath, srcFile)
        if os.path.isdir(absSrcFile):
            copyFile(absSrcFile, absDstFile)
        elif os.path.isfile(absSrcFile):
            if not os.path.exists(dstPath):
                os.makedirs(dstPath);
            shutil.copy(absSrcFile, dstPath);

def startCopy():
    flag = 0
    srcPath = os.path.join(os.path.abspath('.'), 'target');
    dstPathList = getDstPathList('libs/cn.egame.terminal.paysdk.jar');
    for dstPath in dstPathList:
        print(dstPath)
        flag = flag + 1
        copyFile(srcPath, dstPath)
    print("----", flag)

def deleteFile():
    dstPathList = getProjList();
    for dstPath in dstPathList:
        if os.path.exists(os.path.join(dstPath, 'sdkassets/egame/EPSH_141.zip')):
            os.remove(os.path.join(dstPath, 'sdkassets/egame/EPSH_141.zip'))

deleteFile();
# startCopy()
