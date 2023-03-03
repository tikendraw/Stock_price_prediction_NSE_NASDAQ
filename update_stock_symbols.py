

import pandas as pd
import os 
from pathlib import Path

def get_stock_symbols():
    '''
    get stock symbols from NASDAQ and Indian Stock Market

    '''
    
    try:
        # getting the stock symbols of Indian Companies
        print('Getting stock symbols...')
        indian_stock_symbols = pd.read_html('https://indiancompanies.in/listed-companies-in-nse-with-symbol/')[0]

        #making first row as header /column names
        indian_stock_symbols.columns = indian_stock_symbols.iloc[0]
        indian_stock_symbols = indian_stock_symbols[1:]

        #Saving file
        indian_stock_symbols.to_csv('indian_stock_symbols.csv')

        # Nasdaq requires manual downloaing
        ## nasdaq_url = 'https://www.nasdaq.com/market-activity/stocks/screener'

        # Moving csv to src folder
        scr_folder = Path.cwd() / 'src'
        try:
            scr_folder.mkdir(exist_ok=True)
        except:
            pass
            
        os.system('mv -f indian_stock_symbols.csv src/indian_stock_symbols.csv ')
        print('Updated.')

    except Exception as e:
        print(' shit!!!', e )
        
if __name__=='__main__':
    print('Doing Something...')














def main():
	...

if __name__=="__main__":
	
	main()
