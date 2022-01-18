# encoding: utf-8
import os
import numpy as np
import pandas as pd
import shutil

file_path='/Users/user/Desktop/Notes' #文件路径
filename_path='/Users/user/Desktop/filename.xlsx' #文件列表

filelist=os.listdir(file_path)  #获取文件夹中的文件名称
file_name=pd.read_excel(filename_path) #读取所需文件列表

file_name['count']=0 #定义新的一列count，用于计数



for file in filelist:
 m=file_name.shape[0] #表格的行数
 olddir=os.path.join(file_path,file) #每一个文件路径
 for i in range(m):
  if str(file_name['name'][i]) in file: #寻找对应的文件名
   F="/Users/user/Desktop/myfiles_filter/" #新文件夹名称（先建好）
   newdir=os.path.join(F,file)
   shutil.copy(olddir,newdir)  #复制到新文件夹中
   file_name['count'][i]=file_name['count'][i]+1 #计数
   print(file) #打印出文件名，其实我是为了看它是不是在运行
  else:
   continue

file_name.to_excel('file_name_count.xlsx')  #保存新的文件列表