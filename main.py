import eel
from Financial_Model_Builder import buildFile
eel.init("Financial_Modelling")  
@eel.expose    
def createModel(tickerSymbol, companyName, currentPrice, companyFloat):
    buildFile(tickerSymbol, companyName, currentPrice, companyFloat)
eel.start("index.html", size=(700, 500))