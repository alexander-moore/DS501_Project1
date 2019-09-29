# yee haw
import pandas as pd
import statistics
from matplotlib import pyplot

data = pd.read_csv('data/yelp_dataset/user_data.csv', encoding = "ISO-8859-1")

print(data)

print(data.columns.values)

print(statistics.median(list(data['review_count'])))

low_count = data[data['review_count'] < 5]
high_count = data[data['review_count'] > 5]
one_count = data[data['review_count'] == 1]

print(low_count.shape)
print(high_count.shape)
print(one_count.shape)

high_ratings = high_count['average_stars']
low_ratings = low_count['average_stars']
one_rating = one_count['average_stars']

pyplot.hist(high_ratings, alpha = .5, label = 'more than 5 reviews')
pyplot.hist(low_ratings, alpha = .5, label = 'less than 5 reviews')
pyplot.hist(one_rating, alpha = .5, label = 'one rating')

pyplot.legend(loc = 'upper right')
pyplot.show()