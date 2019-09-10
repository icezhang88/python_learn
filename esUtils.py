from elasticsearch import Elasticsearch
from elasticsearch import helpers
import time
import urllib3
import json
import requests


# curl -XPUT -H "Content-Type: application/json" http://:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
#now_timestamp-timePeriod
es=Elasticsearch([{'host':'192.168.1.210','port':9200}])

timePeriod=10*60*1000
now_timestamp=int(round(time.time() * 1000))

body={
    "query": {
        "bool": {
            "must": [
                {
                    "range": {
                        "utcTime": {
                            "gte": 0,
                            "lt": now_timestamp
                        }
                    }
                }
            ],
            "must_not": [],
            "should": []
        }
    },
    "from": 0,
    "size": 100,
    "sort": [],
    "aggs": {}
}



def selectEsData():
    result=es.search(index='cars',body=body)
    carsArray=result['hits']['hits']
    return carsArray






