# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

class FilePipeline(object):
    def process_item(self, item, spider):
        
        host = settings['MYSQL_HOSTS']  
        user = settings['MYSQL_USER']  
        psd = settings['MYSQL_PASSWORD']  
        db = settings['MYSQL_DB']  
        c = settings['CHARSET']  
        port = settings['MYSQL_PORT']
        
        #数据库连接  
        con = pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)   
        #操作的游标
        cue = con.cursor()  
        
        print("!!!mysql connect success")

        try:
            sql = 'insert into wiki_EN (url,names,summary,info,content,uptime,refer,label) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            parameters = (item["url"], item["name"], item["summary"], item["info"], item["content"], item["uptime"], item["refer"], item["label"])
            cue.execute(sql,parameters)

   
        except Exception as e:  
            print('Insert error:',e)  
            con.rollback()
        else:  
            con.commit()  
        
        con.close()         
        return item
