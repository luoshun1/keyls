# -*- coding: utf-8 -*-

import os,shutil,re
import newMyUtile

projPathList = newMyUtile.getProjList()

# print(projPathList)

newMyUtile.copyFilePro(os.path.join(os.path.abspath('.'), 'app'), projPathList, 1)
    