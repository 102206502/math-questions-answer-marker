# -*- coding: utf-8 -*-
import re
from datetime import datetime

class QuestionSolutions(object):
	"""一個題目，內含一個以上的解題法"""
	def __init__(self, question_name):
		self.question_name = question_name
		self.math_solutions = []

	'''依據本題儲存之解法，計算本題分數

		Parameter
		----------
		answer_sheet_file_name : string
			被評分的文字檔名

		line_finish_time_file_name : string
			每行完成時間的文字檔名

		pseudocode 
		-----------
		# 將作答檔案逐行放進list
		# 完成answer_lines
		# 
		# max_score = 0
		# 
		# for each math solution in math solutions
		# 	max_score = 取最高分
		# 	if answer marked as 100%(=1)
		# 		break
		# end for
		# return max_score
	'''
	def get_score(self, answer_sheet_file_name, line_finish_time_file_name, output_file):
		answer_lines = self.read_file_in_lines(answer_sheet_file_name)
		time_lines = self.read_file_in_lines(line_finish_time_file_name)
		max_score = 0.0
		# calculate score
		for solution_count, solution in enumerate(self.math_solutions):
			solution_count += 1
			output_file.write('solution ' + str(solution_count) + '\n')
			print 'solution ' + str(solution_count) + '\n'
			solution_score = solution.get_score(answer_lines, time_lines, output_file)
			output_file.write('solution ' + str(solution_count) + ' 正確率 : ' + str(solution_score) + '\n\n')
			print 'solution ' + str(solution_count) + ' 正確率 : ' + str(solution_score) + '\n\n'
			if solution_score > max_score:
				max_score = solution_score

			if max_score >= 1:
				break


		return max_score

	def read_file_in_lines(self, file_name):
		lines = []
		file = open(file_name, 'rt')
		while True:
			line = file.readline()
			if not line or line == '\n':
				break

			lines.append(line)

		file.close()
		print 'read file\n', lines

		return lines

	def addSolution(self, solution):
		self.math_solutions.append(solution)
		
class MathSolution(object):
	"""某個題目的一種解法"""
	def __init__(self):
		self.step_count = 0
		self.steps = []
		#

	def add_step(self, step):
		self.step_count += 1
		step.number = self.step_count
		self.steps.append(step)

	def get_score(self, answer_lines, time_lines, output_file):
		FMT = '%H:%M:%S.%f0\n'
		step_scores = 0.0
		temp_step_type = 'No match'
		temp_step_time = datetime.strptime('00:00:00.0000000\n', FMT)
		# print('time init '+temp_step_time.strftime(FMT))

		for line_idx, ans_line in enumerate(answer_lines):
			for step in self.steps:
				step_score = step.get_score(ans_line, time_lines, output_file)
				step_scores += step_score
				if step_score > 0:
					print('last step time '+temp_step_time.strftime(FMT))
					# output_file.write('total '+temp_step_time.strftime(FMT))
					temp_step_time = datetime.strptime(time_lines[line_idx], FMT)
					# print('new step time:'+temp_step_time.strftime(FMT))
					temp_step_type = step.step_type
				else:
					# 和上個時間相加
					temp_delta = datetime.strptime(time_lines[line_idx], FMT) - datetime.strptime('00:00:00.0000000\n', FMT)
					print temp_delta
					temp_step_time += temp_delta
				if step_score >= 1:
					break
			output_file.write(temp_step_type + ', line ' + str(line_idx) + ', ' + time_lines[line_idx])
			# print(temp_step_type + ', line ' + str(line_idx) + ', ' + time_lines[line_idx] + '\n')

		score = step_scores/len(self.steps)
		return score

class StepOfSolution(object):
	"""一種解法中的一個步驟

		Parameter
		----------
		contect : string
		解題步驟內容
		keys : list of string
		評分關鍵
		number : int
		步驟在解法中的順序 start from 1, default 0
		step_type : string
		步驟類型
	"""
	def __init__(self, content='', step_type='calculation'):
		self.content = content
		#self.keys = add_by_tmp_keys(tmp_keys)
		self.keys = []
		self.number = 0 # 0相當於未設定順序編號
		self.step_type = ''
		self.step_type = step_type

	'''加入關鍵正規式
		Parameter
		----------
		key : string in Regular expression
	'''
	def addKey(self, key):
		self.keys.append(key)

	def add_by_tmp_keys():
		#while(true):
			#加入key，遇到\n表示下個key

		return

	'''計算該步驟成績
		Parameter
		----------
		answer : 1D string list
			lines of the answer sheet
		output_file : file obj
			marked result file
	'''
	def get_score(self, answer, time_lines, output_file):
		match_count = 0.0

		for key in self.keys:
			matches = re.finditer(key, answer)

			result = False

			for matchNum, match in enumerate(matches):
				matchNum = matchNum + 1
				if matchNum:
					result = True

			if result:
				match_count += 1

		score = 0.0
		score = match_count/len(self.keys)
		# if score > 0:
		# 	print self.step_type, '\nstep ' + self.content + '\n正確率 ' + str(score)

		# print 'step ' + self.content + '\nmatch count : ' + str(match_count) + '\n正確率 ' + str(score)
		return score


###end of class definition###	
