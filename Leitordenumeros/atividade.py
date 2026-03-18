import threading
import time
import os

# Função para realizar a soma serial
def soma_serial(dados):
    inicio = time.time()
    total = sum(dados)
    fim = time.time()
    return total, fim - inicio

# Função que cada thread executará
def worker_soma(sub_lista, resultados, index):
    resultados[index] = sum(sub_lista)

# Função para realizar a soma paralela
def soma_paralela(dados, num_threads):
    tamanho_bloco = len(dados) // num_threads
    threads = []
    resultados = [0] * num_threads
    
    inicio = time.time()
    for i in range(num_threads):
        inicio_idx = i * tamanho_bloco
        # A última thread pega o resto da lista caso a divisão não seja exata
        fim_idx = None if i == num_threads - 1 else (i + 1) * tamanho_bloco
        sub_lista = dados[inicio_idx:fim_idx]
        
        t = threading.Thread(target=worker_soma, args=(sub_lista, resultados, i))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    total_final = sum(resultados)
    fim = time.time()
    return total_final, fim - inicio

# --- Execução do Experimento ---

nome_arquivo = 'numerogigante.txt'

if not os.path.exists(nome_arquivo):
    print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
else:
    # Carregamento dos dados do arquivo real
    with open(nome_arquivo, 'r') as f:
        # Lê cada linha, converte para int se não estiver vazia
        numeros = [int(linha.strip()) for linha in f if linha.strip()]

    print(f"Total de elementos lidos: {len(numeros)}")
    print("-" * 50)

    # Teste Serial
    res_s, tempo_s = soma_serial(numeros)

    # Teste Paralelo (2, 4, 8, 12 threads)
    resultados_experimento = []
    for n in [2, 4, 8, 12]:
        res_p, tempo_p = soma_paralela(numeros, n)
        resultados_experimento.append((n, res_p, tempo_p))

    # Exibição dos Resultados (Tabela baseada nos seus dados de exemplo)
    print(f"{'Configuração':<15} | {'Soma Real':<12} | {'Tempo (s)':<12}")
    print("-" * 50)
    print(f"{'Serial':<15} | {res_s:<12} | {tempo_s:.6f}s")
    
    for n, soma, t in resultados_experimento:
        print(f"{n} Threads {'':<5} | {soma:<12} | {t:.6f}s")