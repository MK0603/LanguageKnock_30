#!/usr/bin/python
# coding: UTF-8

import MeCab

mcb = MeCab.Tagger("")

ifile = open('/home/nanoha/Documents/neko.txt')
ofile = open('/home/nanoha/Documents/neko.txt.mecab','w')

idata = ifile.read()
ifile.close()

ofile.write(mcb.parse(idata))
ofile.close()