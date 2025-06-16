from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'Title': [], 'Price': [], 'URL Link': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding='utf-8') as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        cards = soup.find_all('div', class_='puis-card-container')
        for card in cards:
            try:
                h2 = card.find('h2', class_='a-size-medium a-spacing-none a-color-base a-text-normal')
                title = h2.get_text(strip=True) if h2 else 'N/A'

                a_tag = h2.find_parent('a', href=True) if h2 else None
                link = "https://www.amazon.in" + a_tag['href'] if a_tag else 'N/A'

                price_span = card.find('span', class_='a-price-whole')
                price = price_span.get_text(strip=True).replace(',', '') if price_span else 'N/A'

                d['Title'].append(title)
                d['Price'].append(price)
                d['URL Link'].append(link)

            except Exception as inner_e:
                print(f"Error parsing a card: {inner_e}")

    except Exception as e:
        print(f"Error reading file {file}: {e}")

df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)
