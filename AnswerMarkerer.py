import re

class QuestionSolutions(object):
	"""一個題目，內含一個以上的解題法"""
	def __init__(self, question_name):
		self.question_name = question_name
		self.math_solutions = []

	'''
	'''
	def get_score(answer_sheet_file_name):
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
		answer_lines = read_answer_sheet(answer_sheet_file_name)
		max_score = 0
		# calculate score
		for solution in self.math_solutions:
			solution_score = solution.get_score(answer_lines)
			if solution_score > max_score:
				max_score = solution_score

			if max_score >= 1:
				break

		return max_score

	def read_answer_sheet(answer_sheet_file_name):
		answer_lines = []
		file_answer = open(answer_sheet_file_name, 'rt')
		while true:
			line = file_answer.readline()
			if not line:
				break

			answer_lines += line
			answer_lines += '\n'

		file_answer.close()
		return answer_lines

	def addSolution(solution):
		self.math_solutions.append(solution)
		
class MathSolution(object):
	"""某個題目的一種解法"""
	def __init__(self):
		self.step_count = 0
		#

	def add_step(step):
		self.step_count += 1
		step.number = self.step_count
		self.steps.append(step)

	def get_score(answer):
		step_score = 0
		for step in self.steps:
			step_score += step.get_score(answer)

		score = step_score/len(steps)

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
	def __init__(self, content='', step_type='calculation', tmp_keys='', number=0):
		self.content = content
		self.keys = add_by_tmp_keys(tmp_keys)
		self.number = number # 0相當於未設定順序編號
		self.step_type = step_type

	'''加入關鍵正規式
	key : string in Regular expression'''
	def addKey(key):
		self.keys.append(key)

	def add_by_tmp_keys():
		while(true):
			#加入key，遇到\n表示下個key

	'''計算本步驟正確率'''
	def get_score(answer):
		match_count = 0

		for key in self.keys:
			result = re.search(key, answer)
			if result:
				match_count = match_count + 1


		score = match_count/len(self.keys)
		print 'step ' + self.content + ' get ' + score + ' points'
		return score

###end of class definition###	
###############################################################################
###start here###

# set 鐵桶題目 solution
bucket_question = QuestionSolutions('buket question')

temp_solution = MathSolution()
temp_step = StepOfSolution('設鐵桶與鐵柱底面積、半徑2m, m', 'set variables')
temp_step.addKey('設.*鐵桶.*底面積.*半徑')
temp_step.addKey('設.*鐵柱.*底面積.*半徑')
temp_step.addKey('2\w.*\w')
temp_solution.add_step(temp_step)

temp_step = StepOfSolution('\dfrac {\left( 2m\right) ^{2}\pi \times 12-m^{2}\pi \times 12} {\left( 2m\right) ^{2}\pi }=\dfrac {36m^{2}\pi } {4m^{2}\pi }=9', 'equesion calculate')
temp_step.addKey('\dfrac {\left( 2m\right) ^{2}\pi \times 12-m^{2}\pi \times 12} {\left( 2m\right) ^{2}\pi }=\dfrac {36m^{2}\pi } {4m^{2}\pi }=9')
temp_solution.add_step(temp_step)

temp_step = StepOfSolution('水面高度變為 9公分', 'answer')
temp_step.addKey('9\s*公分')
temp_solution.add_step(temp_step)



