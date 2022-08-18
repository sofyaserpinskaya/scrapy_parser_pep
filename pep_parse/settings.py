from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = Path('results')

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEED_URI_PARAMS = 'pep_parse.utils.uri_params'

FEEDS = {
    RESULTS_DIR / 'pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
