import socket
import time
import psutil
import json
import sys

ip=""
port=5656

if(len(sys.argv)>1  ):
    ip=sys.argv[1]
if(len(sys.argv)>2  ):
    port=int(sys.argv[2])

waitConnnectTime=2
socket.setdefaulttimeout(waitConnnectTime)

def getCpuInfo():
    cpuRate = psutil.cpu_percent(None)
    return cpuRate

def getMemoryInfo():
    memoryRate = psutil.virtual_memory().percent
    return memoryRate;
def getDisRateInfo():
    disRate = psutil.disk_usage("/home")
    return disRate
def getHostName():
    hostname=socket.gethostname()
    return hostname
def doConnect(host,port):
    the_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        the_socket.connect((host,port))
    except:
        time.sleep(waitConnnectTime)
        print("连接失败,%s秒后重新尝试建立链接"%(waitConnnectTime))
        doConnect(host,port)
    return the_socket

def send(ip,port):
    the_socket=doConnect(ip,port)
    while True:
        try:
            jsonStr = {'hostname':getHostName(),'cpu': getCpuInfo(), 'memory': getMemoryInfo()}
            the_socket.send(str(json.dumps(jsonStr)).encode('utf-8'))
        except socket.error:
            print("正在尝试重新建立连接.....")
            the_socket = doConnect(ip,port)
            time.sleep(waitConnnectTime)

        time.sleep(waitConnnectTime)
if __name__ == '__main__':
    print("start... ip is %s port is %s"%(ip,port))
    send(ip,port)



