BOT_NAME = "metallurg_moskva"

SPIDER_MODULES = ["metallurg_moskva.spiders"]
NEWSPIDER_MODULE = "metallurg_moskva.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
   'metallurg_moskva.pipelines.PGPipeline': 300,
}
