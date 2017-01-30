import urllib.request,socket
import urllib.parse, re, urllib

socket.setdefaulttimeout(20000)


def fixScan():
    data = b"[ACT_WLAN_SCAN#1,1,0,0,0,0#0,0,0,0,0,0]0,0\r\n"
    url = 'http://192.168.1.222/cgi?7'
    headers = {'Host': '192.168.1.222',
               'Connection': 'keep-alive',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Cookie': 'Authorization=Basic MTIzNDU2Nzg5OTg3NjU0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
               'Content-Type': 'text/plain; charset=UTF-8',
               'Cache-Control':'no-cache',
               'Content-Length': '44',
               'Pragma':'no-cache',
               'Referer': 'http://192.168.1.222/',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
               }

    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req,timeout=20000)
    compressedData = response.read().decode("utf-8")
    if compressedData == '[error]0':
        print('扫描成功！\n')
    else:
        print("扫描失败,请断电重试\n")


def getChannel():
    data = b"[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]0,1\r\n" + b"name\r\n" + b"[LAN_WLAN_BSSDESC_ENTRY#0,0,0,0,0,0#0,0,0,0,0,0]1,5\r\n" + b"X_TP_SSID\r\n" + b"X_TP_BSSID\r\n" + b"X_TP_SecurityEnable\r\n" + b"X_TP_Channel\r\n" + b"X_TP_RSSI\r\n"

    url = 'http://192.168.1.222/cgi?5&5'
    headers = {'Host': '192.168.1.222',
               'Connection': 'keep-alive',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Cookie': 'Authorization=Basic MTIzNDU2Nzg5OTg3NjU0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
               'Content-Type': 'text/plain; charset=UTF-8',
               'Content-Length': '167',
               'Referer': 'http://192.168.1.222/',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
               }

    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    compressedData = response.read().decode("utf-8")
    pattern = re.compile(
            "X_TP_SSID=ChinaNet-jmgS\s+\w+=\w+:\w+:\w+:\w+:\w+:\w+\s+X_TP_SecurityEnable=1\s+X_TP_Channel=\d*")
    find = re.findall(pattern, compressedData)
    try:
        r_td = re.compile('X_TP_SSID=ChinaNet-jmgS\nX_TP_BSSID=9C:28:EF:58:10:10\nX_TP_SecurityEnable=1\nX_TP_Channel=')
        c = r_td.sub('', find.pop())
    except IndexError:
        fixScan()
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        compressedData = response.read().decode("utf-8")
        pattern = re.compile(
            "X_TP_SSID=ChinaNet-jmgS\s+\w+=\w+:\w+:\w+:\w+:\w+:\w+\s+X_TP_SecurityEnable=1\s+X_TP_Channel=\d*")
        find = re.findall(pattern, compressedData)
        r_td = re.compile('X_TP_SSID=ChinaNet-jmgS\nX_TP_BSSID=9C:28:EF:58:10:10\nX_TP_SecurityEnable=1\nX_TP_Channel=')
        c = r_td.sub('', find.pop())

    return c


def getSetData(channel):
    data = b"[LAN_WLAN#1,1,0,0,0,0#0,0,0,0,0,0]0,11\r\n" + b"SSID=MERCURY_9E4308\r\n" + b"Standard=n\r\n" + b"X_TP_11nOnly=0\r\n" + b"AutoChannelEnable=0\r\n" + b"Channel=" + (
        channel.encode(
                "utf8")) + b"\r\n" + b"X_TP_Bandwidth=Auto\r\n" + b"Enable=1\r\n" + b"SSIDAdvertisementEnabled=1\r\n" + b"WMMEnable=1\r\n" + b"X_TP_WdsBridgeEnable=1\r\n" + b"X_TP_FragmentThreshold=2346\r\n" + b"[LAN_WLAN_WDSBRIDGE#1,1,0,0,0,0#0,0,0,0,0,0]1,6\r\n" + b"X_TP_BridgeBSSID=9C:28:EF:58:10:10\r\n" + b"X_TP_BridgeSSID=ChinaNet-jmgS\r\n" + b"X_TP_BridgeAuthMode=PSKAuthentication\r\n" + b"X_TP_BridgeEncryptMode=TKIPEncryption\r\n" + b"X_TP_BridgeKey=mfjgtjs4\r\n" + b"X_TP_BridgeWepKeyIndex=1\r\n"
    return data


def setAll(data):
    url = 'http://192.168.1.222/cgi?2&2'
    headers = {'Host': '192.168.1.222',
               'Connection': 'keep-alive',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Cookie': 'Authorization=Basic MTIzNDU2Nzg5OTg3NjU0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
               'Content-Type': 'text/plain; charset=UTF-8',
               'Content-Length': '491',
               'Referer': 'http://192.168.1.222/',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
               }
    req = urllib.request.Request(url, data, headers)
    try:
        response = urllib.request.urlopen(req,timeout=20000)
        compressedData = response.read().decode("utf-8")
        if compressedData == '[error]0':
            print('修改成功！\n')
        else:
            print("修改失败,请重新设置\n")
    except socket.error:
        print("修改完成!(exception)")

print("程序开始运行...")
try:
    fixScan()
except socket.error:
    print("返回超时,继续下一步 ")


try:
    channel = getChannel()
except urllib.error.HTTPError:
    print(" 认证结束,开始扫描")
    channel = getChannel()

print("获取信道数,")
setdata = getSetData(channel)
print("获取填充数据成功,开始设置\n")
setAll(setdata)
print("(按返回键退出程序-然后选择No)")
