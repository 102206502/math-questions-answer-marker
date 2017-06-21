# -*- coding: utf-8 -*-
import AnswerMarkerer


## setting 買筆題目 solution ##
# solution 1 #
payForPen_question = AnswerMarkerer.QuestionSolutions('pay for pen question')
temp_solution = AnswerMarkerer.MathSolution()
temp_step = AnswerMarkerer.StepOfSolution('設買x枝鉛筆，( 10－x ) 枝原子筆', 'set variables')
temp_step.addKey(r'(設|令).*買\s*(x|X).*鉛筆')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12x+25 ( 10-x )+52=12 ( 10-x )+25x', 'write equesion')
temp_step.addKey((r'(12x(\+)25\\left\( 10-x\\right\) (\+)52=12\\left\( 10-x\\right\) (\+)25x)'
	'|(12x(\+)25\\left\( 10-x\\right\) =12\\left\( 10-x\\right\) (\+)25x-52)'))
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12x＋25 ( 10－x )＋52＝12 ( 10－x )＋25x\n12x＋250－25x＋52＝120－12x＋25x\n－26x＝－182\nx＝7', 'equesion calculation')
temp_step.addKey(r'x\s*=\s*7')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12\\times 7+25\\times \left( \\begin\{matrix\} 10& -7\\end\{matrix\} \\right) =84+75=159', 'calculate answer')
temp_step.addKey(r'=\s*159')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('答：159 元', 'answer')
temp_step.addKey(r'1\s*5\s*9\s*\(?(元|塊)\)?')
temp_solution.add_step(temp_step)

payForPen_question.addSolution(temp_solution)
# end solution 1 #
# solution 2 #
temp_solution = AnswerMarkerer.MathSolution()
temp_step = AnswerMarkerer.StepOfSolution('設買x枝原子筆，( 10－x ) 枝鉛筆', 'set variables')
temp_step.addKey(r'(設|令).*買\s*(x|X).*原子筆')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12(10－x)＋25 x ＋52＝12 x＋25 ( 10－x )', 'write equesion')
temp_step.addKey((r'(12\\left\( 10-x\\right\) \+25x\+52=12x\+25\\left \( 10-x \\right \))'
	'|(12\\left\( 10-x\\right\) \+25x=12x\+25\\left \( 10-x \\right \)-52)'))
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12(10－x)＋25 x ＋52＝12 x＋25 ( 10－x )\n120－10x＋25 x＋52＝12x＋250－25x\n26x＝78\nx＝3', 'equesion calculation')
temp_step.addKey(r'x\s*=\s*3')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12\\times 7+25\\times \left( \\begin\{matrix\} 10& -7\\end\{matrix\} \\right) =84+75=159', 'calculate answer')
temp_step.addKey(r'=\s*159')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('答：159 元', 'answer')
temp_step.addKey(r'1\s*5\s*9\s*\(?(元|塊)\)?')
temp_solution.add_step(temp_step)

payForPen_question.addSolution(temp_solution)
# end solution 2 #

# solution 3 #
temp_solution = AnswerMarkerer.MathSolution()
temp_step = AnswerMarkerer.StepOfSolution('設買x枝鉛筆，y 枝原子筆', 'set variables')
temp_step.addKey(r'(設|令).*買\s*(x|X).*鉛筆')
temp_step.addKey(r'(設|令).*(y|Y).*原子筆')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12x＋25 y ＋52＝12 y＋25 x', 'write equesion')
temp_step.addKey(r'12x\+25y\+52\s*=\s*12y\+25x')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('x+y=10', 'write equesion')
temp_step.addKey(r'x\+y=10')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('x-y=4, x+y=10,x=7,y=3', 'equesion calculation')
temp_step.addKey(r'x\s*=\s*7')
temp_step.addKey(r'y\s*=\s*3')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12\\times 7+25\\times \left( \\begin\{matrix\} 10& -7\\end\{matrix\} \\right) =84+75=159', 'calculate answer')
temp_step.addKey(r'=\s*159')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('答：159 元', 'answer')
temp_step.addKey(r'1\s*5\s*9\s*\(?(元|塊)\)?')
temp_solution.add_step(temp_step)

payForPen_question.addSolution(temp_solution)
# end solution 3 #

# solution 4 #
temp_solution = AnswerMarkerer.MathSolution()
temp_step = AnswerMarkerer.StepOfSolution('設買x枝原子筆，y 枝鉛筆', 'set variables')
temp_step.addKey(r'(設|令).*買\s*(x|X)\s*(枝|支)原子筆')
temp_step.addKey(r'(設|令).*買\s*(y|Y)\s*(枝|支)鉛筆')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12y＋25 x ＋52＝12 x＋25 y', 'write equesion')
temp_step.addKey('25x\+12y\+52\s*=\s*25y\+12x')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('x+y=10', 'write equesion')
temp_step.addKey('x\+y=10')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('x-y=-4, x+y=10, x=3,y=7', 'equesion calculation')
temp_step.addKey('x\s*＝\s*3')
temp_step.addKey('y\s*＝\s*7')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('12\\times 7+25\\times \left( \\begin\{matrix\} 10& -7\\end\{matrix\} \\right) =84+75=159', 'calculate answer')
temp_step.addKey('=\s*159')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('答：159 元', 'answer')
temp_step.addKey('1\s*5\s*9\s*\(?(元|塊)\)?')
temp_solution.add_step(temp_step)

payForPen_question.addSolution(temp_solution)
# end solution 4 #

# solution 5 #
# end solution 5 #

# solution 6 #
# end solution 6 #

## end setting 買筆題目 solution ##