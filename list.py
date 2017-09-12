import datetime
import glob
import pandas as pd
import json
import csv
import codecs
def get_retrieved_urls():
    alldf = pd.DataFrame()
    csv_files = glob.glob('data/posts/*.csv')
    posts = []
    ids = set()
    for csv_file in csv_files:
        with codecs.open(csv_file, 'r',encoding='UTF-8') as csvr:
            sreader = csv.DictReader(csvr)
            for row in sreader:
                if row['id'] not in ids:
                    post = {'title' : u"{}".format(row['title']),
                            'text' : u"{}".format(row['content']),
                            'tags' :  u"{}".format(row['tags']),
                            'url': u"{}".format(row['url']),
                            'id': u"{}".format(row['id'])

                            }
                    posts.append(post)
                    ids.add(row['id'])

    mmap = {"posts": posts}
    return mmap

mmap = get_retrieved_urls()



with  codecs.open('tech_posts_4.json', 'wb',encoding='UTF-8') as f:
    json.dump(mmap, f, ensure_ascii=False)
