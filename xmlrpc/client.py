# -*- coding=utf-8 -*-'''

import xmlrpc.client
import datetime
""":type:xmlrpcdemo.client"""
with xmlrpc.client.ServerProxy("http://localhost:9001/") as proxy:
    print(type(proxy))
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))
    today = proxy.today()
    converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
    print(today,  converted)
    print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))
