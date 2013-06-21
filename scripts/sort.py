#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Just a script to sort keyword in the markdown so as to make it more readable.
@author Lhfcws
'''
import re

# CONFIG
begin_line = 11
path = '../'
filename = 'uml_index.markdown'
output_filename = 'uml_index_in_order.markdown'

fname = path + filename
outputf = path + output_filename

p_keyword = re.compile('\*\*(\w)+\*\*')
p_page = re.compile('p[0-9]+')

# FUNCTIONS
def get_keyword(line):
    match = p_keyword.search(line)
    if match == None:
        return False
    return match.group(0)[2:-2]

def italic_page(line):
    new_l = p_page.sub('_'++'_', line)
    return new_l

def readfile():
    fp = open(fname, 'r')
    lines = fp.readlines()
    fp.close()
    return lines

def writefile(lines):
    fp = open(outputf, 'w')
    fp.writelines(lines)
    fp.close()

def main():
    lines = readfile()
        
