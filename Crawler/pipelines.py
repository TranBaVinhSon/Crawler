# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class CrawlerPipeline(object):
	
	def __init__(self):
     	
    def process_item(self, item, spider):
    	# valid = True
    	# for data in item:
    	# 	if not data:
    	# 		valid = False
    	# 		raise DropItem("Missing {0}!".format(data))
    	# if valid:
    	# 	self.connection.insert(dict(item))
    	# 	log.msg("Link add to MongoDB!", level = log.DEBUG, spider = spider)
        return item

