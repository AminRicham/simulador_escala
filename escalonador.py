from queue import Queue
import signal, logging, os, time

class Escalonador:
    def __init__(self, quantum):
        self.quantum = quantum
        self.queue = Queue()
        self.logger = logging.getLogger(__name__)

    def executar(self):
        while not self.queue.empty():
            try:
                tarefaAtual = self.queue.get()
                if tarefaAtual.processo is None:
                    self.iniciaTarefa(tarefaAtual)
                elif tarefaAtual.processo.is_alive():
                    self.resumeTarefa(tarefaAtual)
                else:
                    continue  # Tarefa finalizada

                inicioTempoEmExecucao = time.time()
                while time.time() - inicioTempoEmExecucao < self.quantum:
                    if not tarefaAtual.processo.is_alive():
                        break  # Sai do loop se a tarefa terminar antes do quantum
                    time.sleep(0.1)  # Verifica a cada 0.1s para permitir preempção

                # Pausa a tarefa se ainda estiver rodando
                if tarefaAtual.processo.is_alive():
                    self.paraTarefa(tarefaAtual)
                    self.queue.put(tarefaAtual)
                else:
                    self.logger.info(f"Tarefa {tarefaAtual.nome} finalizada.")
            except Exception as e:
                self.logger.debug(f"Erro no momento de executar o escalonador {e}")
    def addTarefa(self, tarefa):
        try:
            self.queue.put(tarefa)
            self.logger.debug("Tarefa adicionada")
        except Exception as e:
            self.logger.error(f"Erro no momento de adicionar a tarefa {tarefa.nome}")

    def trocaDeContexto(self, tarefaAntiga, tarefaNova):
        try:
            self.paraTarefa(tarefaAntiga)
            self.iniciaTarefa(tarefaNova)
            self.logger.debug(f"Troca de contexto realizada, de {tarefaAntiga.nome}, para {tarefaNova.nome}")
        except Exception as e:
            self.logger.error(f"Erro no momento da troca de contexto. Erro:{e}")

    def iniciaTarefa(self, tarefa):
        try:
            tarefa.iniciar()
            self.logger.debug(f"Tarefa {tarefa.nome} iniciada")
        except Exception as e:
            self.logger.error(f"Erro ao iniciar a tarefa. Erro: {e}")
    
    def resumeTarefa(self,tarefa):
        try:
            os.kill(tarefa.processo.pid, signal.SIGCONT)
            self.logger.debug(f"Tarefa {tarefa.nome} voltou a rodar")
            self.realocaTarefa(tarefa)
        except Exception as e:
            self.logger.error(f"Erro no momento de parar a tarefa. Erro:{e}")
        
    def paraTarefa(self,tarefa):
        try:
            os.kill(tarefa.processo.pid, signal.SIGSTOP)
            self.logger.debug(f"Tarefa {tarefa.nome} pausada")
        except Exception as e:
            self.logger.error(f"Erro no momento de parar a tarefa. Erro:{e}")

    def realocaTarefa(self, tarefa):
        self.queue.put(tarefa)