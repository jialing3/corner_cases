import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def reorder_tabulated_df(selected, df):
    df.index = df.index.droplevel()
    return df.reindex(selected)

def variance_at_return(returns_annual, cov_annual, weights):
    returns = np.dot(weights, returns_annual)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
    sharpe = returns / volatility
    return returns, volatility, sharpe

def returns_and_covariance(data, selected):
    # reorganize data pulled by setting date as index with
    # columns of tickers and their corresponding adjusted prices
    data = data[['date', 'ticker', 'adj_close']]
    clean = data.set_index('date')
    table = clean.pivot(columns='ticker')

    # calculate daily and annual returns of the stocks
    returns_daily = table.pct_change()
    returns_annual = returns_daily.mean() * 250
    returns_annual = reorder_tabulated_df(selected, returns_annual)

    # get daily and covariance of returns of the stock
    cov_daily = returns_daily.cov()
    cov_annual = cov_daily * 250
    cov_annual = reorder_tabulated_df(selected, cov_annual)

    return returns_annual, cov_annual

def generate_random_weights(num_assets):
    weights = [0 for stock in range(num_assets)]
    for ind in range(num_assets):
        weights[ind] = np.random.random() * (1 - sum(weights))
    weights = np.array(weights)
    np.random.shuffle(weights)
    weights /= np.sum(weights)
    return weights

def get_pure_weights(num_assets):
    pure_weights = []
    for ind in range(num_assets):
        weights = [0.0 for stock in selected]
        weights[ind] = 1.0
        pure_weights.append(weights)
    return pure_weights

def optimize_portfolio(data, selected, num_portfolios=5000):
    returns_annual, cov_annual = returns_and_covariance(data, selected)

    # empty lists to store returns, volatility and weights of imiginary portfolios
    port_returns = []
    port_volatility = []
    sharpe_ratio = []
    stock_weights = []
    port_label = []

    # set the number of combinations for imaginary portfolios
    num_assets = len(selected)
    num_portfolios = num_portfolios

    #set random seed for reproduction's sake
    np.random.seed(101)

    # populate the empty lists with each portfolios returns, risk and weights from random weights
    for single_portfolio in range(num_portfolios):
        weights = generate_random_weights(num_assets)
        returns, volatility, sharpe = variance_at_return(returns_annual, cov_annual, weights)
        sharpe_ratio.append(sharpe)
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)
        port_label.append('Random')

    # add customized portfolios
    pure_weights = get_pure_weights(num_assets)
    customized_weights = [0.38, 0.2, 0.2, 0.2, 0.02]
    weights_lst = pure_weights + [customized_weights]
    label_lst = selected + ['Customized']
    for weights, label in zip(weights_lst, label_lst):
        returns, volatility, sharpe = variance_at_return(returns_annual, cov_annual, np.array(weights))
        sharpe_ratio.append(sharpe)
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)
        port_label.append(label)

    # a dictionary for Returns and Risk values of each portfolio
    portfolio = {'Returns': port_returns,
                'Volatility': port_volatility,
                'Sharpe Ratio': sharpe_ratio,
                'Portfolio Label': port_label}

    # extend original dictionary to accomodate each ticker and weight in the portfolio
    for counter, symbol in enumerate(selected):
        portfolio[symbol + ' Weight'] = [weight[counter] for weight in stock_weights]

    # make a nice dataframe of the extended dictionary
    df = pd.DataFrame(portfolio)

    # get better labels for desired arrangement of columns
    column_order = ['Returns', 'Volatility', 'Sharpe Ratio', 'Portfolio Label'] + [stock + ' Weight' for stock in selected]

    # reorder dataframe columns
    df = df[column_order]

    # find min Volatility & max sharpe values in the dataframe (df)
    min_volatility = df['Volatility'].min()
    max_sharpe = df['Sharpe Ratio'].max()

    # change the portfolio labels for min Volatility & max sharpe values
    df.at[df['Sharpe Ratio']==max_sharpe, 'Portfolio Label'] = 'Max Sharpe Ratio'
    df.at[df['Volatility']==min_volatility, 'Portfolio Label'] = 'Min Volatility'

    # find portfolios on the efficient frontier at the volatility / returns level of Customized
    customized_returns = df.loc[df['Portfolio Label']=='Customized', 'Returns'].values[0]
    customized_volatility = df.loc[df['Portfolio Label']=='Customized', 'Volatility'].values[0]

    max_return_port_at_customized_volatility = df.loc[(df['Returns']>=customized_returns) & (df['Volatility']<=customized_volatility), 'Returns'].max()
    min_volatility_port_at_customized_returns = df.loc[(df['Returns']>=customized_returns) & (df['Volatility']<=customized_volatility), 'Volatility'].min()

    df.at[df['Returns']==max_return_port_at_customized_volatility, 'Portfolio Label'] = 'Max Return Portfolio At Customized Volatility'
    df.at[df['Volatility']==min_volatility_port_at_customized_returns, 'Portfolio Label'] = 'Min Volatility Portfolio At Customized Returns'

    # print customized portfolios
    print(df.loc[df['Portfolio Label'] != 'Random'])


    # allow Chinese characters to appear in plots (so my parents can understand this more easily)
    from matplotlib import font_manager

    fontP = font_manager.FontProperties()
    fontP.set_family('SimHei')
    fontP.set_size(14)

    # plot frontier, max sharpe & min Volatility values with a scatterplot
    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    # plot non-random portfolios
    colors = ['orange', 'cyan', 'dodgerblue', 'blanchedalmond', 'silver', 'palegreen', 'darkslateblue', 'tomato', 'khaki', 'crimson']
    markers = ['D', 'D', '^', '^', 'o', 'o', 'o', 'o', 'o', 'o']
    for ind, port in df.loc[df['Portfolio Label'] != 'Random'].reset_index().iterrows():
        plt.scatter(x=port['Volatility'], y=port['Returns'], c=colors[ind], marker=markers[ind], s=200, label=port['Portfolio Label'], alpha=0.8)
    plt.xlabel('Volatility (Std. Deviation) 风险', fontproperties=fontP)
    plt.ylabel('Expected Returns 收益', fontproperties=fontP)
    plt.title('Efficient Frontier 效率前沿', fontproperties=fontP)
    plt.legend()
    plt.show()


# get adjusted closing prices of 5 selected companies with Quandl
#quandl.ApiConfig.api_key = ''
#selected = ['CNP', 'F', 'WMT', 'GE', 'TSLA']
#data = quandl.get_table('WIKI/PRICES', ticker = selected,
#                        qopts = {'columns': ['date', 'ticker', 'adj_close']},
#                        date = {'gte': '2014-1-1', 'lte': '2017-12-01'},
#                        paginate=True)
selected = ['IVV', 'FCNTX', 'FSMEX', 'FTEC', 'FNCL']
data = pd.DataFrame()
for symbol in selected:
    tmp = pd.read_csv('~/Downloads/' + symbol + '.csv')
    tmp = tmp[['Date', 'Adj Close']]
    tmp['ticker'] = symbol
    data = pd.concat([data, tmp])
data.columns = list(map(lambda x: '_'.join(x.lower().split()), data.columns))
optimize_portfolio(data, selected, 5000)
