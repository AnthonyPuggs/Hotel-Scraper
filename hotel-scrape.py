from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import matplotlib.pyplot as plt

#Load the sample csv file
sample_df = pd.read_csv('hotel-sample.csv')

(sample_df)

main_link = "https://www.booking.com/searchresults.en-gb.html?flex_window=0&search_selected=true&src_elem=sb&checkout_month=&checkin_month=&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaA-IAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AuCp65wGwAIB0gIkM2YxNzJkMzktN2FjMS00M2EyLWI0ODgtYmU3OWUwNzI5Mjlm2AIG4AIB%26sid%3Daff587ca08b00a9eef94ee00cde4e278%26sb_price_type%3Dtotal%26%26&ss=Brisbane%2C+Australia&aid=304142&is_ski_area=&sb=1&sb_lp=1&sid=aff587ca08b00a9eef94ee00cde4e278&efdco=1&order=bayesian_review_score&dest_id=-1561728&label=gen173nr-1FCAEoggI46AdIM1gEaA-IAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AuCp65wGwAIB0gIkM2YxNzJkMzktN2FjMS00M2EyLWI0ODgtYmU3OWUwNzI5Mjlm2AIG4AIB&checkin_year=&group_adults=2&from_sf=1&search_pageview_id=aec838b0e94901d2&no_rooms=1&checkout_year=&dest_type=city&b_h4u_keep_filters=&group_children=0&offset=0"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

#Request for the URL
page = requests.get(main_link, headers=headers)

#We can also check the response code
print(page.status_code)

#Make it a soup
soup = BeautifulSoup(page.text,"lxml")

#Display Soup (Main Page)
print(soup)

url = "https://www.booking.com/searchresults.en-gb.html?flex_window=0&search_selected=true&src_elem=sb&checkout_month=&checkin_month=&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaA-IAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AuCp65wGwAIB0gIkM2YxNzJkMzktN2FjMS00M2EyLWI0ODgtYmU3OWUwNzI5Mjlm2AIG4AIB%26sid%3Daff587ca08b00a9eef94ee00cde4e278%26sb_price_type%3Dtotal%26%26&ss=Brisbane%2C+Australia&aid=304142&is_ski_area=&sb=1&sb_lp=1&sid=aff587ca08b00a9eef94ee00cde4e278&efdco=1&order=bayesian_review_score&dest_id=-1561728&label=gen173nr-1FCAEoggI46AdIM1gEaA-IAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AuCp65wGwAIB0gIkM2YxNzJkMzktN2FjMS00M2EyLWI0ODgtYmU3OWUwNzI5Mjlm2AIG4AIB&checkin_year=&group_adults=2&from_sf=1&search_pageview_id=aec838b0e94901d2&no_rooms=1&checkout_year=&dest_type=city&b_h4u_keep_filters=&group_children=0&offset={}"

#We need to add query number

def get_page(url,head,num):
	"""
	Function takes url as parameter and returns the soup.
	`url` : Link in strings
	'num' : For different pages (1-40)
	'head' : header for the url
	"""
	page = requests.get(url.format(num),headers=head)
	if page.status_code != 200:
		raise Exception('Failed to load page {}'.format(url))
	soup = BeautifulSoup(page.text, "lxml")
	return soup

blocks = soup.select(".a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942")
print(len(blocks))

#For first block
print(blocks[0])

# Select the First Section
section = soup.select(".a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942")[0]

# Select the second anchor tag
anchor = section.select("a")[1] 

# Select the first span (now div) tag
div = anchor.select("div")[0]

# Get the name of hotel
name = div.getText().split('\n')[0]

print(name)

def get_hotel_name(section):
	"""
	Function gives us the hotel name
	"""
	name = section.select(".fcab3ed991.a23c043802")[0].getText()
	return name

# Location
place = section.select(".f4bd0794db.b4273d69aa")[0].getText()

def get_location(section):
	"""
	Function gives us the location info
	"""
	place = section.select(".f4bd0794db.b4273d69aa")[0].getText()
	return place

