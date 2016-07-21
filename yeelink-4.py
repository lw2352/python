#python2

import os
import requests
import json,time,string
import commands

#获取cpu温度
def getcputemperature():
    cputemp=os.popen('vcgencmd measure_temp').readline()
    sumcputemp=cputemp.replace("temp=","").replace("'C\n","")
    return sumcputemp

#获取CPU使用情况
def getCPUuse():  
        return(os.popen("top -n1"))#获取CPU的情况的函数  
    
#获取RAM使用情况
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
            
#apikey为用户id
apiheaders={'U-ApiKey':'71572dde6dfbf42a0979f56f10ed4e28','content-type': 'application/json'}

#CPU温度使用 392295传感器
cputemp_apiurl="http://api.yeelink.net/v1.1/device/349924/sensor/392295/datapoints"
#gpu温度使用392296传感器
gputemp_apiurl="http://api.yeelink.net/v1.1/device/349924/sensor/392296/datapoints"

#cpu占用率使用 392297 传感器
CPUusage_apiurl="http://api.yeelink.net/v1.1/device/349924/sensor/392297/datapoints"
#RAM占用率使用 392300传感器
RAMusage_apiurl="http://api.yeelink.net/v1.1/device/349924/sensor/392300/datapoints"

if __name__=='__main__':
    while 1:
        #上传cpu温度
        cpu_temp=getcputemperature()
        cputemp_payload={'value':cpu_temp}
        r=requests.post(cputemp_apiurl, headers=apiheaders, data=json.dumps(cputemp_payload))
        print ("cpu_temp:",cpu_temp)

        #上传gpu温度
        gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
        gpu_temp = float(gpu_temp)
        gputemp_payload = {'value': gpu_temp}
        r = requests.post(gputemp_apiurl, headers=apiheaders, data=json.dumps(gputemp_payload))
        print ("gpu_temp:",gpu_temp)
        
        #上传cpu占用率及RAM占用率
        CPU_usage = getCPUuse()
        
        for cpuline in CPU_usage:  
          if cpuline[:3]=="%Cp":  
            CPU_usage=cpuline.split(":")[1].split(",")[0].split(" ")[-2]  
        
        CPUusage_payload = {'value': CPU_usage}
        r=requests.post(CPUusage_apiurl, headers=apiheaders, data=json.dumps(CPUusage_payload))
        print ("CPU_usage:",CPU_usage)
        
        RAM_stats = getRAMinfo()
        RAM_total = round(int(RAM_stats[0]) / 1000,1)       
        RAM_used = round(int(RAM_stats[1]) / 1000,1)
        RAM_usage = (RAM_used/RAM_total)*100
        RAMusage_payload = {'value':RAM_usage}
        r=requests.post(RAM_usage_apiurl, headers=apiheaders, data=json.dumps(RAMusage_payload))
        print ("RAM_usage:",RAM_usage)
        
        print(>-<>-<>-<>-<>-<>-<>-<>)
        
        
        
        time.sleep(5)  #距离下一次采集的时间


        #http://shumeipai.nxez.com/2014/10/04/get-raspberry-the-current-status-and-data.html
        #http://www.cnblogs.com/xiaowuyi/p/4020499.html
