Stock Trading Robot

These robots are built to trade stocks live using Alpaca's stock trading API.
Moving Averages Robot

This robot monitors the market for buy and sell signals generated from the crossover of simple or exponential moving averages.

Upon execution of the code the user is asked to define:

    Ticker to trade
    Buying power or quantity of securities to use in trades
    Type of moving averages to monitor for buy/sell signals
        5, 8, 13 bar exponential moving average
        5, 8, 13 bar simple moving average
    Maximum number of trades to execute
        2 - one buy, one sell
        4 - two buys, two sells
        etc.

Momentum Robot

Currently in developement.
Breakout Strategy

    Look at past highs and generate buy signals as soon as price manages to break out from its previous high
    Use dynamic lookback ranges based on volatility
        When volatility is high, look further back
        When low, look less
    Open short-term long position and use stop loss

Gap and Go Strategy

    Looks for overnight gappers and bets on continuation of that move
    Open Short-term long/short trade and use stop loss

Earnings/News Strategy

    Look at the most well known/liquid stocks that had earnings in the past few days
    Focus on stocks that have an especially negative reaction from the market (-2%)
    Open medium-term long position and use stop loss
