from scrapy import Spider 
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.http import TextResponse
from scrapy.selector import HtmlXPathSelector

from Crawler.items import CrawlerItem

class ImportExport(Spider):
	name = "importexport"
	allowed_domains = ["thesaigontimes.vn"]
	start_urls = [
		"http://www.thesaigontimes.vn/kinhdoanh/xuatnhapkhau/"
	]

	def parse(self, response):
		base_url = "http://www.thesaigontimes.vn"
		posts = Selector(response).xpath('//div[@class="ARTICLE"]')

		for post in posts:
			postTitle = post.xpath(
				'a[@class="ArticleTitle"]/text()').extract()[0]
			itemFullURL = base_url + post.xpath(
				'a[@class="ArticleTitle"]/@href').extract()[0]
			request = Request(itemFullURL, callback = self.parse_full_post)
			request.meta['title'] = postTitle
			request.meta['url'] = itemFullURL
			
			yield request

	def parse_full_post(self, response):

		fullPost = HtmlXPathSelector(response)
		post_content = fullPost.select(
			'//*[@id="ctl00_cphContent_lblContentHtml"]/p/text()').extract()[0]
		post_time = fullPost.select(
			'//*[@id="ctl00_cphContent_lblCreateDate"]/text()').extract()[0]
		post_author = fullPost.select(
			'//*[@id="ctl00_cphContent_Lbl_Author"]/text()').extract()[0]
	
		item = CrawlerItem()
		item['title'] = response.meta['title'].encode('utf-8')
		item['url'] = response.meta['url'].encode('utf-8')
		item['author'] = post_author.encode('utf-8')
		item['time'] = post_time
		item['content'] = post_content.encode('utf-8')

		yield item
