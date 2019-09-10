import datetime
import schedule
import threading
from kafka import KafkaProducer
import json
import esUtils
import time
# 引入  kafka  采集信息  发送采集数据
# 1.采集系统信息
# 2.采集mysql  采集redis  采集elaticsearch数据
# 3.平台开发  黄河大桥 协议
#

# jsonStr = {"hostname": mySocket.getHostName(), "cpu": mySocket.getCpuInfo(), "memory": mySocket.getMemoryInfo()}
# print(jsonStr)
# producer.send('edge_server_info', jsonStr)

kafkaAddress='39.98.161.145:9092'

isConnect=False;
producer=None
def connect():
    try:
        producer = KafkaProducer(bootstrap_servers=['39.98.161.145:9092'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))
        isConnect=True
    except :
        isConnect=False
        print("2s后尝试重新建立连接")
        time.sleep(2)
        connect()


#_source

#定
def sendServerInfoJob():
    esData=esUtils.selectEsData()
    for item in esData:
        if isConnect:
            try:
                 producer.send("esData",item['_source'])
            except:
                connect()
    print("send complete")
    print("job1:", datetime.datetime.now())


def job1_task():
    threading.Thread(target=sendServerInfoJob).start()

def run():
    schedule.every(10).seconds.do(job1_task)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    connect()
    run()



