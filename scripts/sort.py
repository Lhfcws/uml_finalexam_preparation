#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Just a script to sort keyword in the markdown so as to make it more readable.
@author Lhfcws
'''
### IMPORT
import re

### CONFIG
begin_line = 10
path = '../'
filename = 'uml_index.markdown'
output_filename = 'uml_index_in_order.markdown'

fname = path + filename
outputf = path + output_filename

p_keyword = re.compile('\*\*(\W|\w|\(|\)| )+\*\*')
p_page = re.compile('p[0-9]+')

### FUNCTIONS

# Get the keyword of a markdown line
def get_keyword(line):
    match = p_keyword.search(line)
    if match == None:
        return False
    return match.group(0)[2:-2].lower()

# Set the page word (like p123, p22) being italic.
def italic_page(line):
    new_l = p_page.sub(lambda(m): '_'+m.group(0)+'_', line)
    return new_l

# Usually there will be no * in page block.
def has_italic(line):
    return line.count('_') >= 2

# Read md file
def readfile():
    fp = open(fname, 'r')
    lines = fp.readlines()
    fp.close()
    return lines

# Output to a new md file
def writefile(lines):
    fp = open(outputf, 'w')
    fp.writelines(lines)
    fp.close()

### MAIN
def main():
    lines = readfile()
    static_lines = lines[0:begin_line]
    lines = lines[begin_line:]

    dct = {}
    preline = ''

    for i, line in enumerate(lines[::-1]):
        if line.strip() == '':
            continue
        keyword = get_keyword(line)
        if not keyword:
            if not has_italic(line):
                preline = italic_page(line)
        else:
            dct[keyword] = line + '%%' + preline
            continue

    ls = []
    tl = list(dct.iterkeys())
    tl.sort()
    for key in tl:
        for line in dct[key].split('%%'):
            ls.append(line)

    ls[:0] = static_lines
    writefile(ls)
    print '> Generation success!'

if __name__ == '__main__':
    main()
