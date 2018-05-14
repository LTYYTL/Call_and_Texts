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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
def creat_dictionary(input_list):
	"""
	将列表转换为字典
	"""
	new_dictionary = {}
	for elment in input_list:
		if new_dictionary.get(elment[0]):
			new_dictionary[elment[0]] = new_dictionary.get(elment[0])+int(elment[3])
		else:
			new_dictionary[elment[0]] = int(elment[3])
		if new_dictionary.get(elment[1]):
			new_dictionary[elment[1]] = new_dictionary.get(elment[1])+int(elment[3])
		else:
			new_dictionary[elment[1]] = int(elment[3])
	return new_dictionary
#获得电话时长字典
telephone_time_dictionary = creat_dictionary(calls)
telephone = ""
next_seconds = 0

#遍历字典
for key,value in telephone_time_dictionary.items():
    if value > next_seconds:
        next_seconds = value
        telephone=key
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone,next_seconds))

