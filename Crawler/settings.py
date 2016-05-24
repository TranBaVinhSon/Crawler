BOT_NAME = 'Crawler'

SPIDER_MODULES = ['Crawler.spiders']
NEWSPIDER_MODULE = 'Crawler.spiders'
DOWNLOAD_HANDLERS = {
  's3': None,
}

