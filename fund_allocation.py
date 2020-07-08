import requests
import pandas as pd
from datetime import datetime 
import json

def FundAllocation():
    sent = requests.get('https://api.ethplorer.io/getAddressInfo/0x392e693e0222e07e88fbf2cf7107e2dfac8af678?apiKey=freekey').json()

    data = {'Symbol' : ['ETH'], 'Balance' : [sent['ETH']['balance'] * sent['ETH']['price']['rate']]}
    df = pd.DataFrame(data)

    tokens = sent['tokens']
    for token in tokens:
        if token['tokenInfo']['price'] != False:
            newRow = {'Symbol' : token['tokenInfo']['symbol'], 'Balance' : token['balance'] * token['tokenInfo']['price']['rate'] / 10 ** (int(token['tokenInfo']['decimals']))}
            df = df.append(newRow, ignore_index=True)
    df.to_csv('FundAllocation.csv', index=False)
    
def FundAllocationInsula():
    sent = requests.get('https://api.ethplorer.io/getAddressInfo/0xCB60D600160D005845Ec999f64266D5608fd8943?apiKey=freekey').json()

    data = {'Symbol' : ['ETH'], 'Balance' : [sent['ETH']['balance'] * sent['ETH']['price']['rate']]}
    df = pd.DataFrame(data)

    tokens = sent['tokens']
    for token in tokens:
        if token['tokenInfo']['price'] != False:
            newRow = {'Symbol' : token['tokenInfo']['symbol'], 'Balance' : token['balance'] * token['tokenInfo']['price']['rate'] / 10 ** (int(token['tokenInfo']['decimals']))}
            df = df.append(newRow, ignore_index=True)
    df.to_csv('FundAllocationInusla.csv', index=False)

def main():
    FundAllocation()
    FundAllocationInsula()

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f = open("run_log.txt","a")
    f.write("Ran at " + dt_string + "\n")
    f.close() 

if __name__ == '__main__':
    main()
