# -*- coding: utf-8 -*-
import re
from datetime import datetime
import time_plus

class QuestionSolutions(object):
	"""一個題目，內含一個以上的解題法"""
	def __init__(self, question_name):
		self.question_name = question_name
		self.time_lines = []
		self.math_solutions = []
		self.score = 0.0
		self.hit_solution = 0


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
		# 將作答時間檔案逐行放進list
		# 完成answer_lines
		# 
		# max_score = 0
		# 
		# for each math solution in math solutions
		# 	計算solution分數
		# 	max_score = 取最高分
		# 	if answer marked as 100%(=1)
		# 		break
		# end for
		# return max_score
	'''
	def get_score(self, answer_sheet_file_name, line_finish_time_file_name):
		self.clean_score()
		answer_lines = self.read_file_in_lines(answer_sheet_file_name)
		time_lines = self.read_file_in_lines(line_finish_time_file_name)
		self.time_lines = time_lines
		max_score = 0.0
		# calculate score
		for solution_count, solution in enumerate(self.math_solutions):
			solution_count += 1
			# output_file.write('solution ' + str(solution_count) + '\n')
			# print 'solution ' + str(solution_count) + '\n'
			solution_score = solution.get_score(answer_lines, time_lines)
			# output_file.write('solution ' + str(solution_count) + ' 正確率 : ' + str(solution_score) + '\n\n')
			# print 'solution ' + str(solution_count) + ' 正確率 : ' + str(solution_score) + '\n\n'
			if solution_score > max_score:
				max_score = solution_score
				self.hit_solution = solution_count
				self.score = max_score

			if max_score >= 1:
				break

		return max_score

	def clean_score(self):
		self.score = 0.0
		self.hit_solution = 0

	def total_cost_time(self):
		FMT = '%H:%M:%S.%f0'
		total_time = '00:00:00.0000000'
		for time in self.time_lines:
			total_time = time_plus.time_str_plus(FMT, total_time, time)
		print total_time
		return total_time

	'''回傳正確解法的內容'''
	def get_marked_data(self):
		temp_list = self.math_solutions[self.hit_solution-1].get_marked_sln_data()
		print temp_list
		# temp_list = self.refine_step_finish_time(self.time_lines, temp_list)
		return temp_list

	# def refine_step_finish_time(self, time_lines, marked_data):
	# 	plus_time = False
	# 	appended_time_line = []
	# 	temp_step_time = '00:00:00.0000000'
	# 	for time_line in time_lines:
	# 		appended_time_line.append(False)
	# 	steps = self.math_solutions[self.hit_solution-1].steps
	# 	for step_num, step in enumerate(steps):
	# 		match = re.finditer(r'(設定變數)|(寫答案)|(列方程式)', step.step_type)
	# 		if not match and step.score <= 0:
	# 			plus_time = True
	# 		elif step.score > 0:
	# 			for i in range(len(step.hit_lines)):
	# 				appended_time_line[step.hit_lines[i]] = True
	# 		else:

	# 	return marked_data


	def write_marked_result(self, file_out):
		marked_result_list = self.get_marked_data()

		for indx in range(len(marked_result_list)-1):
			step_data_list = marked_result_list[indx]
			file_out.write(step_data_list[0] + ', 正確率 ' + str(step_data_list[1]) + ', ' + step_data_list[2] + '\n')# 步驟 正確率 累計時間
		return marked_result_list


	def read_file_in_lines(self, file_name):
		lines = []
		file = open(file_name, 'rt')
		str_buffer = ''
		while True:
			line = file.readline()
			if not line or line == '\n':
				break
			str_buffer+=line
		file.close()
		lines = str_buffer.split('\n')
		if lines[len(lines)-1] == '':
			del  lines[-1]
		# print 'read file\n', lines
		return lines

	def addSolution(self, solution):
		self.math_solutions.append(solution)
		
class MathSolution(object):
	"""某個題目的一種解法"""
	def __init__(self):
		self.step_count = 0
		self.steps = []
		self.score = 0.0
		#
	'''增加一個步驟
		
		paramater
		----------
			step : StepOfSolution
	'''
	def add_step(self, step):
		self.step_count += 1
		step.number = self.step_count
		self.steps.append(step)

	'''回傳 步驟資料 解法正確率'''
	def get_marked_sln_data(self):
		temp_list = []
		for step in self.steps:
			temp_list.append(step.get_marked_step_data())
		temp_list.append(self.score)
		return temp_list

	'''在用本解法計算對某份學生答案的正確率之前，先將步驟分數等歸零'''
	def clean_score(self):
		self.score = 0.0
		for step in self.steps:
			step.score = 0.0
			step.cost_time = '00:00:00.0000000'
			step.hit_lines = []
	'''計算本解法分數

		pseudocode 
		-----------
		先將步驟分數等歸零
		for 行 in 作答檔案
			尋找對於各步驟的正確率
			if 此步驟正確率非零
				break
			end if
		end for
		'''
	def get_score(self, answer_lines, time_lines):
		self.clean_score()
		FMT = '%H:%M:%S.%f0'
		step_scores = 0.0
		temp_step_time = '00:00:00.0000000'
		temp_hit_line = []
		temp_step_type = '計算'
		for line_idx, ans_line in enumerate(answer_lines):
			# print 'line', line_idx, ans_line
			for step_idx, step in enumerate(self.steps):
				step_score = step.get_score(ans_line, time_lines[line_idx], line_idx)
				if step_score > 0:
					step_scores += step_score
					match = re.search(r'(設定變數)|(寫答案)|(列方程式)', step.step_type)
					if not match:
						print 'add all', temp_step_time
						step.cost_time = time_plus.time_str_plus(FMT, step.cost_time, temp_step_time)
						step.hit_lines += temp_hit_line
						temp_step_time = '00:00:00.0000000'
						temp_hit_line = []
					break
				elif step_idx == len(self.steps) - 1:
					temp_step_time = time_plus.time_str_plus(FMT, temp_step_time, time_lines[line_idx])
					temp_hit_line.append(line_idx)
		self.score = step_scores/len(self.steps)
		return self.score

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
		self.score = 0.0
		self.cost_time = '00:00:00.0000000'
		self.hit_lines = [] # 符合步驟正規式的行號

	'''加入關鍵正規式
		Parameter
		----------
		key : string in Regular expression
	'''
	def addKey(self, key):
		self.keys.append(key)

	'''回傳 步驟 正確率 累計時間 符合行號 的list'''
	def get_marked_step_data(self):
		temp_list = []
		temp_list.append(self.step_type)
		temp_list.append(self.score)
		temp_list.append(self.cost_time)
		temp_list.append(self.hit_lines)
		return temp_list


	def add_by_tmp_keys():
		#while(true):
			#加入key，遇到\n表示下個key

		return

	'''計算該步驟成績
		Parameter
		----------
		answer : string
			a line of the answer sheet
		time_line : string
			finish time of a line of the answer sheet finish time
		line_idx : int
			the index of the line of the answer
	'''
	def get_score(self, answer, time_line, line_idx):
		FMT = '%H:%M:%S.%f0'
		match_count = 0.0

		for key in self.keys:
			matches = re.finditer(key, answer)
			# print key, answer
			result = False

			for matchNum, match in enumerate(matches):
				matchNum = matchNum + 1
				if matchNum:
					result = True

			if result:
				match_count += 1

		score = 0.0
		score = match_count/len(self.keys)
		if score > 0:
			self.score += score# 讓每個步驟各自累算得分，之後再在列出個步驟正確率時使用(但是如何累算時間?)
			self.hit_lines.append(line_idx)
			self.cost_time = time_plus.time_str_plus(FMT, self.cost_time, time_line)

		# if score > 0:
		# 	print self.step_type, '\nstep ' + self.content + '\n正確率 ' + str(score)
		# print self.step_type, '\nstep ' + self.content + '\n正確率 ' + str(score)
		return score


###end of class definition###	
