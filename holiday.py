# coding=utf-8
"""
从土味情话中获取每日一句。
 """
import requests
import json
from datetime import datetime


__all__ = ['get_lovelive_info']


def get_lovelive_info():
    dt = datetime.now()
    time = dt.strftime('%Y-%m-%d')
    print('获取...')
    try:
        resp = requests.get('http://api.haoshenqi.top/holiday?date='+time)
        if resp.status_code == 200:
            content_dict = resp.json()

            str25 = ""
            data1 = content_dict[0]
            print(data1)
            # 0普通工作日1周末双休日2需要补班的工作日3法定节假日
            if data1['status'] == 1:  # 判断变量是否为 python
                str25 = '周末双休日'  # 条件成立时设置标志为真
                print (str25)
            else:

                if data1['status'] == 0:
                    str25 = '普通工作日'

                else:
                    if data1['status'] == 2:
                        str25 = '需要补班的工作日'

                    else:
                        if data1['status'] == 3:
                            str25 = '法定节假日'
            return str25



    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


get_one_words = get_lovelive_info

if __name__ == '__main__':

    is_tomorrow = get_lovelive_info()
    url = 'https://service-etcne5bg-1254304775.gz.apigw.tencentcs.com/release/Wecom_push'
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    dt = datetime.now()
    time = dt.strftime('%Y-%m-%d')
    # 'application/x-www-form-urlencoded'
    # 'application/json;charset=utf-8'
    FormData = {
        'sendkey': 'akb48',
        'msg_type': 'text',
        'msg': f'今天是-{time}'+'\n'+is_tomorrow

    }

    res = requests.post(url=url, json=FormData)
    # content = requests.post(url=url, data=FormData).text

    print(res.text)

    # print(is_tomorrow)
