from myutil import *
import os,shutil

def codePlay(src_path, src_file, begin_str, end_str, dst_str):
	'''
	# 安卓工程批量代码替换
	- src_path:源文件所在工程的目录
	- src_file:源文件名
	- begin_str:需要匹配的代码的开始部分
	- end_str:需要匹配的代码的结束部分
	- dst_str:想要替换的代码
	'''
	allChannels = getNeedChannels()
	for dir in allChannels:
		_target_file = dirAppPlay + "/" + dir + "/" + src_path + "/" + src_file
		target_file = os.path.realpath(_target_file)

		print("")
		print(target_file)
		
		try:
			rf = open(target_file, 'r', encoding='UTF-8')
			s = rf.read()
			rf.close()
		except Exception as ex:
			print("error: can not read file %s, ex = %s" % (target_file, ex))
			continue
		
		
		ind0 = s.find(begin_str)
		ind1 = s.find(')', ind0, -1)

		str0 = s[:ind0]
		str1 = s[ind0:ind1+1]
		str2 = s[ind1+1:]

		need_str = str0 + dst_str + str2
		print('1------str2 = ' + str2)

		try:
			wf = open(target_file, 'w', encoding='UTF-8')
			wf.write(need_str)
			wf.close()
		except Exception as ex:
			print("error: con not write file '%s'" % ex)

def codeAdd(src_path, src_file, flag, dst_str):
	'''
	# 添加代码
	- src_path:源文件所在工程的目录
	- src_file:源文件名
	- flag:添加代码的位置
	- dst_str:需要添加的代码
	'''
	root_paht = os.path.realpath(os.path.join(os.path.dirname(__file__), '../..'))
	target_path = os.path.join(root_paht, src_path)

	for fileName in os.listdir(target_path):
		target_file = os.path.join(target_path, fileName)

		print(target_file)

		try:
			rf = open(target_file, 'r', encoding='UTF-8')
			s = rf.read()
			rf.close()
		except Exception as ex:
			print(ex)

		# print(s.find("install"))
		
		if s.find("%1%") > 0:
			print('----')
		elif s.find("android") > 0:
			s = s + " %1%"
		else:
			s = s + " android-19 %1%"

		print(s)

		try:
			wf = open(target_file, 'w', encoding='UTF-8')
			wf.write(s)
			wf.close
		except Exception as ex:
			print(ex)
		

		
		
			
		
# codePlay("src/org/appplay/lib", "AppPlayBaseActivity.java", "public static void LoadSdkAD", ")", "public static void LoadSdkAD(int platformId, int positionId)")
codeAdd("ApkBuilderScripts/projects_build_1", "hahaha", "hahaha", "hahaha")