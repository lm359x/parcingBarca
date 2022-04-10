from bs4 import BeautifulSoup
import codecs
import csv
import requests

URL = "https://www.euro-football.ru/team/Barselona/match_comming"

# TODO тащить с сайта а не локального файла
# TODO не использовать списки, обращаться по классам?

def create_csv(match_list):
    columns = ["date", "time", "turnir", "team1", "team2"]
    formatted_match_info = []
    for football_match in match_list:
        match_info = dict()
        match_info = {"date": football_match.contents[1].string.strip(),
                      "time": football_match.contents[3].string.strip(),
                      "turnir": football_match.contents[5].string.strip(),
                      "team1": football_match.contents[7].contents[1].contents[1].string.strip(),
                      "team2": football_match.contents[7].contents[1].contents[5].string.strip()}
        formatted_match_info.append(match_info)
    with open("users.csv", "w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writerows(formatted_match_info)


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    web_site = requests.get(URL).text
    soup = BeautifulSoup(web_site,"lxml")
    matches = soup.findAll("div", class_="team-match__item")
    create_csv(matches)
    # то что ниже для локального файла
    # with open(web_site, "r", "utf_8_sig") as file:
    #     src = file.read()
    #     soup = BeautifulSoup(src, "lxml")
    #     matches = soup.findAll("div", class_="team-match__item")
    #     create_csv(matches)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
