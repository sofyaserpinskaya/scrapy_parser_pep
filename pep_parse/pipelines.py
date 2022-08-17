from collections import defaultdict
from datetime import datetime

from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, RESULTS_DIR


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILENAME = 'status_summary_{time}.csv'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        if 'status' not in item:
            raise DropItem('No status.')
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            BASE_DIR / RESULTS_DIR / FILENAME.format(
                time=datetime.now().strftime(DATETIME_FORMAT)
            ),
            mode='w',
            encoding='utf-8'
        ) as file:
            file.write('Статус,Количество\n')
            for status, number in sorted(self.results.items()):
                file.write(f'{status},{number}\n')
            file.write(f'Total,{sum(self.results.values())}\n')
