# -*- coding:utf-8 -*-

'''
WARNING!!!

1、不要尝试转换二进制文件的编码，程序会崩溃。
2、如果被转换文件已存在编码错误，比如说字符编码套圈，或者文件中存在乱码，
	则该转换程序的结果不可预测，有可能报错，也有可能生成一个乱码文件。
3、执行字符编码转换前，请备份被转换的文件，本程序无法保证编码转换结果无误，
	程序作者不对程序执行结果负责。
4、执行字符编码转换后一定要用类似Beyond Compare这样的工具进行对比，防止错误转换为乱码。

HOWTO
首先安装python3，并将python3安装目录加入PATH，安装过程中请选择安装pip。
在命令行中执行pip install chardet，安装chardet包

命令行执行：

python convergbk2utf.py d:\test
可以将d:\test目录中的所有文件，转码成utf8.

python convergbk2utf.py
可以将当前目录中的所有文件，转码成utf8.

python convergbk2utf.py test.c
可以将test.c，转码成utf8.

'''

__author__ = 'Hank'

import os,sys
import chardet

def convert( filename, out_enc="UTF8" ):
	try:
		print("convert " + filename,)
		content = open(filename, mode="rb").read()
		result = chardet.detect(content)#通过chardet.detect获取当前文件的编码格式串，返回类型为字典类型
		coding = result.get('encoding')#获取encoding的值[编码格式]
		if coding != 'utf-8':#文件格式如果不是utf-8的时候，才进行转码
			print(coding + " to utf-8!",)
			if coding == 'ISO-8859-1':#如果检测到ISO-8859-1编码，按照GB2312解码
				coding = 'GB2312'
				print(filename + " is decode as ISO-8859-1, Please recheck!!!")
			new_content = content.decode(coding).encode(out_enc)
			open(filename, mode="wb").write(new_content)
			print(" done")
		else:
			print(coding)
	except IOError as e:
	# except:
		print("Ooops, something went wrong!" + e)


def explore(dir):
	for root, dirs, files in os.walk(dir):
		for file in files:
			path = os.path.join(root, file)
			convert(path)

def main():
	if len(sys.argv) < 2:
		root_path = os.listdir(".")
	else:
		root_path = sys.argv[1:]

	for path in root_path:
		if os.path.isfile(path):
			convert(path)
		elif os.path.isdir(path):
			explore(path)

if __name__ == "__main__":
	main()

