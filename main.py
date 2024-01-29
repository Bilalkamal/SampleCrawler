# main.py

from src.crawler import Crawler
import json
import os


def main():
    os.makedirs('data', exist_ok=True)
    urls = [urls for urls in json.load(open('urls.json'))]
    for url in urls:
        crawler = Crawler(url)
        crawler.crawl()
        crawler.collect_data()
        data = crawler.get_data()
    
        with open('data/' + crawler.article.title + '.json', 'w') as outfile:
            json.dump(data, outfile)

if __name__ == '__main__':
    main()