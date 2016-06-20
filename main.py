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


def main():

    # Atribuindo valores aos Parâmetros
    # tabR_name = input("Nome do arquivo da tabela R externa: ")
    # tabS_name = input("Nome do arquivo da tabela S interna: ")
    # buff_size = int(input("Tamanho do Buffer em Bytes: "))
    # page_size = int(input("Tamanho da Página em Bytes: "))

    tabR_name = 'user'
    tabS_name = 'dep'
    buff_size = 20
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

    # Lê nos arquivo as informação da tabela
    tabR_info = tabR.readline().split(',')
    tabS_info = tabS.readline().split(',')

    done = True

    # Executa um laço até o fim do algoritmo
    while(done):

        # Lê o buffer externo
        buffer_ext = tabR.read(buff_size)

        print (buffer_ext)

        cache = []
        i = -1
        while(buffer_ext[i] != '\n'):
            cache.append(buffer_ext[i])
            i -= 1

        done = False


if __name__ == '__main__':
    main()
