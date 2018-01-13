# Simple-wikicrawler
A simple crawler which is used to attain wiki entries.

开始时Vicia遇到的错误是mysql提示句法错误，
 >Insert error: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '),'',{},'25 May 2015,23:48',(),('Bromeliaceae cultivar','Aechmea stubs'))' at line 1")
 
其原因是不支持存储字典及列表或字符集不匹配，将其转换为str即可（也有转为utf-8编码的功能）
顺便将里面看着碍眼的"\n"全删了233
```
item["url"] = str(url)
item["name"] = str(name)
item["summary"] = re.sub(r'\\n', '', str(summary), count=0, flags=0)
item["info"] = re.sub(r'\\n', '', str(info), count=0, flags=0)
item["content"] = re.sub(r'\\n', '', str(content), count=0, flags=0)
item["uptime"] = str(uptime)
item["refer"] = re.sub(r'\\n', '', str(refer), count=0, flags=0)
item["label"] = str(label)
```
稍微修改了一下数据库的表，
```
CREATE TABLE `wiki_EN` (
  `sequence` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(80) NOT NULL DEFAULT '',
  `names` varchar(100) NOT NULL DEFAULT '',
  `summary` text,
  `info` text,
  `content` text,
  `uptime` varchar(30) NOT NULL DEFAULT '',
  `refer` text,
  `label` varchar(500) DEFAULT '',
  PRIMARY KEY (`sequence`)
) ENGINE=InnoDB AUTO_INCREMENT=10660 DEFAULT CHARSET=utf8;
```
把一些可能特别长的结果类型换为了text型

同时需要注意一下我的数据库名为"wiki_entries"，表为"wiki_EN"，密码为1，并加了序列号作为主键
