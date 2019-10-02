# yee haw
import pandas as pd
import statistics
from matplotlib import pyplot
import seaborn
import numpy as np

data = pd.read_csv('data/user_data.csv', encoding = "ISO-8859-1")

print(data)

print(data.columns.values)

print(statistics.median(list(data['review_count'])))

reviews = data['average_stars']

low_count = data[data['review_count'] < 5]
high_count = data[data['review_count'] > 5]
one_count = data[data['review_count'] == 1]

print(low_count.shape)
print(high_count.shape)
print(one_count.shape)

high_ratings = high_count['average_stars']
low_ratings = low_count['average_stars']
one_rating = one_count['average_stars']
all_ratings = data['average_stars']


pyplot.hist(all_ratings, alpha = 1, label = 'Distribution of all reviews', color = 'lightsalmon')
pyplot.legend(loc = 'upper left')
pyplot.xlabel('Average Review')
pyplot.ylabel('Review Count')
pyplot.show()

pyplot.hist(high_ratings, alpha = 1, label = 'Accounts with more than 5 reviews')
pyplot.axis([1, 5, 0,300000])
pyplot.legend(loc = 'upper left')
pyplot.xlabel('Average Review')
pyplot.ylabel('Review Count')
pyplot.show()

pyplot.hist(high_ratings, alpha = 1, label = 'Accounts with more than 5 reviews')
pyplot.hist(low_ratings, alpha = 1, label = 'Accounts with less than 5 reviews')
pyplot.legend(loc = 'upper left')
pyplot.xlabel('Average Review')
pyplot.ylabel('Review Count')
pyplot.show()

pyplot.hist(high_ratings, alpha = 1, label = 'Accounts with more than 5 reviews')
pyplot.hist(low_ratings, alpha = 1, label = 'Accounts with less than 5 reviews')
pyplot.hist(one_rating, alpha = 1, label = 'Accounts with one review')
pyplot.legend(loc = 'upper left')
pyplot.xlabel('Average Review')
pyplot.ylabel('Review Count')
pyplot.show()



#trim_data = data[data['review_count'] < 50]

#count_vec = trim_data['review_count']
#score_vec = trim_data['average_stars']


#pyplot.scatter(count_vec, score_vec, alpha = .005)
#pyplot.show()

#df = data

#squish_data = data.copy()

# turn the high-count obs into 30-count
#squish_data['review_count'] = np.select(
#    [squish_data["review_count"] > 30], 
#    [30], 
#    squish_data["review_count"]
#)

#count_vec = squish_data['review_count']
#score_vec = squish_data['average_stars']

#round_score = [ round(elem) for elem in score_vec ]

#seaborn.set(style="whitegrid")
#seaborn.violinplot(x = round_score, y = count_vec)

#pyplot.show()