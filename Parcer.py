import json
import requests
from collections import defaultdict
from bs4 import BeautifulSoup


class Parser:
    url = ""
    html = ""
    current_site = ""

    def __init__(self, url):
        self.url = url
        if str(url).__contains__("retiva"):
            self.current_site = "retiva"
        else:
            self.current_site = "MarathonBet"
        self.get_html()

    def get_html(self):
        res = requests.get(self.url)
        self.html = res.text

    def get_all_event_marathonbet(self):
        all_players = []
        all_coef = []
        soup = BeautifulSoup(self.html, "lxml")
        all_event = soup.find('div', class_='sport-category-content').find_all('div', class_='bg coupon-row')

        for players in all_event:
            players = players['data-event-name']. \
                replace('- ', '.').split('.')
            player_1 = players[1].strip()
            player_2 = players[3].strip()
            all_players.append(player_1)
            all_players.append(player_2)

        for g in all_event:
            coef_1 = g.find('td', colspan="1").find('span',
                                                    class_="selection-link active-selection").text
            coef_2 = g.find('td', colspan="1").find('span',
                                                    class_="selection-link active-selection"). \
                findNext('span').text
            all_coef.append(coef_1)
            all_coef.append(coef_2)

        return all_players, all_coef

    def get_all_event_retiva(self):
        all_players = []
        all_coef = []
        soup = BeautifulSoup(self.html, "lxml")

        res = soup.find('section', class_='main__content').find('script', type='application/ld+json')
        json_to_parse = str(res).replace('<script type="application/ld+json">', "").replace('</script>', "")
        all_event = json.loads(json_to_parse)

        for players in all_event:
            players = players["name"].replace('— ', '.').split('.')
            player_1 = players[0].strip()
            player_2 = players[1].strip()
            all_players.append(player_1)
            all_players.append(player_2)

        for g in all_event:
            coef_1 = g["offers"][0]["price"]
            coef2 = g["offers"][1]["price"]
            all_coef.append(coef_1)
            all_coef.append(coef2)

        return all_players, all_coef

    def define_arr(self):
        if self.current_site == "retiva":
            return self.get_all_event_retiva()
        else:
            return self.get_all_event_marathonbet()

    def create_arr_couple(self):
        arr_players = self.define_arr()[0]
        arr_couple = []
        for i in range(0, len(arr_players), 2):
            arr_couple.append(arr_players[i] + '.' + arr_players[i + 1])
        return arr_couple

    def create_dict(self):
        cat = defaultdict(list)
        arr_couple = self.create_arr_couple()
        arr_key = self.define_arr()[1]
        scet = 0
        try:
            for i in range(len(arr_couple)):
                cat[arr_couple[i]].append(arr_key[scet])
                cat[arr_couple[i]].append(arr_key[scet + 1])
                scet += 2
            return dict(cat)
        except IndexError:
            print('ERROR!')
