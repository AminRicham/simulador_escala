# Simulador de um Escalonador Round Robin

Este é um projeto desenvolvido para a disciplina de **Sistemas Operacionais 1**, com o objetivo de simular o funcionamento de um **escalonador de processos do tipo Round Robin**.

---

## 📌 Descrição

O escalonador implementado neste projeto gerencia a execução de várias tarefas simuladas como processos independentes, utilizando o algoritmo **Round Robin**. Cada tarefa recebe uma fatia de tempo (quantum) para execução. Caso a tarefa não termine dentro desse tempo, ela é pausada e colocada de volta na fila, permitindo que a próxima tarefa seja executada. Esse processo se repete até que todas as tarefas sejam finalizadas.

O projeto utiliza a biblioteca `multiprocessing` para simular a execução concorrente de processos reais, com controle de execução usando sinais (`SIGSTOP`, `SIGCONT`), e inclui **logs detalhados** salvos em `log.txt`.

---

## ▶️ Como Executar

### 1. **Pré-requisitos**
Certifique-se de estar usando o **Python 3.8+** e que o sistema operacional seja compatível com **sinais Unix (como Linux ou MacOS)**. Este projeto **não funciona no Windows** devido ao uso de sinais `os.kill` com `SIGSTOP` e `SIGCONT`.

### 2. **Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
