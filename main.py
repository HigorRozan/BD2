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
from tabulate.tabulate import tabulate
import time 



def arq_size(filename):
    # coleta os dados do arquivo
    statinfo = os.stat(filename)

    return statinfo.st_size


def convert_buffer_to_mat(buff):
    buff = buff.splitlines()
    cache = []
    for x in buff:
        cache.append(x.split(","))

    return cache


def register_size(tabName):
    tabR = open(tabName, "r")
    tabLine = tabR.readline()
    size = len(bytes(tabLine, encoding="UTF-8"))
    tabR.close()

    return size


def head_size(tabName):
    tabR = open(tabName + '_meta', "r")
    tabLine = tabR.readline()
    size = len(bytes(tabLine, encoding="UTF-8"))
    tabLine = tabR.readline()
    size = size + len(bytes(tabLine, encoding="UTF-8"))
    tabLine = tabR.readline()
    size = size + len(bytes(tabLine, encoding="UTF-8"))
    tabR.close()

    return size


def head_register(tabName):

    tab = open(tabName + '_meta', "r")
    tabLine = tab.readline()
    head = tabLine

    tabLine = tab.readline()
    _keys = tabLine.split(',')

    # Verifica se existem chaves
    # retorna a posição da chave para comparar na tabela
    #[fields]
    #[0]
    key_c = []

    for line in _keys:
        key_c.append(line.split(':')[1].splitlines())

    tabLine = tab.readline()
    size = len(bytes(tabLine, encoding="UTF-8")) + 1

    head_bytes = head_size(tabName)

    info = [size, key_c, head, head_bytes]
    tab.close()

    return info


def join_reg(regx, regy):
	reg = []

	reg.append(regx[0])
	reg.append(regx[1])
	reg.append(regx[2])
	reg.append(regy[1])

	return reg


def main():

    # Atribuindo valores aos Parâmetros
    tabR_name = input("Nome do arquivo da tabela R externa: ")
    tabS_name = input("Nome do arquivo da tabela S interna: ")
    buff_size = int(input("Tamanho do Buffer em Bytes: "))
    page_size = int(input("Tamanho da Página em Bytes: "))

    # Abre os arquivos das Tabelas e verifica se foram encontrados
    # A função open recebe como parâmetro o tamanho em Bytes
    # de blocos que devem ser lido

    try:
        tabR = open(tabR_name, "r", page_size)
        tabS = open(tabS_name, "r", page_size)
    except IOError:
        print ("Erro - Arquivo não encontrado")
        exit()

    # Informações do cabeçalho
    # Calcula o tamanho inteiro de registros que
    # cabem em um tamanho de buffer
    infoR = head_register(tabR_name)
    infoS = head_register(tabS_name)

    regR_size = infoR[0]
    regS_size = infoS[0]

    buff_ext_size = round(buff_size / regR_size) * regR_size
    buff_int_size = round(buff_size / regS_size) * regS_size

    # Calcula o número de leitura necessária
    num_read_ext = 1 + m.floor(arq_size(tabR_name) / buff_ext_size)
    num_read_int = 1 + m.floor(arq_size(tabS_name) / buff_int_size)
    
    #Calculos dos fatores
    fatores_f = []
 
    fatores_f.append(buff_size/page_size)
    fatores_f.append(round(page_size/register_size(tabR_name),2))
    fatores_f.append(round(page_size/register_size(tabS_name),2))

    out_tab = []
    # Laço externo
    st_time = time.time()
    for i in range(num_read_ext):

        # Lê o buffer
        buff_ext = tabR.read(buff_ext_size)

        # Tranforma em Matriz
        mat_ext = convert_buffer_to_mat(buff_ext)

        # Laço interno
        for t in range(num_read_int):

            # Lê o buffer
            buff_int = tabS.read(buff_int_size)

            # Tranforma em Matriz
            mat_int = convert_buffer_to_mat(buff_int)

            # Executa a comparação
            for x in mat_ext:

                for y in mat_int:

                    if (x[3] == y[0]):
                        out_tab.append(join_reg(x, y))

        # Volta ai inicio da Tabela interna

        tabS.seek(0, 0)
    end_time = time.time()

    time_total = end_time - st_time
    fatores_f.append(round(time_total,4))
    # Resultados

    print (tabulate(out_tab,['cod','first_name','last_name','dep']))
    head = ['Paginas no Buffer','Fator de Blocagem R','Fator de Blocagem S','Tempo de Execução']
    print("----------------------------------------------------------------")
    print(head)
    print (fatores_f)
   

if __name__ == '__main__':
    main()
