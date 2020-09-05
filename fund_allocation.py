import requests
import pandas as pd
from datetime import datetime 
import json

def AnastasiaAllocation():
    sent = requests.get('https://api.ethplorer.io/getAddressInfo/0x9C49c053a8b9106024793516EE3c5562875A5C9a?apiKey=freekey').json()

    data = {'Symbol' : ['ETH'], 'Balance' : [sent['ETH']['balance'] * sent['ETH']['price']['rate']]}
    df = pd.DataFrame(data)

    tokens = sent['tokens']
    for token in tokens:
        if token['tokenInfo']['price'] != False:
            newRow = {'Symbol' : token['tokenInfo']['symbol'], 'Balance' : token['balance'] * token['tokenInfo']['price']['rate'] / 10 ** (int(token['tokenInfo']['decimals']))}
            df = df.append(newRow, ignore_index=True)
    df.to_csv('AnastasiaAllocation.csv', index=False)
    

def MaltaAllocation():
    sent = requests.get('https://api.ethplorer.io/getAddressInfo/0x0d9596Afc608B3322A17118A573750045F52C0B8?apiKey=freekey').json()

    data = {'Symbol' : ['ETH'], 'Balance' : [sent['ETH']['balance'] * sent['ETH']['price']['rate']]}
    df = pd.DataFrame(data)

    tokens = sent['tokens']
    for token in tokens:
        if token['tokenInfo']['price'] != False:
            newRow = {'Symbol' : token['tokenInfo']['symbol'], 'Balance' : token['balance'] * token['tokenInfo']['price']['rate'] / 10 ** (int(token['tokenInfo']['decimals']))}
            df = df.append(newRow, ignore_index=True)
    df.to_csv('MaltaAllocation.csv', index=False)
    
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
    AnastasiaAllocation()
    MaltaAllocation()
    ## FundAllocationInsula()

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f = open("run_log.txt","a")
    f.write("Ran at " + dt_string + "\n")
    f.close() 

if __name__ == '__main__':
    main()
