# -*- coding: utf-8 -*-
import AnswerMarkerer
import set_bucket_solution
import set_payForPen_solution

##############################################################


file_out_id = open("Stroke_NN.txt", "r")
file_id = file_out_id.read() # the 'NN' of file name Stroke_NN_text.txt
stroke_file_name = 'answer_sheet_file/Stroke_' + file_id + '_text.txt' # make the string of the stroke file

# write file
file_out = open('marked result/Stroke_' + file_id + '_score.txt', 'w')
#score1 = set_bucket_solution.bucket_question.get_score(stroke_file_name, file_out)
score1 = set_payForPen_solution.payForPen_question.get_score(stroke_file_name, file_out)
file_out.write('Stroke_' + file_id + '正確率 ' + str(score1))
file_out.close()
