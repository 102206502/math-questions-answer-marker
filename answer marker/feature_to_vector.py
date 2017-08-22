# -*- coding: utf-8 -*-
import AnswerMarkerer
import set_bucket_solution
import set_payForPen_solution
import get_score
import time_plus
import numpy as np


student_state_dic = {'well' : 0, '不會列方程式' : 1, '計算錯誤' : 2, '計算太慢' : 3, '公式不熟' : 4, '完全不會' : 5}
file_nums_question1 = [37, 38, 52, 53, 55, 56, 58]
file_nums_question2 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80]
file_nums_question_list = [file_nums_question1, file_nums_question2]
student_state_list  = [ 0,  0,  0,  1,  2,  2,  3,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  4,  4,  4,  4,  4,  4,  2,  2,  2,  2,  2,  2]
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
		get_score.write_marked_result(math_question, str(file_num))

	return marked_results_list

'''得取所有檔案的平均正確率'''
def get_average_score(question_file_nums, marked_results_list):
	total = 0.0
	for idx_file_num, marked_result in enumerate(marked_results_list):
		cur_score = marked_result[len(marked_result)-2]
		# print question_file_nums[idx_file_num], cur_score
		total += cur_score
	avg_score = total/len(question_file_nums)
	print('avg_score', avg_score)
	return avg_score

'''得出所有樣本平均花費時間'''
def get_average_cost_time(question_file_nums, marked_results_list):
	total = '00:00:00.0000000'
	for idx_file_num, marked_result in enumerate(marked_results_list):
		cur_time = marked_result[len(marked_result)-1]
		# print question_file_nums[idx_file_num], cur_time
		total = time_plus.time_str_plus(FMT, total, cur_time)
	avg_time = time_plus.time_str_divide(FMT, total, len(question_file_nums))
	print('avg_time', avg_time)
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
	print('steps_avg_score', steps_avg_score)
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
		temp_step_avg_time_str = time_plus.time_str_divide(FMT, total, non_zero_sample)
		steps_avg_time.append(time_plus.time_str_to_float(FMT, temp_step_avg_time_str))
	print('steps_avg_time', steps_avg_time)
	return steps_avg_time

'''製作解答特徵的陣列'''
def make_feature_vector_all(question_file_nums, marked_results_list):
	# 取出多份檔案的平均值
	all_feature_vector_list = []
	avg_score = get_average_score(question_file_nums, marked_results_list)
	avg_time = get_average_cost_time(question_file_nums, marked_results_list)
	steps_avg_score = get_average_steps_score(question_file_nums, marked_results_list)
	steps_avg_time = get_average_steps_time(question_file_nums, marked_results_list)

	# 取出單份答案的資料
	for idx_file_num, marked_result in enumerate(marked_results_list):
		step_status_list = make_step_feature_vector(idx_file_num, marked_result)
		feature_vector = step_status_list
		# print(feature_vector)
		feature_vector += steps_avg_score
		# print(feature_vector)
		feature_vector += steps_avg_time
		# print(feature_vector)
		feature_vector.append(marked_result[len(marked_result)-2])
		feature_vector.append(avg_score)
		# print(feature_vector)
		feature_vector.append(time_plus.time_str_to_float(FMT, marked_result[len(marked_result)-1]))
		feature_vector.append(time_plus.time_str_to_float(FMT, avg_time))
		# print(feature_vector)
		all_feature_vector_list.append(feature_vector)

	all_feature_vector = np.array(all_feature_vector_list)
	# print(all_feature_vector)
	# print(all_feature_vector.shape)
	# print(type(all_feature_vector))
	return all_feature_vector

# def make_normal_feature_vectors():
# 	pass

def make_step_feature_vector(idx_file_num, marked_result):# 未完成
	step_status_list = []# 分數 對錯 時間
	step_score_list = []
	step_times = []
	step_len = len(marked_result)-2
	for i in range(step_len):
		step_score_list.append(marked_result[i][1])
		step_times.append(time_plus.time_str_to_float(FMT, marked_result[i][2]))

	step_status_list = step_score_list + step_times

	return step_status_list

'''
	Paramater
	---------
	question_mode : int

	Return
	------
	X_data
	Y_data
'''
def get_all_data(question_mode):
	marked_results_list = get_answers_result(file_nums_question_list[question_mode-1], question_mode)
	X_data = make_feature_vector_all(file_nums_question2, marked_results_list)
	Y_data = np.array(student_state_list)
	return X_data, Y_data

############################################################################################

marked_results_list = get_answers_result(file_nums_question2, 2)
X_data = make_feature_vector_all(file_nums_question2, marked_results_list)
Y_data = np.array(student_state_list)