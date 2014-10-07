SensitivePy
===========

使用python开发的极简的敏感词过滤系统
-----------

API LIST
-----------
1.检测敏感词<br />
URL   http://your_domain/check<br />
参数名         请求类型        可选            长度<br />
words   POST   false  65535
<br />
返回格式：json<br />
{"count":1,"data":[[0,6,"\u6bcd\u5b5d"]]}
<br />
2.过滤敏感词<br />
URL   http://your_domain/replace<br />
参数名         请求类型        可选            长度<br />
words   POST   false  65535<br />
返回格式：text<br />
**这是已经过滤的文本**,还好<br />

words.txt为敏感词文件<br />

### 安装说明<br />
先通过pip或easy_install安装bottle框架<br />
再修改localbottle里的端口设置和域名设置，再使用python 启动即可<br />
*通过云环境的需要修改一下配置，保留wsgi.py，具体参考云环境的说明<br />

### 更新说明<br />
2014/10/7  <br />
1.完成核心检测和过滤API<br />
2.集成bottle框架<br />
3.检测使用DFA过滤算法<br /><br />

<br />
重庆尚简科技工作室(http://www.sj-kj.com) caroltc(312493732@qq.com)