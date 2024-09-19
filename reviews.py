# add your code here
import pandas as pd
import zipfile
import os

#reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)
#pd.set_option("display.max_rows", 5)
#reviews_written = reviews.groupby('taster_twitter_handle').size()
#best_rating_per_price = reviews.groupby('price').points.max()
#price_extremes = pd.DataFrame({'min':reviews.groupby('variety').price.min(),'max':reviews.groupby('variety').price.max()})
#sorted_varieties = price_extremes.sort_values(by=['min','max'], ascending = False)
#reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
#print(reviews)

#reviews

# Load the dataset
reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Check the first few rows to understand the structure of the data
#print(reviews.head())

# Group by 'country' and calculate the count and average of 'points'
country_summary = reviews.groupby('country').agg(count=('points', 'size'), points=('points', 'mean')).reset_index()

# Sort the summary by the count in descending order
country_summary = country_summary.sort_values(by='count', ascending=False)

# Format the points to 1 decimal place
country_summary['points'] = country_summary['points'].round(1)

# Display the final summary
#print(country_summary)
#reviews
country_summary.to_csv('reviews-per-country.csv')





