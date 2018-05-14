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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""
def creat_list(input_list,number):
	"""获得所有主叫号码的列举"""
	new_list=[]
	for element in input_list:
		new_list.append(element[number])
	return new_list
calls_telephone=[]
#主叫号码列表
calls_first_list=creat_list(calls,0)
#被叫号码列表
calls_second_list=creat_list(calls,1)
#主发短信的号码列表
texts_first_list=creat_list(texts,0)
#被发短信的号码列表
texts_second_list=creat_list(texts,1)
#遍历集合找出符合条件的号码放到列表中
for element in calls_first_list:
	if "140" in element:
		if " " not in element:
			if "(" not in element:
				calls_telephone.append(element)
	if element not in calls_second_list:
		if element not in texts_first_list:
			if element not in texts_second_list:
				calls_telephone.append(element)
all_set= set(calls_telephone)
all_list=[]
for element in all_set :
	all_list.append(element)

#按字母顺序输出
telephoneStr=""
for elements in sorted(all_list):
	telephoneStr = telephoneStr + elements + "\n"
print("These numbers could be telemarketers:\n{}".format(telephoneStr))
			