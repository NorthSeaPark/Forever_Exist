# CAPM 策略

1. Get the historical price of Dow 30 stocks in the past 21 trading days and calculate their daily rates of return.
2. Conduct simple linear regression on the return of each stock against a benchmark (S&P 500 index, SPY).
3. Rank the stocks by their intercepts.
4. Liquidate all our positions and purchase the first 2 stocks in our sorted list.

We have demonstrated that during a smooth market, the stocks that beat the market last month are likely to beat the market again in the subsequent month. When there is market fluctuation, the significance level of linear regression will reduce and the model performance will decrease. We can understand this by looking at the covariance of the **asset(x)** and the **benchmark (y)**. As the covariance reduces to zero, the beta will decrease.

β(hat) = Cov[x,y]  / ∑(xi−βx)^2

Improvement:

- Conduct optimizations: we can implement mean-variance analysis to determine the asset allocation each month and select more stocks to trade. This will lower our risk and manage the portfolio more scientifically.
- Take beta into consideration: If we want to be more aggressive, we can select targets by a combination of alpha and beta. This means we choose stocks with a high alpha that are more volatile than the market. If we are conservative investors however, we can make the strategy market-neutral, which means the portfolio would not be affected by the market performance. For example, if we long two stocks with beta 1 and -1 respectively at the same position size, our portfolio becomes market-neutral.

