from futu import *
import pandas as pd

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)


# code =  'HK.00700'
code =  'HK.01157'
# startDate = '2019-09-11'
startDate = None
# endDate = '2019-09-18'
endDate = None

ret, data, page_req_key = quote_ctx.request_history_kline(
	code, start=startDate, end=endDate, ktype=KLType.K_1M, max_count=1000)  # 5 per page, request the first page
if ret == RET_OK:
    # print(data)
    print(data['code'][0])  # Take the first stock code
    # The closing price of the first page is converted to a list
    # print(data['close'].values.tolist())
else:
    print('error:', data)

while page_req_key != None:  # Request all results after
    print('*************************************')
    ret, data1, page_req_key = quote_ctx.request_history_kline(
	code, start=startDate, end=endDate, ktype=KLType.K_1M, max_count=1000, page_req_key=page_req_key)  # Request the page after turning data
    if ret == RET_OK:
        # print(data1)
        data = pd.concat([data, data1])
    else:
        print('error:', data1)

print('All pages are finished!')

# print(data)
filePath = f'./examples/data/k_line/K_1M/{code}'
if not(os.path.exists(filePath) and os.path.isdir(filePath)):
	os.mkdir(filePath)

filePath = f'{filePath}/{code}.csv'
data.to_csv(filePath, index=False)

quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
