import tkinter as t
import urllib.request
import urllib.parse
import json

def get_result(words):
	url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
	data={}
	data['i']=words
	data['from']='AUTO'
	data['to']='AUTO'
	data['smartresult']='dict'
	data['client']='fanyideskweb'
	data['salt']='1505051652168'
	data['sign']='69c88cbc6dc79b2c84b12a2750ed7ec'
	data['doctype']='json'
	data['version']='2.1'
	data['keyfrom']='fanyi.web'
	data['action']='FY_BY_CLICKBUTTION'
	data['typoResult']='true'
	data['response']='urllib.request.urlopen'
	header={}
	header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
	header['Accept']='application/json, text/javascript, */*; q=0.01'
	header['Accept-Encoding']='gzip, deflate'
	header['Accept-Language']='zh-CN,zh;q=0.8'
	header['Connection']='keep-alive'
	header['Content-Length']='215'
	header['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
	header['Cookie']='OUTFOX_SEARCH_USER_ID=2143487715@180.160.41.109; P_INFO=gba-mqz-kdyg@163.com|1492505008|2|caipiao|11&10|shh&1492504434&mail_client#shh&null#10#0#0|132132&0||gba-mqz-kdyg@163.com; OUTFOX_SEARCH_USER_ID_NCOO=941993755.956503; _ntes_nnid=f6d107d35d91013604a80481322ff398,1501842741770; JSESSIONID=aaamg83Z346uT5Ok4cS5v; ___rl__test__cookies=1505051652156'
	header['Host']='fanyi.youdao.com'
	header['Origin']='http://fanyi.youdao.com'
	header['Referer']='http://fanyi.youdao.com/'
	header['X-Requested-With']='XMLHttpRequest'
	
	data=urllib.parse.urlencode(data).encode('utf-8')
	response=urllib.request.urlopen(url,data)
	html=response.read().decode('utf-8')
	result=json.loads(html)
	return (result['translateResult'][0][0]['tgt'])
	
def print_result(words,label):
	label['text']='翻译结果：'+words
	
def copy(root,text):
	root.clipboard_clear()
	root.clipboard_append(text)
	
def main():
	root=t.Tk()
	root.title('Mini Translator')
	f1=t.Frame()
	f1.pack()
	l1=t.Label(f1,text='请输入待翻译文本：')
	l1.pack(side='left')
	e1=t.Entry(f1)
	e1.pack(side='right')
	b1=t.Button(root,text='确定',command=lambda:print_result(get_result(e1.get()),l2),relief="raised")
	b1.pack()
	l2=t.Label(root,text='翻译结果：')
	l2.pack()
	b2=t.Button(root,text='复制到剪贴板',command=lambda:copy(root,l2['text'].split('：')[1]),relief="raised")
	b2.pack()
	root.mainloop()
	
	
main()