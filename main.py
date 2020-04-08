import requests
from bs4 import BeautifulSoup
import datetime
import json

url = 'http://menu.hfs.psu.edu/shortmenu.aspx?sName=Penn+State+Housing+and+Food+Services'

west = '&locationNum=16&locationName=West+Food+District&naFlag=1'
north = '&locationNum=17&locationName=North+Food+District&naFlag=1'
south = '&locationNum=13&locationName=South+Food+District&naFlag=1'
east = '&locationNum=11&locationName=East+Food+District&naFlag=1'
pollock = '&locationNum=14&locationName=Pollock+Dining+Commons+&naFlag=1'

menu = {}


def get_menu(locationUrl):
    page = requests.get(
        "http://menu.hfs.psu.edu/shortmenu.aspx?sName=Penn+State+Housing+and+Food+Services" + locationUrl)
    content = BeautifulSoup(page.content, 'html.parser')

    table = content.find('table', attrs={'id': 'menuDisplay'})

    meals = table.find_all('table', attrs={'class': 'collapse'})

    count = 0

    for meal in meals:
        meal_type = meal.find('td', attrs={'class': 'meal-header'}).get_text().strip()
        # menu[meal_type] = meal

        html_categories = meal.find_all('div', attrs={'class': 'nutmenucats'})
        categories = {};

        for cat in html_categories:
            item_list = [];

            isNextCat = False

            next = cat;
            while isNextCat == False:

                next = next.findNext('tr').find('div', attrs={'class': 'shortmenurecipes'})

                if next and next.findNext('tr').findNext('div', attrs={'class': 'shortmenurecipes'}):
                    item_list.append(
                        next.get_text().strip())
                else:
                    isNextCat = True

            categories[cat.get_text().strip().replace("-", "")] = item_list

            menu[meal_type] = categories

    return menu


def main(request):

    all_menus = {
        'west':get_menu(west),
        'north':get_menu(north),
        'south':get_menu(south),
        'east':get_menu(east),
        'pollock':get_menu(pollock)

        }

    return json.dumps(all_menus)
    