# Check for the fourth anchor tag
rating = section.select(".b5cd09854e.d10a6220b4")[0].getText() 
category = section.select(".b5cd09854e.f0d4d6a2f5.e46e88563a")[0].getText()
count = section.select(".d8eab2cf7f.c90c0a70d3.db63693c62")[0].getText()

review_data = []
review_data.extend([rating, category, count])
print(review_data)

print(rating)
print(category)
print(count)


def get_review_details(section):
	"""
	Function gives us the Review Rating, Review Category and Review Count
	"""
	try:
		rating = section.select(".b5cd09854e.d10a6220b4")[0].getText() 
	except:
		rating = 'Nan'

	try:
		category = section.select(".b5cd09854e.f0d4d6a2f5.e46e88563a")[0].getText()
	except:
		category = 'Nan'

	try:
		count = section.select(".d8eab2cf7f.c90c0a70d3.db63693c62")[0].getText()
	except:
		count = 'Nan'

	return rating,category,count

review_details = get_review_details(section)

# New class for the Distance and Travel Sustainability Info
distance = section.select(".cb5ebe3ffb")[3].getText()
print(distance)

# Metro Info
#metro = section.select(".a51f4b5adb")[0].getText()
#print(metro)

def get_distance_info(section):
	"""
	Function returns the distance information
	"""
	# For the centre distance
	exclude_words = ['Show', 'prices', 'reviews', 'Travel', ' Level']

	elements = section.find_all(class_='cb5ebe3ffb')

	relevant_text = []

	for element in elements:
		element_text = element.getText()

		if not any(word in element_text for word in exclude_words):
			distance = element_text

	# For Travel Sustainability - for some reason each time the page is loaded a different class for travel sustainaility is used, so I had to check for both
	try:
		travelsust = section.select(".d8eab2cf7f.be09c104ad")[0]
		travelsust = 'Travel Sustainable'
	except:
			try:
				travelsust = section.select(".a51f4b5adb")[0]
				travelsust = 'Travel Sustainable'
			except: 
				travelsust = 'Not Travel Sustainable'
	else: travelsust = 'Travel Sustainable'
	return distance, travelsust

distance_info = get_distance_info(section)
print(distance_info)

#Class for hotel description
hotel_desc = section.select(".d8eab2cf7f")[1].getText()
print(hotel_desc)

def get_description(section):
	"""
	Function returns hotel description if any
	"""
	exclude_words = [' reviews', ' review', 'Booking.com']

	elements = section.find_all(class_="d8eab2cf7f")

	relevant_text = []

	for element in elements:
		element_text = element.getText()

		if not any(word in element_text for word in exclude_words):
			hotel_desc = element_text
	return hotel_desc

description = get_description(section)
print(description)

# Make Dictionary

def new_data_dict():
	"""
	Function return new directory
	"""

	new_dict = {
	"Name" : [],
	"Place" : [],
	"Rating Point" : [],
	"Rating Category" : [],
	"Number of Reviews" : [],
	"Distance from Centre" : [],
		"Travel Sustainability" : [],
	"Description" : [] }

	return new_dict

# Creating empty dictionary for storing
scrape_dict = new_data_dict()

# Looping through all the content from 0-1000
for num in range(0, 535, 25):

	# Request for the URL and make soup
	soup = get_page(url,headers,num)

	#Get the sections
	sections = soup.select(".a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942")

	# For all the blocks
	for section in sections:

		# Get and add the details to dictionary
		scrape_dict["Name"].append(get_hotel_name(section))
		scrape_dict["Place"].append(get_location(section))
		part1,part2,part3 = get_review_details(section)
		scrape_dict["Rating Point"].append(part1)
		scrape_dict["Rating Category"].append(part2)
		scrape_dict["Number of Reviews"].append(part3)
		info1,info2 = get_distance_info(section)
		scrape_dict["Distance from Centre"].append(info1)
		scrape_dict["Travel Sustainability"].append(info2)
		scrape_dict["Description"].append(get_description(section))

# Saving the data to a dataframe
df = pd.DataFrame(scrape_dict)

# Check the length of the dataframe
print(df[:50])

# To save the data frame
df.to_csv("hotel-list.csv")
