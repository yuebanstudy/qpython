#-*-coding:utf8;-*-
#qpy:3
#qpy:webapp:Sample 
#qpy://localhost:8080/
"""
This is a sample for qpython webapp
"""
from bottle import route, run
from ip import get_IP
from sms import zfb_get,get_count
ip = get_IP()

@route('/')
def hello():
	body = zfb_get(get_count())
	return body

	

run(host=ip, port=8080) 
