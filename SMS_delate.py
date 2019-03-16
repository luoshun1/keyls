# -*- coding: utf-8 -*-

import os,shutil,sys,logging,re
import newMyUtile

def deleteFile(src):
    print('-----%s-----' % src)
    flag = 0
    projPathList = newMyUtile.getProjList();
    for projPath in projPathList:
        if (re.search('Proj.Android.Wo', projPath) or
                re.search('Mumayi', projPath) or
                re.search('Muzhiwan', projPath) or
                re.search('Leshi', projPath) or
                re.search('Haixin', projPath) or
                re.search('Egame', projPath)):
            print("--------%s---------" % projPath);
            continue;
        dst = os.path.join(projPath, src);
        if os.path.exists(dst):
            flag = flag + 1
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            else:
                os.remove(dst)
    print("deleteFile flag = %d" % flag);

# 联通
deleteFile('sdkassets/ijiami_sdk')
deleteFile('sdkassets/ijiami_sdk_libs')
deleteFile('sdkassets/unipaysdk_res')
deleteFile('sdkassets/wocapsdk_res')
deleteFile('sdkassets/unicom_classez.jar')
deleteFile('libs/Multimode_Unipay_base.jar')
deleteFile('libs/Multimode_UniPay_payinfo.jar')
deleteFile('sdklibs/armeabi/libme_unipay.so')
deleteFile('runtime')

# 电信
deleteFile('sdkassets/egame')
deleteFile('libs/cn.egame.terminal.paysdk.jar')
deleteFile('libs/egame.log_20161103_out_release.jar')
deleteFile('sdklibs/armeabi/libegamepay_dr2.so')