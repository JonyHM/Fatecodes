#!usr/bin/env python
#-*- coding: utf-8 -*-

def rep(code):

	from unicodedata import normalize

	code = normalize('NFkD', code).encode('ASCII', 'ignore').decode('ASCII')

	return code

name = input('codigo: ')
f = open(name, 'r').read()
txt = open(name, 'w')

for palavra in f:
	rep(palavra)
