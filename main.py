from src.ola_mundo import ola_mundo
import logging

if __name__ == '__main__':
    logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info('Executando a função ola_mundo')

    message = ola_mundo()
    print(message)
