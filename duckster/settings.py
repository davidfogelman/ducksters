# Scrapy settings for duckster project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'duckster'

SPIDER_MODULES = ['duckster.spiders']
NEWSPIDER_MODULE = 'duckster.spiders'


# DOWNLOADER_MIDDLEWARES = {
#     # 'misc.middleware.CustomHttpProxyMiddleware': 400,
#     'misc.middleware.CustomUserAgentMiddleware': 401,
# }

ITEM_PIPELINES = {
    'duckster.pipelines.JsonWithEncodingPipeline': 300,
    # 'duckster.pipelines.RedisPipeline': 301,
}


LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1
