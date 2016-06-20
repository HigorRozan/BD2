# encoding=UTF-8
"""
	Autores:Higor Rozan
			João Bertoncini
			Luan Andryl Silve

	E-mail: higorb.rozan@gmail.com
			jvbertoncini@gmail.com
			luan.andryl@gmail.com

	Este código recebe duas tabela R e S
	e faz a junção deles usando o algoritmo
	Nested Loop Blocado Bufferizado
"""
import os
import math as m


def arq_size(filename):
	# coleta os dados do arquivo
	statinfo = os.stat(filename)

	return statinfo.st_size


def convert_buffer_to_mat(buff):
	buff = buff.split('\n')

	return buff


def register_size(tabName):
	tabR = open(tabName, "r")
	tabLine = tabR.readline()
	size = len(bytes(tabLine, encoding="UTF-8"))
	tabR.close()

	return size


def main():

	# Atribuindo valores aos Parâmetros
	# tabR_name = input("Nome do arquivo da tabela R externa: ")
	# tabS_name = input("Nome do arquivo da tabela S interna: ")
	# buff_size = int(input("Tamanho do Buffer em Bytes: "))
	# page_size = int(input("Tamanho da Página em Bytes: "))

	tabR_name = 'usernew'
	tabS_name = 'dep'
	buff_size = 45
	page_size = 10

	# Abre os arquivos das Tabelas e verifica se foram encontrados
	# A função open recebe como parâmetro o tamanho em Bytes
	# de blocos que devem ser lido
	try:
		tabR = open(tabR_name, "r", page_size)
		tabS = open(tabS_name, "r", page_size)
	except IOError:
		print ("Erro - Arquivo não encontrado")
		exit()

	# Calcula o tamanho inteiro de registros que
	# cabem em um tamanho de buffer
	regR_size = register_size(tabR_name)
	regS_size = register_size(tabS_name)

	buff_ext_size = round(buff_size/regR_size) * regR_size
	buff_int_size = round(buff_size/regS_size) * regS_size 
	
	# Calcula o número de leitura necessária
	num_read_ext = m.floor(arq_size(tabR_name)/buff_ext_size)
	num_read_int = m.floor(arq_size(tabS_name)/buff_int_size) 


	# Lê o buffer
	print (regR_size)
	print (buff_ext_size)
	buff_ext = tabR.read(buff_ext_size)

	# Tranforma em vetor
	mat_ext = buff_ext.splitlines()

	print (buff_ext)


if __name__ == '__main__':
	main()
