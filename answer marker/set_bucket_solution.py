# -*- coding: utf-8 -*-
import AnswerMarkerer

## set 水桶題目 solution ##
bucket_question = AnswerMarkerer.QuestionSolutions('buket question')

temp_solution = AnswerMarkerer.MathSolution()
temp_step = AnswerMarkerer.StepOfSolution('設水桶與鐵柱底面積、半徑2m, m', '設定變數')
temp_step.addKey('(設|令).*桶.*底面積.*半徑')
temp_step.addKey("(設|令).*柱.*底面積.*半徑")
temp_step.addKey(r'2[a-zA-Z].*[a-zA-Z]')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('\dfrac {\left( 2m\right) ^{2}\pi \times 12-m^{2}\pi \times 12} {\left( 2m\right) ^{2}\pi }=\dfrac {36m^{2}\pi } {4m^{2}\pi }', '列公式')
temp_step.addKey(r'(\^\\\{2\\\}\\( \\times)?\\pi)|(\\pi[^=+\-*]*\^\\\{2\\\})')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution(r'=9\b', '計算答案')
temp_step.addKey(r'(\^\\\{2\\\}\\( \\times)?\\pi)|(\\pi[^=+\-*]*\^\\\{2\\\})')
temp_step.addKey(r'=\s*9')
temp_solution.add_step(temp_step)

temp_step = AnswerMarkerer.StepOfSolution('水面高度變為 9公分', '寫答案')
temp_step.addKey('(9|九)\s*公分')
temp_solution.add_step(temp_step)

bucket_question.addSolution(temp_solution)

## end setting 水桶題目 solution ##