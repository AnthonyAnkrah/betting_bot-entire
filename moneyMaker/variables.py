driver_path = 'lib/chromedriver.exe'
sites = {
    'yetu': 'https://parimatch.com.gh/',
    # 'mel': 'https://melbet.com.gh/',
    # 'sporty': 'https://www.sportybet.com/gh/'
}
creds = {
    'yetu' : ['',''],
    'mel' : ['',''],
    'sporty' : ['',''],
}
tabs = {}
xpaths = {
    'yetu_cat': "//div[.='A-Z Sport']",
    'mel_cat': "//span[. = 'Sports']",
    'sporty_cat': "//a[@data-path='eventListDefault' and @data-key='eventListDefault']",
}
events = {}
