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


def arq_size(filename):
	# coleta os dados do arquivo
	statinfo = os.stat(filename)

	return statinfo.st_size


def convert_buffer_to_mat(buff):
	buff = buff.split('\n')
	buff_cache = []
	for i in buff:
		buff_cache.append(i.split(','))

	return buff_cache


def register_size(tabName):
	tabR = open(tabName, "r")
	tabLine = tabR.readline()
	size = len(bytes(tabLine, encoding="UTF-8"))

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


	x = register_size(tabR_name)

	a = tabR.read(x)

	print (a)



if __name__ == '__main__':
	main()
