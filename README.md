SensitivePy
===========

使用python开发的极简的敏感词过滤系统
-----------

API LIST
-----------
1.检测敏感词
URL   http://your_domain/check
参数名         请求类型        可选            长度
worrds   POST   false  65535

返回格式：json
{"count":1,"data":[[0,6,"\u6bcd\u5b5d"]]}

2.过滤敏感词
URL   http://your_domain/replace
参数名         请求类型        可选            长度
worrds   POST   false  65535

返回格式：text
**这是已经过滤的文本**,还好

words.txt为敏感词文件

### 安装说明<br />
先通过pip或easy_install安装bottle框架
再修改localbottle里的端口设置和域名设置，再使用python 启动即可
*通过云环境的需要修改一下配置，保留wsgi.py，具体参考云环境的说明

### 更新说明<br />
2014/10/7  
1.完成核心检测和过滤API
2.集成bottle框架
3.检测使用DFA过滤算法