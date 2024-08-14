import requests
from bs4 import BeautifulSoup
import time
import random

def search_linkedin(query, num_pages=3, results_per_page=10, delay_range=(2, 5)):
    base_url = "https://www.linkedin.com/search/results/people/"
    urls = []
    
    for page in range(num_pages):
        start_index = page * results_per_page
        params = {
            'keywords': query,
            'start': start_index
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontrar e extrair URLs dos perfis
            for profile in soup.find_all('a', class_='app-aware-link'):
                link = profile['href']
                if '/in/' in link:  # Verifica se é um link de perfil
                    urls.append(link)
                
            # Adiciona um delay aleatório entre as requisições
            time.sleep(random.uniform(*delay_range))
        else:
            print(f"Erro ao acessar o LinkedIn: {response.status_code}")
        
    return urls


""" import requests
from bs4 import BeautifulSoup
import time
import random

def search_linkedin(query, num_pages=3, results_per_page=10, delay_range=(2, 5)):
    base_url = "https://www.linkedin.com/search/results/people/"
    urls = []
    
    for page in range(num_pages):
        start_index = page * results_per_page
        params = {
            'keywords': query,
            'start': start_index
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontrar e extrair URLs dos perfis
            for profile in soup.find_all('a', class_='app-aware-link'):
                link = profile['href']
                if '/in/' in link:  # Verifica se é um link de perfil
                    urls.append(link)
                
            # Adiciona um delay aleatório entre as requisições
            time.sleep(random.uniform(*delay_range))
        else:
            print(f"Erro ao acessar o LinkedIn: {response.status_code}")
        
    return urls
 """