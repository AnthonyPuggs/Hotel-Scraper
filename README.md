# Hotel-Scraper
This is a Python script that scrapes various pieces of data about hotels from Booking.com search results.

By default, it scrapes all hotels listed in the city of Brisbane, Queensland, Australia. The script uses BeautifulSoup to scrape the data from the webpage, Requests to help make HTTP requests, and uses Pandas to neatly organise the data into a spreadsheet file.

The script gathers all information relating to the hotels on the search results, this includes:
Name, location, rating score, rating category, number of reviews, distance from city centre, travel sustainability, and the hotel description.

# Changing Location of Hotels to Scrape
If you wish to change the location from the default of Brisbane, replace with the 'main_link' and 'url' variables to a Booking.com search results URL of your choice. Also adjust the second value in the for loop range to the total properties found so it scrapes them all, this is on line 160. 

# Things to Note
Particularly when looking at hotels toward the end of all the listings, you will see many hotels with 'Nan' as they have no reviews yet. There will also be some with abnormal looking data compared to the rest of the hotels, such as noting 'external reviews' or having the rating score mixed in with the rating category. This is because these hotels have such little activity that Booking.com takes reviews from other places instead which messes with the continuity of the rest of their listings. This is not an issue with my script but with how they lay out their data. Although, this script could be updated further to account for this.

This script should work with most locations, some locations such as India list 'metro access' on their hotels. This data is not scraped from my script - but would be worth including in the future to account for other countries better.

# References
https://jovian.com/bhupeshchandrawanshi/web-scraping-project-scraping-hotel-list This was very helpful in making my script, this script is outdated and broken hence the motivation to make a new script. It also does not scrape 'travel sustainability' as this was only added in recent years.
