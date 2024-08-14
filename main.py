from scraper import fetch_page_content
from parser import parse_client_data
from storage import save_to_csv
from google_scraper import search_google
from linkedin_scraper import search_linkedin
from url_loader import load_urls_from_file


def main():
    google_query = 'advogados em belém'
    linkedin_query = 'advogados em belém'

    # Carregar URLs fixas a partir de um arquivo
    url_fixa = load_urls_from_file("url.txt")

    # Buscar URLs dinâmicas usando os scrapers do Google e LinkedIn
    google_urls = search_google(google_query)
    linkedin_urls = search_linkedin(linkedin_query)
    
    # Combinar todas as URLs
    all_urls = google_urls + linkedin_urls + url_fixa

    print(all_urls)
    
    all_clients = []
    for url in all_urls:
        attempts = 3
        use_selenium = "linkedin.com" in url or "glassdoor.com" in url  # Decidir se usa Selenium

        while attempts > 0:
            page_content = fetch_page_content(url, use_selenium=use_selenium)  # Usar Selenium quando necessário
            if page_content:
                clientes = parse_client_data(page_content)
                all_clients.extend(clientes)
                break
            else:
                attempts -= 1
                print(f"Tentando novamente {url}... Tentativas restantes: {attempts}")
        
        if attempts == 0:
            print(f"Falha ao buscar conteúdo da página: {url} após várias tentativas")

    # Salvar os dados coletados em um arquivo CSV
    if all_clients:
        save_to_csv(all_clients, 'clientes.csv')
    else:
        print("Nenhum dado de cliente encontrado.")

if __name__ == "__main__":
    main()




""" from scraper import fetch_page_content
from parser import parse_client_data
from storage import save_to_csv
from google_scraper import search_google
from linkedin_scraper import search_linkedin
from url_loader import  load_urls_from_file



def main():
    google_query = 'advogados em belém'
    linkedin_query = 'advogados em belém'

    # Buscar URLs
    url_fixa = load_urls_from_file("url.txt")

    google_urls = search_google(google_query)
    linkedin_urls = search_linkedin(linkedin_query)
    
    all_urls = google_urls + linkedin_urls + url_fixa

    print(all_urls)
    
    all_clients = []
    for url in all_urls:
        attempts = 3
        while attempts > 0:
            page_content = fetch_page_content(url)
            if page_content:
                clientes = parse_client_data(page_content)
                all_clients.extend(clientes)
                break
            else:
                attempts -= 1
                print(f"Tentando novamente {url}... Tentativas restantes: {attempts}")
        
        if attempts == 0:
            print(f"Falha ao buscar conteúdo da página: {url} após várias tentativas")

    if all_clients:
        save_to_csv(all_clients, 'clientes.csv')
    else:
        print("Nenhum dado de cliente encontrado.")

if __name__ == "__main__":
    main()

 """

""" from scraper import fetch_page_content
from parser import parse_client_data
from storage import save_to_csv
from google_scraper import search_google
from linkedin_scraper import search_linkedin

def main():
    # Consultas de pesquisa
    google_query = 'advogado em belém'
    linkedin_query = 'advogado'

    # Buscar URLs
    google_urls = search_google(google_query)
    linkedin_urls = search_linkedin(linkedin_query)
    
    all_urls = google_urls + linkedin_urls
    
    all_clients = []
    for url in all_urls:
        page_content = fetch_page_content(url)
        if page_content:
            clientes = parse_client_data(page_content)
            all_clients.extend(clientes)
        else:
            print(f"Falha ao buscar conteúdo da página: {url}")

    if all_clients:
        save_to_csv(all_clients, 'clientes.csv')
    else:
        print("Nenhum dado de cliente encontrado.")

if __name__ == "__main__":
    main()
 """


""" from scraper import fetch_page_content
from parser import parse_client_data
from storage import save_to_csv
from google_scraper import search_google
from linkedin_scraper import search_linkedin

def main():
    # Consultas de pesquisa
    google_query = 'advogados em belém'
    linkedin_query = 'advogados em belém'

    # Buscar URLs
    google_urls = search_google(google_query)
    linkedin_urls = search_linkedin(linkedin_query)
    
    all_urls = google_urls + linkedin_urls
    
    all_clients = []
    for url in all_urls:
        page_content = fetch_page_content(url)
        if page_content:
            clientes = parse_client_data(page_content)
            all_clients.extend(clientes)
        else:
            print(f"Falha ao buscar conteúdo da página: {url}")

    if all_clients:
        save_to_csv(all_clients, 'clientes.csv')
    else:
        print("Nenhum dado de cliente encontrado.")

if __name__ == "__main__":
    main() """