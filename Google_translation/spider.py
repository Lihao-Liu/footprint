'''
This file is a crawler
Author: Lihao Liu
2020.3.17
'''
import requests
from tk_crack import Py4Js

def handle_input_test(original_test):
    handle_text=original_test.replace('\n',' ',999)
    # print(handle_text)
    return handle_text
def handle_url_method(handle_text):
    handle_url=handle_text.replace(' ','%20',999)
    # print(handle_url)
    return handle_url
def spider_translate(original_text):
    #处理输入信息中的回车
    handle_text = handle_input_test(original_text)
    # 破解tk参数
    js=Py4Js()
    tk=js.getTk(handle_text)
    #拼凑url
    handle_url=handle_url_method(handle_text)
    #请求内容
    r=requests.get(url='https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=2&ssel=3&tsel=0&kc=5&tk='+tk+'&q='+handle_url)
    # print('statys_code:',r.status_code)
    # print(r.text)
    response=r.text.split('"')
    # print(response)
    return response[1],r.status_code