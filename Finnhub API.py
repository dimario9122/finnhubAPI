import requests
import json

#токен API
token = 'your_token_API'

#массив с названиями фондов
ETF = [['ESGU', 'iShares ESG Aware MSCI USA ETF'], ['VOO', 'Vanguard S&P 500 ETF'],
       ['VTV', 'Vanguard Value ETF'], ['DSTL', 'Distillate U.S. Fundamental Stability & Value ETF'],
       ['SCHA', 'Schwab US Small-Cap ETF'], ['XLI', 'Industrial Select Sector SPDR Fund'],
       ['PBW', 'Invesco WilderHill Clean Energy ETF'], ['JHMC', 'John Hancock Multifactor Consumer Discretionary ETF'],
       ['BETZ', 'Roundhill Sports Betting & iGaming ETF'], ['DSTL', 'Distillate U.S. Fundamental Stability & Value ETF'],
       ['KBWB', 'Invesco KBW Bank ETF'], ['FINX', 'Global X FinTech ETF'],
       ['ARKK', 'ARK Innovation ETF'], ['IPO', 'Renaissance IPO ETF'],
       ['IEHS', 'iShares Evolved U.S. Healthcare Staples ETF'], ['MSOS', 'AdvisorShares Pure US Cannabis ETF'],
       ['XSOE', 'WisdomTree Emerging Markets ex-State-Owned Enterprises Fund'], ['EMLC', 'VanEck Vectors J.P. Morgan EM Local Currency Bond ETF'],
       ['VTEB', 'Vanguard Tax-Exempt Bond ETF'], ['ICSH', 'BlackRock Ultra Short-Term Bond ETF'],
       ['BAR', 'GraniteShares Gold Trust']]

#функция проверки введенного числа
def check(number, max):
    try:
        int(number)
        if ((int(number) < 0) or (int(number) > max)):
            return -1
        else:
            return int(number)
    except ValueError:
        return -1

#функция вывода информации о новостях для фонда
def print_news_mood(data):
    print('оценка новостей компании : ', data['companyNewsScore'])
    print('средний Бычий процент по сектору : ', data['sectorAverageBullishPercent'])
    print('средний показатель новостей по сектору : ', data['sectorAverageNewsScore'])

#функция вывода информации о воздействие фонда на различные отрасли
def print_exposure_to_the_ETFs_sector(data):
    for i in range(len(data['sectorExposure'])):
        print('Отрасль : ', data['sectorExposure'][i]['industry'],
              ' процент воздействия в данной отрасли : ', data['sectorExposure'][i]['exposure'])

#функция вывода информации о воздействие фонда в различых странах
def print_country_exposure_of_ETFs(data):
    for i in range(len(data['countryExposure'])):
        print('Страна : ', data['countryExposure'][i]['country'],
              ' процент воздействия в данной стране : ', data['countryExposure'][i]['exposure'])

#функция получения информации о новостях для фонда
def news_mood(choice_etf, token):
    params = {'symbol': choice_etf, 'token': token}
    r = requests.get('https://finnhub.io/api/v1/news-sentiment?', params=params)
    print_news_mood(r.json())

#функция получения информации о воздействие фонда на различные отрасли
def exposure_to_the_ETFs_sector(choice_etf, token):
    params = {'symbol': choice_etf, 'token': token}
    r = requests.get('https://finnhub.io/api/v1/etf/sector?', params=params)
    print_exposure_to_the_ETFs_sector(r.json())

#функция получения информации о воздействие фонда в различых странах
def country_exposure_of_ETFs(choice_etf, token):
    params = {'symbol': choice_etf, 'token': token}
    r = requests.get('https://finnhub.io/api/v1/etf/country?', params=params)
    print_country_exposure_of_ETFs(r.json())

#функция выбора вызова функции
def do_function(choice_etf, choice_function, token):
    if choice_function == 1:
        news_mood(choice_etf, token)
    if choice_function == 2:
        exposure_to_the_ETFs_sector(choice_etf, token)
    if choice_function == 3:
        country_exposure_of_ETFs(choice_etf, token)

if __name__ == "__main__":
    choice = -1
    choice_etf = -1
    choice_function = -1
    while (choice == -1):
        #вывод всех фондов на экран
        for i in range(len(ETF)):
            print(str(i+1),' - ', ETF[i][0], ' - ', ETF[i][1])
        while not ((choice_etf > -1) and (choice_etf < len(ETF)+1)):
            print('Введите номер ETF и нажмите enter'
                  '\n0 - Выход из программы')
            choice_etf = check(input(), len(ETF))
            choice_function=-1
        if (choice_etf==0): break;
        # вывор функции для получения информации
        while (choice_function != 0):
            while not ((choice_function > -1) and (choice_function < 4)):
                print('Выберите информацию для получения\n'
                      '0 - Отмена\n'
                      '1 - новостное настроение\n'
                      '2 - воздействие на сектор ETF\n'
                      '3 - страновая экспозиция ETF\n')
                choice_function = check(input(), 4)
            if(choice_function != 0):
                do_function(ETF[choice_etf-1][0], choice_function, token)
                choice_function = -1
            else:
                choice_etf = -1