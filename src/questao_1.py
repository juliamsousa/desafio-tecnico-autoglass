import logging

logging.basicConfig(filename='../logs/questao_1.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def multiply_numbers(first_number: int, second_number:int) -> int:
    try:
        if not isinstance(first_number, int) and not isinstance(first_number, float):
            raise TypeError()

        if not isinstance(second_number, int) and not isinstance(second_number, float):
            raise TypeError()

        first_number = round(first_number)
        second_number = round(second_number)
        result = first_number * second_number

        return result

    except TypeError:
        logger.error('Erro na execução')

        print('Os parâmetros passados devem ser números!')
        return False


if __name__ == '__main__':
    logger.info('Executando a questão 1')

    print('Executando o teste')
    test_result = multiply_numbers(7, 2)
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = multiply_numbers(5.8, 2.3)
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = multiply_numbers(10, 1.1)
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = multiply_numbers(1.5, 8)
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = multiply_numbers('a', 'b')
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = multiply_numbers(1, 'b')
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = multiply_numbers('a', '1')
    print(f'Resultado do teste: {test_result} \n')

    logger.info('Fim da execução da questão 1')
