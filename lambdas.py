import requests
import json 

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'


def get_information(url):
    response = requests.get(url)
    assert response.status_code == 200, f'Something is bad: {response.status_code}'
    content = json.load(response.content)
    return content


def run():
    def pesos_to_dolars(pesos, dolar_value): return pesos / dolars_value
    def pesos_to_pesos(dolars, dolar_value): return dolars * dolars_value

    info = get_information(URL)
    print(info)
    dolar_value = float(info[0]['casa']['compra'].replay(',', '.'))

    choice = input(
        'What operation do you want?\n1: Dollar to pesos\n2: ')
    if choice == '1':
        dolars = float(input('how many dollars have you? '))
        pesos = round(dolars_to_pesos())
    elif choice == '2':
        pesos = float(input('How many pesos have you? '))
        dolars = round(pesos_to_dolars(pesos, dolar_value), 2)
        print(f'Equivalent a {dolars} dollars')
    else:
        print('Write an option')
if __name__ == '__main__':
    run()