import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Get all match statistics for a soccer league in specified year
def get_historical(leagues:list,start_year=15,end_year=21):
    dict_historical_data = {}
    for league in leagues:
        frames = []
        for i in range(start_year,end_year):
            df = pd.read_csv("http://www.football-data.co.uk/mmz4281/"+str(i)+str(i+1)+"/"+league+".csv")
            df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']] #choose any column you want
            df = df.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
            df = df.assign(Season=i)
            frames.append(df)
        df_historical_data = pd.concat(frames)
        dict_historical_data[league] = df_historical_data
    return dict_historical_data


# Get matches left to be played in current active season
def get_matches_left(leagues:list):
    # matches_DF = pd.DataFrame(columns=['Date','Time','Home','Away'])
    driver_path = 'lib/chromedriver.exe'
    # Webdriver Options and init
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-sh-usage')
    driver = webdriver.Chrome(driver_path, options=option)
    driver.maximize_window()
    all_fixtures = []
    for league in leagues:
        driver.get(f'https://www.skysports.com/{league}-fixtures')
        content = driver.page_source
        soup = BeautifulSoup(content, features="lxml")
        for div in soup.findAll('div', attrs={'class': 'fixres__item'}):
            time = div.find('span', attrs={'class': 'matches__date'})
            home = div.find('span', attrs={'class': 'matches__item-col matches__participant matches__participant--side1'})
            home = home.find('span', attrs={'class': 'swap-text__target'})
            away = div.find('span', attrs={'class': 'matches__item-col matches__participant matches__participant--side2'})
            away = away.find('span', attrs={'class': 'swap-text__target'})
            curr_rec = {
                'Date': '',
                'Time': time.text.strip(),
                'League': league.replace('-',' ').title(),
                'Home': home.text,
                'Away': away.text,
            }
            all_fixtures.append(curr_rec)
    matches_DF = pd.DataFrame(all_fixtures)
    return matches_DF
