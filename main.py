from tarefa import Tarefa
from escalonador import Escalonador
import logging, time


def createLogger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
    logger.debug("Logger Created")
    return logger

logger = createLogger()

def sleep(tempo):
    time.sleep(tempo)

def contador(limite):
    for i in range(limite):
        logger.debug(f"Contador: {i}")
        time.sleep(1)  

def imprimir_status():
    status = ["Iniciando", "Conectando", "Carregando", "Executando", "Finalizando"]
    for msg in status:
        logger.debug(f"Status: {msg}")
        time.sleep(1)

def contas():
    logger.debug(15 + 23)
    time.sleep(1)  

    logger.debug(50 - 17)
    time.sleep(1)  

    logger.debug(12 * 8)
    time.sleep(1)  

    logger.debug(100 / 4)
    time.sleep(1)  

    logger.debug(27 % 5)
    time.sleep(1)  

    logger.debug(2**8)
    time.sleep(1)  

    logger.debug(64**0.5)
    time.sleep(1)  

    logger.debug((14 + 6) * 3 - 10)
    time.sleep(1)  

    logger.debug(100 / (5 + 5))
    time.sleep(1)  

    logger.debug(3.14 * 2)
    time.sleep(1)  

    logger.debug(10.5 / 0.5)
    time.sleep(1)  

    logger.debug((5 + 10 + 15) / 3)
    time.sleep(1)  

    logger.debug(3.14159 * 4**2)
    time.sleep(1)  

    logger.debug(int(15 > 10))
    time.sleep(1)  

    logger.debug(int(20 == 21))
    time.sleep(1)  

    logger.debug(5 << 2)
    time.sleep(1)  

    logger.debug(12 & 5)
    time.sleep(1)  

    logger.debug(2.71828**2)
    time.sleep(1)  

    logger.debug(2.302585)
    time.sleep(1)  

def main():

    quantum = 4
    escalonador = Escalonador(quantum)
    tarefas = [ Tarefa(nome = "sleep", funcao = sleep, args = (15,)),
               Tarefa(nome = "contador", funcao =  contador, args = (21,)),
               Tarefa(nome = "contas", funcao = contas, args = ()),
               Tarefa(nome = "status", funcao = imprimir_status, args = ())
               ]

    for tarefa in tarefas:
        escalonador.addTarefa(tarefa)
    try:
        escalonador.executar()
        logger.debug(f"Escalonador funcinal")
    except Exception as e:
        logger.exception(f"Falha ao executar o escalonador: {e}")
            
if __name__ == "__main__":
    main()

