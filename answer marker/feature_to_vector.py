# -*- coding: utf-8 -*-
import AnswerMarkerer
import set_bucket_solution
import set_payForPen_solution
import get_score
import time_plus
import numpy as np


file_nums_question1 = [37, 38, 52, 53, 55, 56, 58]
file_nums_question2 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 61, 62, 63, 64, 65, 66]
FMT = '%H:%M:%S.%f0'
'''取得同類題目的全部資料'''
def get_answers_result(question_file_nums, question_mode):
	marked_results_list = []
	cost_time = ''

	for file_num in question_file_nums:
		cur_score, math_question = get_score.get_mark_score(str(file_num), question_mode)
		marked_result = math_question.get_marked_data()
		marked_result.append(math_question.total_cost_time())
		marked_results_list.append(marked_result)
		# get_score.write_marked_result(math_question, str(file_num))

	return marked_results_list

'''得取所有檔案的平均正確率'''
def get_average_score(question_file_nums, marked_results_list):
	total = 0.0
	for idx_file_num, marked_result in enumerate(marked_results_list):
		cur_score = marked_result[len(marked_result)-2]
		# print question_file_nums[idx_file_num], cur_score
		total += cur_score
	avg_score = total/len(question_file_nums)
	return avg_score

'''得出所有樣本平均花費時間'''
def get_average_cost_time(question_file_nums, marked_results_list):
	total = '00:00:00.0000000'
	for idx_file_num, marked_result in enumerate(marked_results_list):
		cur_time = marked_result[len(marked_result)-1]
		# print question_file_nums[idx_file_num], cur_score
		total = time_plus.time_str_plus(FMT, total, cur_time)
	avg_time = time_plus.time_str_divide(FMT, total, len(question_file_nums))
	print 'avg_time', avg_time
	return avg_time

'''得出每個步驟的平均'''
def get_average_steps_score(question_file_nums, marked_results_list):
	steps_avg_score = []
	step_len = len(marked_results_list[0]) - 2
	for i in range(step_len):
		total = 0.0
		for idx_file_num, marked_result in enumerate(marked_results_list):
			cur_score = marked_result[i][1]
			total += cur_score
		steps_avg_score.append(total/(len(marked_results_list)))
	print steps_avg_score
	
	return steps_avg_score

'''得出每個步驟的平均時間，去掉時間是0的樣本'''
def get_average_steps_time(question_file_nums, marked_results_list):
	steps_avg_time = []
	non_zero_sample = 0
	step_len = len(marked_results_list[0]) - 2
	for i in range(step_len):
		total = '00:00:00.0000000'
		non_zero_sample = 0
		for idx_file_num, marked_result in enumerate(marked_results_list):
			if marked_result[i][2] != '00:00:00.0000000':
				cur_time = marked_result[i][2]
				total = time_plus.time_str_plus(FMT, total, cur_time)
				# print cur_time, total
				non_zero_sample += 1
		steps_avg_time.append(time_plus.time_str_divide(FMT, total, non_zero_sample))
		# print non_zero_sample
	print steps_avg_time
	return steps_avg_time

'''製作解答特徵的陣列'''
def make_feature_vector(question_file_nums, marked_results_list):
	# 取出多份檔案的平均值
	avg_time = get_average_cost_time(question_file_nums, marked_results_list)
	steps_avg_score = get_average_steps_score(question_file_nums, marked_results_list)
	steps_avg_time = get_average_steps_time(question_file_nums, marked_results_list)

	# 取出單份答案的資料
	for idx_file_num, marked_result in enumerate(marked_results_list):
		step_status_list = []# 對錯 分數 時間
		step_is_correct_list = []
		step_times = []
		step_len = len(marked_result)-2
		for i in range(step_len):
			if marked_result[i][1] == 0 :
				step_is_correct_list.append(-1)
			else:
				step_is_correct_list.append(0)
			step_times.append(XXXXXX)



############################################################################################

alist = get_answers_result(file_nums_question2, 2)
avg_score = get_average_score(file_nums_question2, alist)
make_feature_vector(file_nums_question2, alist)
# for data in alist:
# 	print data