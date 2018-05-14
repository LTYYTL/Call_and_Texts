"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#第一条短信的发送电话号码
texts_incoming_number = texts[0][0]
#第一条短信的接收电话号码
texts_answering_number = texts[0][1]
#第一条短信的短信的时间戳
texts_time = texts[0][2]
#输出第一条短信的内容
print("First record of texts, {} texts {} at time {}".format(texts_incoming_number,texts_answering_number,texts_time))

#最后一条通话的主叫电话号码
calls_incoming_number = calls[-1][0]
#最后一条通话的被叫电话号码
calls_answering_number = calls[-1][1]
#最后一条通话的电话开始的时间截
calls_time = calls[-1][2]
#最后一条通话的电话持续时间
calls_during = calls[-1][3]
#最后一条通话的内容
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls_incoming_number,calls_answering_number,calls_time,calls_during))
