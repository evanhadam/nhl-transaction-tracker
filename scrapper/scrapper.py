from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
import time

class PlayerList:
    def __init__(self):
        self.dateList = []
        self.lastSigning = []
        self.signingList = []

    def addCurrentDate(self):
        today = date.today()
        dateStr = today.strftime('%B %d, %Y')
        self.dateList.append(dateStr)

    def getSigningLists(self):
        driver = webdriver.Firefox()
        driver.get(f'https://en.wikipedia.org/wiki/2022%E2%80%9323_NHL_transactions#Trades')
        playerList = []

        time.sleep(5)

        players = driver.find_elements(By.CLASS_NAME, "wikitable")
        for player in players:
            text = player.text
            playerList.append(text)

        players = playerList[2]
        players = players[0:players.index("\n")]
        signings = playerList[2].split("\n")
        signings = signings[1:]
        print(signings)

        self.signingList = signings

    def parseItems(playerList):
        parsedList = []
        teamList = ['Anaheim Ducks', 'Arizona Coyotes', 'Boston Bruins', 'Buffalo Sabres', 'Calgary Flames', 'Carolina Hurricanes', 'Chicago Blackhawks', 'Colorado Avalanche', 'Columbus Blue Jackets', 'Dallas Stars', 'Detroit Red Wings', 'Edmonton Oilers', 'Florida Panthers', 'Los Angeles Kings', 'Minnesota Wild', 'Montreal Canadiens', 'Nashville Predators', 'New Jersey Devils', 'New York Islanders', 'New York Rangers', 'Ottawa Senators', 'Philadelphia Flyers', 'Pittsburgh Penguins', 'San Jose Sharks', 'Seattle Kraken', 'St. Louis Blues', 'Tampa Bay Lightning', 'Toronto Maple Leafs', 'Vancouver Canucks', 'Vegas Golden Knights', 'Washington Capitals', 'Winnipeg Jets']

        #date, player, newTeam, oldTeam
        for item in enumerate(playerList):
            date = item[0:(item.index("2022") + 4)]
            player = ''
            newTeam = ''
            oldTeam = ''

            key = ""
            for word in teamList:
                if word in item:
                    key = word
            player = item[(item.index("2022") + 5):(item.index(key) - 1)]
            newTeam = key
            oldTeam = item[item.index(key) + (len(key) + 1):item.index("[") - 1]

            parsedList.append([date, player, newTeam, oldTeam])

        return parsedList

    #def signingsToCSV(parsedList):
        
#player = PlayerList()
#player.getSigningLists()