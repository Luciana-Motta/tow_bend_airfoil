import matplotlib.pyplot as plt
import csv
import math

def grafico_comparativo(file_name):
    # Ler os dados reais presentes no arquivo 
    file = 'data/' + file_name
    with open(file, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Extrair os valores do eixo x e y
    dados_x = []
    dados_y = []
    for linha in linhas[4:]:
        valores = linha.split()
        dados_x.append(float(valores[0]))
        dados_y.append(float(valores[1]))

    i, j = -1, -1
    if file_name.find('cd') != -1:
        eixo_x = 'cl'
        eixo_y = 'cd'
        i, j = 2, 1
    elif file_name.find('cl') != -1:
        eixo_x = 'alpha'
        eixo_y = 'cl'     
        i, j = 0, 2
    elif file_name.find('cm') != -1:
        eixo_x = 'cl'
        eixo_y = 'cm'    
        i, j = 2, 3

    # Ler os resultados da simulação
    x_est = []
    y_est = []

    with open('resultados.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Pular o cabeçalho
        
        for linha in leitor_csv:
            x_est.append(float(linha[i]))
            y_est.append(float(linha[j]))

    # Criar o gráfico
    plt.scatter(dados_x, dados_y)
    plt.plot(x_est, y_est, '-*')
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)
    plt.title('Gráfico ' + eixo_y)
    plt.grid(True)
    # Define o caminho e nome do arquivo de destino
    caminho_arquivo = 'graphics/' + eixo_y + "60.png"
    # Salva o gráfico no arquivo especificado
    plt.savefig(caminho_arquivo)
    plt.close()

def grafico_erro(file_name):
    # Ler os dados reais presentes no arquivo 
    file = 'data/' + file_name
    with open(file, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Extrair os valores do eixo x e y
    dados_x = []
    dados_y = []
    for linha in linhas[4:]:
        valores = linha.split()
        dados_x.append(float(valores[0]))
        dados_y.append(float(valores[1]))

    j = -1
    if file_name.find('cd') != -1:
        eixo_y = 'cd'
        j = 1
    elif file_name.find('cl') != -1:
        eixo_y = 'cl'     
        j = 2
    elif file_name.find('cm') != -1:
        eixo_y = 'cm'    
        j = 3

    # Ler os resultados da simulação
    x_est = []
    y_est = []

    with open('resultados.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Pular o cabeçalho
        
        for linha in leitor_csv:
            x_est.append(float(linha[0]))
            y_est.append(float(linha[j]))
        
    # Calcular o erro em cada ponto
    erros = []
    for y, y_estimado in zip(dados_y, y_est):
        erro = abs(y - y_estimado)
        erros.append(erro)

    # Calcular o erro quadrático médio (RMSE)
    soma_quadrados = sum([erro**2 for erro in erros])
    rmse = math.sqrt(soma_quadrados / len(erros))

    print("Erros individuais:", erros)
    print("RMSE:", rmse)

    # Plotar o gráfico do erro em relação ao eixo x (dados_x)
    plt.plot(x_est, erros, 'o')
    plt.xlabel('alpha')
    plt.ylabel('Erro')
    plt.title('Gráfico de Erro')
    plt.grid(True)
    # Define o caminho e nome do arquivo de destino
    caminho_arquivo = 'graphics/erro' + eixo_y + "60.png"
    # Salva o gráfico no arquivo especificado
    plt.savefig(caminho_arquivo)
    plt.close()


    return erro, rmse