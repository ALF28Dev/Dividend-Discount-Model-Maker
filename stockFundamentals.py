import requests
from bs4 import BeautifulSoup

class information:
    def __init__(self, ticker, companyName):
        self.ticker = ticker
        self.companyName = companyName
        self.url = "https://www.macrotrends.net/stocks/charts/"+self.ticker+"/"+self.companyName+"/"

    ''' Use BeautifulSoup to parse web data and return the data within the html table. '''
    def parser(self, URL):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        tables = soup.find_all("table", class_="historical_data_table table")
        data = tables[0].find_all("td")
        return data

    ''' Take web data and place it within a hashmap. Data is easier to understand/manipulate in this format. '''
    def returnData(self, data):
        year = None
        results = {}
        for row in data:
            if row.text[0] == "$":
                removeDollar = row.text.strip('$')
                dataValue = removeDollar.replace(',', '')
                results[year] = dataValue
            else:
                year = row.text
        return results

    ''' Get company net income '''
    def net_income(self):
        URL = self.url+"net-income"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company revenue '''
    def revenue(self):
        URL = self.url+"revenue"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company gross profit '''
    def gross_profit(self):
        URL = self.url+"gross-profit"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company operating income '''
    def operating_income(self):
        URL = self.url+"operating-income"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company eps '''
    def earnings_per_share(self):
        URL = self.url+"eps-earnings-per-share-diluted"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company shares outstanding '''
    def shares_outstanding(self):
        URL = self.url+"shares-outstanding"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company total assets '''
    def total_assets(self):
        URL = self.url+"total-assets"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company cash '''
    def cash_on_hand(self):
        URL = self.url+"cash-on-hand"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company debts '''
    def long_term_debt(self):
        URL = self.url+"long-term-debt"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company liabilities '''
    def total_liabilities(self):
        URL = self.url+"total-liabilities"
        data = self.parser(URL)
        return self.returnData(data)
    
    ''' Get company shareholder equity '''
    def total_share_holder_equity(self):
        URL = self.url+"total-share-holder-equity"
        data = self.parser(URL)
        return self.returnData(data)

    ''' Get company cashflow '''
    def cash_flow(self):
        URL = self.url+"cash-flow-from-operating-activities"
        data = self.parser(URL)
        return self.returnData(data)