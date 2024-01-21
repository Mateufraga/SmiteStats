from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', stats=get_smite_stats())

def get_smite_stats():
    url = "https://smite.guru/profile/500100947-Pudiimm_"
    response = requests.get(url)
    stats = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        findgods = soup.find_all("div", class_="mpc__champion")
        for god in findgods:
            name = god.find('div', class_='mpc__name').get_text(strip=True)
            kda = god.find_all('div', class_='mpc__stats')[0].get_text(strip=True)
            stat = god.find_all('div', class_='mpc__stats')[1].get_text(strip=True)
            stats.append({'name': name, 'kda': kda, 'stats': stat})
    return stats

if __name__ == "__main__":
    app.run(debug=True)
