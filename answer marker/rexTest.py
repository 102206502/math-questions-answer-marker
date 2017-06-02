#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

#regex = r"設買\s*x\s*本?(支|枝)鉛筆"
regex = r"設買\s*x\s*(本)?(支|枝)"
test_str = "設買 x 枝"
#test_str = test_str.decode('utf-8')
print type(test_str)
matches = re.finditer(regex, test_str)


result = 0

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    result = matchNum
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


if not result:
	print 'No match!!!!!!!!!!!!!'

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.