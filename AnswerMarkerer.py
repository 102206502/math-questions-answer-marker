# -*- coding: utf-8 -*-
import re

class QuestionSolutions(object):
	"""一個題目，內含一個以上的解題法"""
	def __init__(self, question_name):
		self.question_name = question_name
		self.math_solutions = []

	'''
	'''
	def get_score(self, answer_sheet_file_name):
		'''
		依據本題儲存之解法，計算本題分數

		pseudocode :
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
		answer_lines = self.read_answer_sheet(answer_sheet_file_name)
		max_score = 0.0
		# calculate score
		for solution in self.math_solutions:
			solution_score = solution.get_score(answer_lines)
			if solution_score > max_score:
				max_score = solution_score

			if max_score >= 1:
				break

		return max_score

	def read_answer_sheet(self, answer_sheet_file_name):
		answer_lines = ''
		file_answer = open(answer_sheet_file_name, 'rt')
		while True:
			line = file_answer.readline()
			if not line:
				break

			answer_lines += line

		file_answer.close()
		print 'read file\n' + answer_lines

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

	def get_score(self, answer):
		step_score = 0.0
		for step in self.steps:
			step_score += step.get_score(answer)

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
	def __init__(self, content='', step_type='calculation', keys=[], number=0):
		self.content = content
		#self.keys = add_by_tmp_keys(tmp_keys)
		self.keys = keys
		self.number = number # 0相當於未設定順序編號
		self.step_type = step_type

	'''加入關鍵正規式
	key : string in Regular expression'''
	def addKey(self, key):
		self.keys.append(key)

	def add_by_tmp_keys():
		#while(true):
			#加入key，遇到\n表示下個key

		return


	def get_score(self, answer):
		match_count = 0

		for key in self.keys:
			result = re.search(key, answer)
			if result:
				match_count += 1

		score = 0.0
		score = match_count/len(self.keys)
		print 'step ' + self.content + ' 正確率 ' + str(score)
		return score


###end of class definition###	
###############################################################################
###start here###

# set 鐵桶題目 solution
bucket_question = QuestionSolutions('buket question')

temp_solution = MathSolution()
temp_step = StepOfSolution('設水桶與鐵柱底面積、半徑2m, m', 'set variables')
temp_step.addKey('(設|令).*桶.*底面積.*半徑')
temp_step.addKey("(設|令).*柱.*底面積.*半徑")
temp_step.addKey('2[a-zA-Z].*[a-zA-Z]')
temp_solution.add_step(temp_step)

temp_step = StepOfSolution('\\dfrac {\\left( 2m\\right) ^\{2\}\pi \\times 12-m^\{2\}\pi \\times 12} {\\left( 2m\\right) ^\{2\}\\pi }=\\dfrac {36m^\{2\}\\pi } {4m^\{2\}\\pi }=9', 'equesion calculate')
temp_step.addKey('=(?x)9')
temp_solution.add_step(temp_step)

temp_step = StepOfSolution('水面高度變為 9公分', 'answer')
temp_step.addKey('(9|九)(?x)公分')
temp_solution.add_step(temp_step)

bucket_question.addSolution(temp_solution)

score1 = bucket_question.get_score('Stroke_38_text.txt')

print 'Stroke_38_text 正確率 ' + str(score1)