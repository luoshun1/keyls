#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import shutil,os

rootPath = os.path.abspath(os.path.join(os.getcwd(), "../.."))

defaultChannel = ['Proj.Android.Baidu',
	'Proj.Android.BaiduDK',
	'Proj.Android.BaiduSJZS',
	'Proj.Android.BaiduTB',
	'Proj.Android.Coolpad',
	'Proj.Android.Dangle',
	'Proj.Android.Dianyou',
	'Proj.Android.Egame',
	'Proj.Android.Google',
	'Proj.Android.Haixin',
	'Proj.Android.Huawei',
	'Proj.Android.Jinli',
	'Proj.Android.Kuaifa',
	'Proj.Android.Kugou',
	'Proj.Android.Lenovo',
	'Proj.Android.LenovoYX',
	'Proj.Android.Leshi',
	'Proj.Android.Meizu',
	'Proj.Android.Mi',
	'Proj.Android.Migu',
	'Proj.Android.OverseasBeta',
	'Proj.Android.Oppo',
	'Proj.Android.Mumayi',
	'Proj.Android.Muzhiwan',
	'Proj.Android.Samsung',
	'Proj.Android.TencentQQDT',
	'Proj.Android.TencentAce',
	'Proj.Android.Vivo',
	'Proj.Android.Wdj',
	'Proj.Android.Wo']
cornerChannel = {'Proj.Android.Anzhi':'安智',
	'Proj.Android.Mini':'官网',
	'Proj.Android.Mini7723':'官网',
	'Proj.Android.Mini18183':'官网',
	'Proj.Android.MiniDuoWan':'官网',
	'Proj.Android.MiniGGZS':'官网',
	'Proj.Android.MiniJieKu':'官网',
	'Proj.Android.MiniJinliYY':'官网',
	'Proj.Android.MiniJuFeng':'官网',
	'Proj.Android.MiniKuaiKan':'官网',
	'Proj.Android.MiniKubi':'官网',
	'Proj.Android.MiniLeiZheng':'官网',
	'Proj.Android.MiniMeiTu':'官网',
	'Proj.Android.MiniNubia':'官网',
	'Proj.Android.MiniPP':'官网',
	'Proj.Android.MiniQingCheng':'官网',
	'Proj.Android.MiniQingNing':'官网',
	'Proj.Android.MiniScb':'官网',
	'Proj.Android.MiniSmartisan':'官网',
	'Proj.Android.MiniSmss':'官网',
	'Proj.Android.MiniWdj':'官网',
	'Proj.Android.MiniWuFan':'官网',
	'Proj.Android.MiniXianGuo':'官网',
	'Proj.Android.MiniYDMM':'官网',
	'Proj.Android.MiniYouFang':'官网',
	'Proj.Android.MiniYYH':'官网',
	'Proj.Android.MiniZhongXing':'官网',
	'Proj.Android.SougouLLQ':'搜狗',
	'Proj.Android.SougouSJZS':'搜狗',
	'Proj.Android.SougouSRF':'搜狗',
	'Proj.Android.SougouSS':'搜狗',
	'Proj.Android.SougouYX':'搜狗',
	'Proj.Android.Tencent':'应用宝',
	'Proj.Android.Gg':'GG助手',
	'Proj.Android.Iqiyi':'爱奇艺',
	'Proj.Android.Jrtt':'头条',
	'Proj.Android.T4399':'4399',
	'Proj.Android.uc':'UC',
	'Proj.Android.Qihoo':'360'}

# 废弃的渠道
['Proj.Android.Jifeng',
	'Proj.Android.Meitu',
	'Proj.Android.TencentHTC',
	'Proj.Android.TencentHWYX',
	'Proj.Android.TencentHWYY',
	'Proj.Android.TencentJS',
	'Proj.Android.TencentQLF',
	'Proj.Android.TencentQQ',
	'Proj.Android.TencentQQGJ',
	'Proj.Android.TencentSJJL',
	'Proj.Android.x7sy',
	'Proj.Android.Blockark',
	'Proj.Android.BlockarkIosRes',
	'Proj.Android.Google',
	'Proj.Android.Studio',
	'Proj.Android.TianTian',]

targetFolder = ['drawable-hdpi',
    'drawable-ldpi',
    'drawable-mdpi',
    'drawable-xhdpi',
    'drawable-xxhdpi',]

newDefaultIconRootPath = "D:\\WorkData\\icon\\安卓三周年\\安卓\\无角标-圆角\\"
newCornerIconRootPath = "D:\\WorkData\\icon\\安卓三周年\\安卓\\渠道\\"

newFileName = ['72.png',
    '36.png',
    '48.png',
    '96.png',
    '144.png',]

cornerIconChannel = ""

def SinglePathJoin(*args):
    targetPaty = ""
    for i in args:
        targetPaty = os.path.join(targetPaty, i)
    return targetPaty

def SingleFileCopy(srcPath, desPath):
    print("copy: srcPath:" + srcPath + " ------------>  desPath:" + desPath)
    try:
        shutil.copy(srcPath, desPath)
    except Exception as ex:
        print("onlyOneReplace" + str(ex))

def SingleFullPath():
    for i in defaultChannel:
        m = 0
        for j in targetFolder:
            desFullPath = SinglePathJoin(rootPath, i, "res", j, "ic_launcher.png")
            srcFullPath = SinglePathJoin(newDefaultIconRootPath, newFileName[m])
            SingleFileCopy(srcFullPath, desFullPath)
            m += 1
            # print("desFullPath:" + desFullPath + ", srcFullPath:" + srcFullPath)
    for k, v in cornerChannel.items():
        n = 0
        for x in targetFolder:
            srcFullPath = SinglePathJoin(newCornerIconRootPath, v, newFileName[n])
            desFullPath = SinglePathJoin(rootPath, k, "res", x, "ic_launcher.png")
            SingleFileCopy(srcFullPath, desFullPath)
            n += 1

    
    
SingleFullPath()
# SinglePathJoin("1", "2")
# SingleFileCopy("E:\\a\\2.txt", "E:\\b\\121.txt")