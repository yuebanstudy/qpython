#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import android
import time
import socket
import struct


def get_IP():
	droid = android.Android()
	#获取手机wifi的地址
	result = droid.wifiGetConnectionInfo()
	ip = result.result["ip_address"]
	#将int的ip转换为str
	ip_address = socket.inet_ntoa(struct.pack("=I", ip))
	return ip_address
