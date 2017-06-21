# -*- coding: utf-8 -*-
import re

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
	def get_score(self, answer_sheet_file_name, output_file):
		answer_lines = self.read_answer_sheet(answer_sheet_file_name)
		max_score = 0.0
		# calculate score
		solution_count = 1
		for solution in self.math_solutions:
			output_file.write('solution ' + str(solution_count) + '\n')
			print 'solution ' + str(solution_count) + '\n'
			solution_score = solution.get_score(answer_lines, output_file)
			output_file.write('solution ' + str(solution_count) + ' 正確率 : ' + str(solution_score) + '\n\n')
			print 'solution ' + str(solution_count) + ' 正確率 : ' + str(solution_score) + '\n\n'
			if solution_score > max_score:
				max_score = solution_score

			if max_score >= 1:
				break

			solution_count += 1

		return max_score

	def read_answer_sheet(self, answer_sheet_file_name):
		answer_lines = []
		file_answer = open(answer_sheet_file_name, 'rt')
		while True:
			line = file_answer.readline()
			if not line:
				break

			answer_lines.append(line)

		file_answer.close()
		print 'read file\n', answer_lines

		return answer_lines

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

	def get_score(self, answer, output_file):
		step_score = 0.0
		for step in self.steps:
			step_score += step.get_score(answer, output_file)

		score = step_score/len(self.steps)
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
	def get_score(self, answer, output_file):
		match_count = 0.0

		for key in self.keys:
			print 'key:', key
			for line_count, ans_line in enumerate(answer):
				matches = re.finditer(key, ans_line)

				result = False

				for matchNum, match in enumerate(matches):
					matchNum = matchNum + 1
					if matchNum:
						result = True

				if result:
					match_count += 1
					#self.step_type
					break

		score = 0.0
		score = match_count/len(self.keys)
		output_file.write('keys len:' + str(len(self.keys)) + '\n')
		print 'keys len:', len(self.keys)
		output_file.write('step ' + self.content + '\nmatch count : ' + str(match_count) + '\n正確率 ' + str(score) + '\n')
		print 'step ' + self.content + '\nmatch count : ' + str(match_count) + '\n正確率 ' + str(score)
		return score


###end of class definition###	
