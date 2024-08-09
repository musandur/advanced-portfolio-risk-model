
import pandas as pd
import warnings

idx = pd.IndexSlice
warnings.filterwarnings('ignore')

def select_and_process_historical_data(filename, traded_year=8, number_stocks=10):
    '''
    filename: is the csv file name that contains the historical trading data to be processed and used to construct the portfolio
                
            We select the ten most traded asset in ten years in terms of average market cap.
                
    '''

    data = pd.read_csv(filename, 
                       index_col=[0,1], 
                       parse_dates=True)

    
    # filter the dataframe by selecting the adjencent prices and select 10 years of trading data
    data = data.filter(like='adj_').rename(columns=lambda x: x.replace('adj_', '')).loc[idx[:, '2006':'2016'], :].dropna()
    
    # select the assets: we select the 10 most traded assets over the 10 years in terms of market cap
    dv = data.close.mul(data.volume)
    dv = dv.unstack('ticker').dropna(thresh=traded_year*252, axis=1).rank(axis=1, ascending=True).mean().nlargest(number_stocks)
    selected_assets = dv.index.tolist()
    universe = data.loc[idx[selected_assets, :], :]
    
    # remove data outlier by removing returns that are at least 100 per cent
    universe = universe[universe.close.pct_change().between(-1, 1)]
    
    
    
    return universe

if __name__ == "__main__":
    filename = 'HISTORIC_PRICES.csv'
    select_and_process_historical_data(filename)