# FlyFood - Roteirização de Entregas (Versão Força Bruta)

🛸 FlyFood - Roteirização de Entregas com Drones FlyFood é um projeto acadêmico que simula um sistema de entregas utilizando drones em uma cidade representada por uma matriz. A proposta surgiu diante do desafio de realizar múltiplas, Essa versão contém uma solução bruta baseada no Problema do Caixeiro Viajante (TSP).

O **FlyFood** é uma solução simples e visual para o problema de roteirização de entregas em um grid 2D, aplicando uma abordagem de **força bruta** para encontrar a rota ótima com base na **distância de Manhattan**.

Ideal para fins educacionais e análise comparativa com algoritmos heurísticos ou meta-heurísticos, como o algoritmo de Colônia de Formigas.

## ✨ Funcionalidades

- Leitura dinâmica de uma matriz com ponto de partida e pontos de entrega.
- Cálculo de todas as permutações possíveis das entregas (TSP brute-force).
- Cálculo da distância total da rota usando distância de Manhattan.
- Retorno ao ponto de partida incluso no cálculo.
- Visualização da rota em um gráfico via `matplotlib`.

## 📥 Exemplo de Entrada

Entrada via `stdin` (input padrão). A primeira linha contém as dimensões da matriz, seguida das linhas da matriz:

4 10
a 0 0 I D 0 0 0 L 0
0 A 0 0 0 G 0 0 E 0
0 0 0 b C 0 0 0 0 0
0 0 R 0 0 A 0 T 0 0


- `R` representa o ponto de partida.
- `0` são espaços vazios.
- Letras (maiúsculas e minúsculas) são pontos de entrega.

## 📤 Saída Esperada

Calculando a rota ótima para 11 pontos de entrega...
Solução ótima para a rota: A a b C D E G I L T A
Distância percorrida: 44
Tempo de execução: 0.0465 segundos


Também será exibido um gráfico com a rota ótima desenhada.

## 🧠 Como funciona

1. **Leitura da matriz**: identifica ponto de partida (`R`) e pontos de entrega.
2. **Permutações**: gera todas as ordens possíveis de visitas aos pontos.
3. **Cálculo de custo**: computa a soma das distâncias de Manhattan entre os pontos.
4. **Visualização**: exibe graficamente a rota mais eficiente.

## 📦 Requisitos

- Python 3.7+
- [matplotlib](https://matplotlib.org/)

- Relatório: (https://docs.google.com/document/d/1BHEp4-_55aovDt1U9165fYheern9sPDG9hIsve7ZcE4/edit?usp=sharing)

## Autores:

Francisco José - francisco.jmagalhaes@ufrpe.br
Gilvan Lemos - gilvanlemos7@gmail.com
Mateus Araújo - mateus.araujof@ufrpe.br 
Samuel Pereira - samuel.vasconcelos@ufrpe.br

Orientador:
Rodrigo Gabriel Ferreira Soares - rodrigo.gfsoares@ufrpe.br

Recife
Junho de 2025


