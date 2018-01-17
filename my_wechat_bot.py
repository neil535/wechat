import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	reply_text = ''
	if msg.text == '你好':
		reply_text = '你好'
	elif msg.text == '你是谁':
		reply_text = '李学艺'
	else:
		reply_text = '哦'
		
	return reply_text

itchat.auto_login()
itchat.run()