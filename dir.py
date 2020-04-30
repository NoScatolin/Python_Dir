#!/usr/bin/python

import requests

word = open('lista.txt')
linhas = word.readlines()
url = raw_input ('Insira a URL para scan de diretorio: ')

for linha in linhas:
	resposta = requests.get(url+linha)
	codigo = resposta.status_code
	if codigo != 404:
		print url+linha, resposta.status_code