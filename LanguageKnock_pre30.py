#!/usr/bin/python
# coding: UTF-8

import MeCab,os

dirPath=os.path.dirname(os.path.abspath(__file__))

mcb = MeCab.Tagger("")

ifile = open(dirPath+'/neko.txt')
ofile = open(dirPath+'/neko.txt.mecab','w')

idata = ifile.read()
ifile.close()

ofile.write(mcb.parse(idata))
ofile.close()