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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

def creat_list(input_list1,input_list2):
	"""
	将列表中元素放入新列表中
	"""
	new_list = []
	for index in range(len(input_list1)):
		new_list.append(input_list1[index][0])
		new_list.append(input_list1[index][1])
	for index in range(len(input_list2)):
		new_list.append(input_list2[index][0])
		new_list.append(input_list2[index][1])
	return new_list

#所有电话号码的列表
telephone_list = creat_list(texts,calls)
#创建电话号码的集合
telephone_set = set(telephone_list)
print("There are {} different telephone numbers in the records.".format(len(telephone_set)))

	
