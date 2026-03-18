
Relatório de Experimento: Soma Paralela de Vetores
Disciplina: Computação Paralela

Aluno: João Gabriel Lucas

Professor: Rafael 

Turma: ADS Noite

Data: 18 de Março de 2026

1. Descrição do Problema
Problema Implementado: Soma de um grande conjunto de números inteiros extraídos de um arquivo de texto.

Algoritmo: Soma acumulativa simples (redução). Na versão paralela, o vetor é dividido em n partes iguais (chunks), onde cada thread calcula a soma de sua parte e, ao final, o programa consolida os resultados parciais.

Tamanho da Entrada: Arquivo numero2.txt contendo aproximadamente 1.000.000 de registros.

Objetivo da Paralelização: Diminuir o tempo de resposta do cálculo distribuindo a carga de processamento entre múltiplos núcleos da CPU.

Complexidade: O(n), onde n é o número de elementos no arquivo.

2. Ambiente Experimental
<img width="385" height="174" alt="image" src="https://github.com/user-attachments/assets/d28f1dac-07a9-4902-8184-105b584c6ec5" />

3. Metodologia de Testes
Medição de Tempo: Utilizada a função time.time() para capturar o timestamp inicial e final, calculando a diferença em segundos.

Execuções: Foram realizadas múltiplas execuções para cada configuração para garantir a consistência dos dados.

Configurações: Testadas as variações de 1 (Serial), 2, 4, 8 e 12 threads.

Condições: Máquina em estado de repouso (sem outras aplicações pesadas rodando) para minimizar interferências externas no escalonador do SO.

4. Resultados Experimentais
<img width="332" height="128" alt="image" src="https://github.com/user-attachments/assets/01a72927-27a7-498a-98ef-7ad82b30a627" />


5. Cálculo de Speedup e Eficiência
Utilizando o tempo serial (T1 =0.027144) como base:

Speedup (S): S=T1/Tp
​
Eficiência (E): E=S/p

6. Tabela de Resultados Consolidados
<img width="258" height="154" alt="image" src="https://github.com/user-attachments/assets/f7f67636-7507-4e16-ae70-6615a3dd5ebe" />

7. Gráfico de Tempo de Execução
<img width="752" height="451" alt="image" src="https://github.com/user-attachments/assets/1bf1da64-d346-4c40-a318-91934a1dfd16" />

9. Gráfico de Speedup
<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/93aa7f24-8962-4459-a109-542fd2c820dd" />

11. Gráfico de Eficiência
<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/7de3160f-38f3-4337-a9ea-09039ebd42b3" />

13. Análise dos Resultados
Speedup: O speedup obtido foi negativo (abaixo de 1.0). Isso significa que a versão paralela foi mais lenta que a serial.

Escalabilidade: A aplicação não apresentou escalabilidade. O aumento de threads resultou em aumento de tempo.

Overhead: Houve um alto custo de criação e sincronização de threads. Como a operação de soma é muito simples, o tempo para gerenciar as threads foi maior que o tempo para processar os dados.

Causa Principal (GIL): O Python utiliza o Global Interpreter Lock (GIL), que impede que múltiplas threads executem código Python simultaneamente em diferentes núcleos. Isso causou uma contenção onde as threads disputavam o mesmo núcleo, gerando atraso.

11. Conclusão
O paralelismo via threads em Python não trouxe ganhos de desempenho para este problema de soma. O melhor desempenho foi obtido na versão Serial.
Para este tipo de tarefa (CPU-bound), a melhoria recomendada seria utilizar a biblioteca multiprocessing, que contorna o GIL, ou o uso de bibliotecas de baixo nível como NumPy, que realizam a computação paralela em nível de C.

