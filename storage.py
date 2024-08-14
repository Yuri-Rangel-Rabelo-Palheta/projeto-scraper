import csv

def save_to_csv(data, filename):
    # Defina os nomes dos campos (colunas) que o CSV terá
    fieldnames = ['name', 'email', 'phone']  # Adicione 'name' e 'phone'

    # Abra o arquivo para escrita
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados de cada cliente
        for cliente in data:
            writer.writerow(cliente)
