计算机科学与技术学院*自然语言处理*课程实验报告

 

| 实验题目：实验三                                                                                                                                                                                                                    | 学号：201600130053 |             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-------------|
| 日期：2019/03/26                                                                                                                                                                                                                    | 班级： 2016智能班  | 姓名： 王斌 |
| Email：935681396\@qq.com                                                                                                                                                                                                            |                    |             |
| 实验目的： 要求：利用 Chinese.txt 和 English.txt 的中英文句子，在实验二的基础上，继 续利用以下给定的中英文工具进行词性标注和命名实体识别。并对不同工具产生 的结果进行简要对比分析，将实验过程与结果写成实验报告，实验课结束后提交。 |                    |             |
| 实验软件和硬件环境：  **一、硬件环境： **                                                                                                                                                                                           |                    |             |
| 实验原理和方法： 1、英文工具： Nltk： Spacy： Stanfordnlp： 2、中文工具：（部分工具命名实体识别没有直接调用的函数，可以根据词性 标注的结果自己实现）                                                                                |                    |             |
| 实验步骤：（不要求罗列完整源代码）                                                                                                                                                                                                  |                    |             |
| 结论分析与体会：                                                                                                                                                                                                                    |                    |             |
| 就实验过程中遇到和出现的问题，你是如何解决和处理的，自拟1－3道问答题：                                                                                                                                                              |                    |             |

>   CPU

>   Intel Core i5 7200U \@ 2.50GHz 41 °C

>   Kaby Lake-U/Y 14nm工艺

>   RAM

>   8.00GB 单个的-通道 未知 (15-15-15-35)

>   主板

>   HP 81D1 (U3E1)

>   图像

>   Generic PnP Monitor (1920x1080\@60Hz)

>   Intel HD Graphics 620 (HP)

>   存储器

>   476GB NVMe THNSN5512GPUK TO (未知)

>   40GB Microsoft 虚拟磁盘 (File-backed Virtual)

>   光盘驱动器

>   没有检测到光纤磁盘驱动

>   音频

Conexant ISST Audio

**二、软件环境：**

>   主机操作系统

>   Windows 10 家庭中文版 64-bit

平台编程环境

anaconda + python3.7

>   Jieba：

>   StanfordCoreNLP：

>   SnowNLP：

>   THULAC：

>   NLPIR：

>   HanLP（选做，需要 Microsoft Visual C++ 14.0）

1.  python工具包下载安装准备：

>   **（1）nltk**的命名实体功能模块安装：

![](media/717fbf35dded1de2f9c7d7278efa4554.png)

>   **（2）pyhanlp**的安装：

>   <https://blog.csdn.net/huangjiajia123/article/details/84144583>

>   第一步：

>   下载
>   jpype：https://www.lfd.uci.edu/\~gohlke/pythonlibs/\#jpype下载对应版本已经编译好的whl文件。

>   将 .whl 文件保存到python 所在的script 文件夹下， 然后安装： pip install
>   【下载的文件名】

>   第二步： 安装 pyhanlp: pip install pyhanlp

>   第三步：
>   安装完成后并不能使用，需要下载一个jar包、data文件和properties文件，因为hanlp是java开发的虽然有python的API但是还是需要java环境，所以需要安装JDK，并配置Java
>   环境变量（即添加一个JAVA_HOME变量，变量值为java的bin目录的绝对路径）。

>   （1）打开 python IDE，输入 import pyhanlp， 会自动下载 HanLP jar
>   和properties 文件，默认放在 python -\>Lib-\>site packages 文件夹下的 pyhanlp
>   -\>static 文件夹下

>   （2）可以将 hanlp-1.7.0.jar 和hanlp.properties
>   移动到一个新的文件夹下，比如： D\\HanLp

>   （3）去https://github.com/hankcs/HanLP/releases 下载 hanlp 的data

1.  进行测试观察结果：

1、中文文本：

![](media/675754439270425c58c5cbdbb5c054e7.png)

![](media/fe9a54049ba9a56fadad962e4c826386.png)

![](media/f5f4a0b7e4d9a49325e0ad81b8b66fb9.png)

![](media/ce1f474b6f6c3351c3ed9cd2c0a07c0e.png)

2、英语文本：

![](media/2bf6f485ff079726301948a70bc159a3.png)

NLTK实体标注树状图：

![](media/638c0d989f6ccb3ee560fefad29ed3e7.png)

1.  结果简单对比分析：

中文文本进行词性标注，对于hanlp、jieba、SnowNLP、StanfordCoreNLP、thulac、pynlpir六种方法的结果观察可以发现，
