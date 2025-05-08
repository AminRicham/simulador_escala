from multiprocessing import Process
from signal import SIGSTOP, SIGCONT
import logging

class Tarefa:
    def __init__(self, nome, funcao, args):
        self.nome = nome
        self.funcao = funcao
        self.args = args
        self._pid = None
        self.processo = None
        
        self.logger = logging.getLogger(__name__)
        
    def iniciar(self):
        """Inicia o processo da tarefa"""
        try:
            if self.processo is None:
                self.processo = Process(target=self.funcao, args=self.args)
                self.processo.start()
                self._pid = self.processo.pid
                self.logger.info(f"Processo {self.processo.name} iniciado (PID: {self._pid})")
                return True
        
            return False
        
        except Exception as e:
            self.logger.error(f"Erro ao iniciar: {e}")
            return False
    