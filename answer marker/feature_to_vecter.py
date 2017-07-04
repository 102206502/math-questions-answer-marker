# -*- coding: utf-8 -*-
import AnswerMarkerer
import set_bucket_solution
import set_payForPen_solution
import score

file_nums_question1 = [37, 38, 52, 53, 55, 56, 58]
file_nums_question2 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 61, 62, 63, 64, 65, 66]

def get_average_score(question_file_nums, question_mode):
	total = 0.0
	for file_num in question_file_nums:
		cur_score = score.get_mark_score(str(file_num), question_mode)
		print file_num, cur_score
		total += cur_score

	avg_score = total/len(question_file_nums)
	return avg_score

def get_answer_data():
	pass
avg_score = get_average_score(file_nums_question2, 2)
print avg_score