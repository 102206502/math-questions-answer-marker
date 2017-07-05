# -*- coding: utf-8 -*-
import AnswerMarkerer
import set_bucket_solution
import set_payForPen_solution
import get_score
import time_plus


file_nums_question1 = [37, 38, 52, 53, 55, 56, 58]
file_nums_question2 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 61, 62, 63, 64, 65, 66]

def get_answers_result(question_file_nums, question_mode):
	temp_list = []

	for file_num in question_file_nums:
		cur_score, math_question = get_score.get_mark_score(str(file_num), question_mode)
		temp_list.append(math_question.get_marked_data())
		# get_score.write_marked_result(math_question, str(file_num))

	return temp_list

def get_average_score(question_file_nums, marked_result_list):
	total = 0.0
	for idx_file_num, marked_result in enumerate(marked_result_list):
		cur_score = marked_result[len(marked_result)-1]
		# print question_file_nums[idx_file_num], cur_score
		total += cur_score
	avg_score = total/len(question_file_nums)
	return avg_score

'''得出每個步驟的平均'''
def get_average_steps_score(question_file_nums, marked_result_list):
	steps_avg_score = []
	step_len = len(marked_result_list[0]) - 1
	for i in range(step_len):
		total = 0.0
		for idx_file_num, marked_result in enumerate(marked_result_list):
			cur_score = marked_result[i][1]
			total += cur_score
		steps_avg_score.append(total/(len(marked_result_list)))
	
	return steps_avg_score

'''得出每個步驟的平均時間'''
def get_average_steps_time(question_file_nums, marked_result_list):
	FMT = '%H:%M:%S.%f0'
	steps_avg_time = []
	step_len = len(marked_result_list[0]) - 1
	for i in range(step_len):
		total = '00:00:00.0000000'
		for idx_file_num, marked_result in enumerate(marked_result_list):
			cur_time = marked_result[i][2]
			total = time_plus.time_str_plus(FMT, total, cur_time)
		steps_avg_time.append(time_plus.time_str_divide(FMT, total, ))
	
	return steps_avg_time



'''製作解答特徵的陣列'''
def make_feature_vector(question_file_nums, marked_result_list):
	get_average_steps_score(question_file_nums, marked_result_list)
############################################################################################

alist = get_answers_result(file_nums_question2, 2)
avg_score = get_average_score(file_nums_question2, alist)
make_feature_vector(file_nums_question2, alist)
# for data in alist:
# 	print data