My project is on the classification problem between days
where the price of the S&P 500 closes higher than the 
previous day and days where the price closes lower than 
the previous day.

Wasn’t much cleaning involved as it was clean financial
data from yahoo finance. Only pulled 3 columns from them
and ended up engineering ~20+. Closing date, closing price,
and volume. Only price is used and date to keep predictions
on in order and a rolling basis from one day to the next.

Majority classifier baseline varies by year but, in 
general, most days per year are up days (2018 most 
recent exception where it went the other way). The 
majority classifier accuracy is 54% up days to 46% down
days over the period between 1993 and 2019 (data that 
was available from Yahoo Finance). For 2019, assuming 
every day would be an up day would yield 58% accuracy 
because 58% of days days were up days (and there fore 
the majority classifier is 58% accurate). My model’s 
accuracy for the most recent 2019 RSI data yielded 63%
accuracy of up days vs down days. That would be considered
a significant edge given the ever growing reach for more
yield resulting from human greed.

Clearly, this model increases the probability of finding
days that will close higher the next day than just 
guessing the majority classifier. I ended up dropping 
every engineered column but one and running the model 
training based on 1 engineered feature: previous day’s 
RSI based on exponential moving average with a window 
of 7 trailing days.

A couple of features I will be implementing on the website
are the ability to change the window of the RSI and the 
ability to choose a specific day in the past (or even most
recent/prior day’s closing data) to run the model and on 
see what our prediction would have been which can be 
compared to the actual result. Predictions for the 
upcoming day are also possible using today’s closing 
data/RSI.
