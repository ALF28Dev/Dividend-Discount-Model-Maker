# Dividend Discount Model Maker

> **_NOTE:_**  This project utilises web scraping technology. Please use responsibly and dont send too many requests.

<img width="1583" alt="Screenshot 2022-05-24 at 12 21 26" src="https://user-images.githubusercontent.com/87500491/170023278-de379d30-d9e0-45bf-9dde-343d2b83995b.png">


Im passionate about financial markets and investing. Im also a motivated programmer who likes to apply his skills to solve problems. After spending hours of time developing Excel models manually I decided to build an application to automatically scrape the web for company fundamentals and build Excel models. The application I have developed has saved me hours of time when valueing companies using the dividend discount financial model.

## Requirements
```
yfinance==0.1.63
requests==2.23.0
beautifulsoup4==4.9.1
Eel==0.14.0
pandas==1.2.4
openpyxl==3.0.10
```

## Setup
```Python3
pip3 install -r requirements.txt
```

![Screenshot 2022-05-24 at 16 40 02](https://user-images.githubusercontent.com/87500491/170076387-f8d4cd53-d7e2-4132-9e06-a43aed5802fc.png)


The application takes 4 parameters which enable it to find and build the model. The company ticker symbol, current price and company float are all standard information. However the company name is more specific. Im currently using webscraping to gather the data related to specific companies from a site called https://www.macrotrends.net. This site provides the fundamentals for a specific company. The input for the company name is the URL parameter for thyat specific company. For example coca cola becomes cocacola etc.
