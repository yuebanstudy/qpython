#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import android
import time





#sms_data = {
#	'id':id
#	'thread_id':thread_id,
#	'association_id':association_id,
#	'address':address,
#	'person':person,
#	'date':date,
#	'date_sent':date_sent,
#	'protocol':protocol,
#	'read':read,
#	'status':status,
#	'type':type,
#	'reply_path_present':reply_path_present,
#	'subject':subject,
#	'body':body,
#	'service_center':service_center,
#	'locked':locked,
#	'error_code':error_code,
#	'report_date'report_date,
#	'port'：port,
#	'seen'：seen,
#	'sync_ver'：sync_ver,
#	'uuid'：uuid,
#	'group_msg_id'：group_msg_id,
#	'imsi'：imsi,
#	'is_favorite'：is_favorite,
#	'sim_id':is_favorite,
#	'sub_id':sub_id,
#	'creator':creator
#}


#data_string = json.dumps(sms_data)


'''
	_id：短信序号，如100
　　
　　thread_id：对话的序号，如100，与同一个手机号互发的短信，其序号是相同的
　　
　　address：发件人地址，即手机号，如+86138138000
　　
　　person：发件人，如果发件人在通讯录中则为具体姓名，陌生人为null
　　
　　date：日期，long型，如1346988516，可以对日期显示格式进行设置
　　
　　protocol：协议0SMS_RPOTO短信，1MMS_PROTO彩信
　　
　　read：是否阅读0未读，1已读
　　
　　status：短信状态-1接收，0complete,64pending,128failed
　　
　　type：短信类型1是接收到的，2是已发出
　　
　　body：短信具体内容

	service_center：短信服务中心号码编号，如+8613800755500
'''

droid = android.Android()

def get_count():
	GetMessageCount = droid.smsGetMessageCount(False)
	Count = GetMessageCount.result
	return Count
		
def get_sms(ID):
	GetMessageById = droid.smsGetMessageById(ID)
#	read = GetMessageById.result["read"]
	body = GetMessageById.result["body"]
	address = GetMessageById.result["address"]
	if address != '95188':
		return None
	else:
		return body
		

def zfb_get(Count):
	GetMessageIds = droid.smsGetMessageIds(False)
	ID = GetMessageIds.result
	for cou in range(Count):
		t = ID[cou]
		body = get_sms(t)
		if body is None:
			continue
		else:
			return body
			break

		
		
	