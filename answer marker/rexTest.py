#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

#regex = r"設買\s*x\s*本?(支|枝)鉛筆"
regex = r"設買.*鉛筆"
print 'line 1'
test_str = ("設買 x 枝原子筆, y 枝鉛筆\n"
	"12,25x+12y+52=25y+12x \n"
	"x +y=10\n"
	"x -y=-4\n"
	"x =3,y=7\n"
	"12\\times 7+25\\times 3=84+75=159\n"
	"A: 159 元")
print 'line 2'
#test_str = test_str.decode('utf-8')
print type(test_str)
matches = re.finditer(regex, test_str)


result = 0

print 'line 3'
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    result = matchNum
    
    # start_inx = match.start()
    # end_inx = match.end()

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    # print ('start char'+test_str[start_inx])
    # print ('end char'+test_str[end_inx])
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = start_inx, end = end_inx, group = match.group(groupNum)))


if not result:
	print 'No match!!!!!!!!!!!!!'

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.