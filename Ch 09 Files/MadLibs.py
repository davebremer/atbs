# Create a Mad Libs program that reads in text files and lets the user
# add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB 
# appears in the text file.

from pathlib import Path
import pyinputplus as pyip
import re

fileName = pyip.inputStr(prompt='Filename: ', default='madlib.txt')
theFile = open(Path.home() / fileName, 'r')
fileContent = theFile.read()

adjective = pyip.inputStr(prompt='Adjective: ')
noun = pyip.inputStr(prompt='Noun: ')
verb = pyip.inputStr(prompt='Verb: ')

# print(f'\n\nAdjective: {adjective}\nNoun: {noun}\nVerb: {verb}\n\n')

fileContent = fileContent.replace('ADJECTIVE',adjective)
fileContent = fileContent.replace('NOUN',noun)
fileContent = fileContent.replace('VERB',verb)

outFile = open(Path.home() / 'madlibout.txt', 'w')
outFile.write(fileContent)
# print(fileContent)
theFile.close()
outFile.close()