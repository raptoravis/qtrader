from futu import *
import pandas as pd

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

# print(quote_ctx)

#请求开头50个数据
ret, data, page_req_key = quote_ctx.request_history_kline('SH.510050', start='2005-09-30', end='2019-05-05',max_count=1000)
print(data)

ret, data2, page_req_key = quote_ctx.request_history_kline('SH.510050', start='2005-09-30', end='2019-05-05',max_count=1000,page_req_key=page_req_key) 
print(data2)

ret, data3, page_req_key = quote_ctx.request_history_kline('SH.510050', start='2005-09-30', end='2019-05-05',max_count=1000,page_req_key=page_req_key) 
print(data3)

result = pd.concat([data, data2, data3])

file = open('50ETF.json', 'w')
file.write(str(result.to_json(orient='records')))
file.close()