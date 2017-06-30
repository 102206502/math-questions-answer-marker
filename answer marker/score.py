# -*- coding: utf-8 -*-
import AnswerMarkerer
import set_bucket_solution
import set_payForPen_solution

##############################################################

def read_mark_data():
	file_out_id = open("Stroke_NN.txt", "r")
	file_id = file_out_id.read() # the 'NN' of file name Stroke_NN_text.txt
	answers_file_name = 'recognition output file/Stroke_' + file_id + '_text.txt' # make the string of the answer sheet file
	time_file_name = 'strokes time analysis file/Stroke_' + file_id + '_time.txt' # make the string of the line finished time file
	file_q_mode = open("question_mode.txt")
	question_mode = int(file_q_mode.read())# 1 : bucket, 2: payForPen

	return answers_file_name, time_file_name, file_id, question_mode

def output_mark_result(answers_file_name, time_file_name, file_id, question_mode):
	# write file
	score = 0
	file_out = open('marked result/Stroke_' + file_id + '_score.txt', 'w')
	if question_mode == 1:
		score = set_bucket_solution.bucket_question.get_score(answers_file_name, time_file_name, file_out)
	elif question_mode == 2:
		score = set_payForPen_solution.payForPen_question.get_score(answers_file_name, time_file_name, file_out)

	file_out.write('Stroke_' + file_id + '正確率 ' + str(score))
	file_out.close()
	return score

#######################################################################
answers_file_name, time_file_name, file_id, question_mode = read_mark_data()
output_mark_result(answers_file_name, time_file_name, file_id, question_mode)
