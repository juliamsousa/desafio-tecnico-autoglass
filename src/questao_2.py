from typing import List
import logging

logging.basicConfig(filename='../logs/questao_2.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def check_even_numbers(number_list: List[int]) -> List[int]:
    try:
        if not isinstance(number_list, List):
            raise TypeError()

        if not all(isinstance(item, int) for item in number_list):
            raise TypeError()

        even_numbers = [number for number in number_list if number % 2 == 0]

        return even_numbers

    except TypeError:
        print('O parâmetro passado deve ser uma lista de números inteiros!')
        logger.error('Erro na execução')
        return []


if __name__ == '__main__':
    logger.info('Executando a questão 2')

    print('Executando o teste')
    test_result = check_even_numbers([])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers([1, 3, 5, 7, 9, 11, 13, 15, 17])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers([2, 4, 6, 8, 10, 12, 14, 16])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers([2.4, 6.8, 10.12, 14.16])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers(['a', 'b'])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers([1, 'b'])
    print(f'Resultado do teste: {test_result} \n')

    print('Executando o teste')
    test_result = check_even_numbers(['a', True])
    print(f'Resultado do teste: {test_result} \n')

    logger.info('Fim da execução da questão 2')
