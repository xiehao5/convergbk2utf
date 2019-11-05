# convergbk2utf
Convert GBK encode file to UTF8
将GBK编码的文件转换为UTF8编码


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

WARNING!!!

1、不要尝试转换二进制文件的编码，程序会崩溃。
2、如果被转换文件已存在编码错误，比如说字符编码套圈，或者文件中存在乱码，
	则该转换程序的结果不可预测，有可能报错，也有可能生成一个乱码文件。
3、执行字符编码转换前，请备份被转换的文件，本程序无法保证编码转换结果无误，
	程序作者不对程序执行结果负责。
4、执行字符编码转换后一定要用类似Beyond Compare这样的工具进行对比，防止错误转换为乱码。

