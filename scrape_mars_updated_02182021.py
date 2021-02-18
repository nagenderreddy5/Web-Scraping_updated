# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup 
import requests
import pymongo


# %%
#executable_path = {'executable_path': ChromeDriverManager().install()}
executable_path = {'executable_path': 'C:\\Users\\nagen\\OneDrive\\Documents\\GitHub\\GT-ATL-DATA-PT-09-2020-U-C-2\\GT-ATL-DATA-PT-09-2020-U-C-2\\12-Web-Scraping-and-Document-Databases\\Homework\\Resources\\chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# NASA Mars News (Most recent article)


#visit the website
url1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url1)

#parse HTML
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#step through HTML to find news title
step1 = soup.find('ul', class_='item_list')
step2 = step1.find('li', class_='slide')
step3 = step2.find('div', class_='content_title')
title = step3.text

#continue step to find paragraph
step4 = step2.find('div', class_='article_teaser_body')
paragraph = step4.text


# %%
#check returns
title


# %%
paragraph


# %%
# JPL Mars Space Image (Featured)

#visit the website
url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)

#Scrape the page into BeautifulSoup
html = browser.html
soup = BeautifulSoup(html, "html.parser")

soup


# %%
print(soup.prettify())


# %%
links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]
links_with_text


# %%
soup.find_all('a')


# %%
soup.find_all('div')


# %%
# direct links for the NASA images
for link in soup.find_all('img'):
    print(link.get('data-src'))


# %%
# JPL Mars Space 2nd Image to be scraped (Featured)

#visit the website
url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)

#Scrape the page into BeautifulSoup
html = browser.html
soup = BeautifulSoup(html, "html.parser")

soup


# %%
images = soup.findAll('img')
# example = images[1]
images


# %%
src=images[0]['src']
src


# %%
base_url= 'https://www.jpl.nasa.gov'
combined_url = base_url+src
combined_url


# %%
html = browser.html
soup = BeautifulSoup(html, "html.parser")

src = soup.find('img').get('src')
src


# %%
#Combine main website to image for full URL
base_url = 'https://www.jpl.nasa.gov'
featured_image_url2 = base_url + src
featured_image_url2

# %% [markdown]
# Mars Facts
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.

# %%
#executable_path = {'executable_path': ChromeDriverManager().install()}
executable_path = {'executable_path': 'C:\\Users\\nagen\\OneDrive\\Documents\\GitHub\\GT-ATL-DATA-PT-09-2020-U-C-2\\GT-ATL-DATA-PT-09-2020-U-C-2\\12-Web-Scraping-and-Document-Databases\\Homework\\Resources\\chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# URL of webpage to be scraped
url3 = 'https://space-facts.com/mars/'
browser.visit(url3)


# %%

#Read table data into Pandas
mars_table_facts = pd.read_html(url3)


mars_table_facts


# %%
#Return results as a dataframe
mars_df = mars_table_facts[1]
#mars_df.head()
mars_df.columns=['Index', 'Description', 'value']
mars_df


# %%
# Use Pandas to convert the data to a HTML table string.
facts_df_html = mars_df.to_html(classes='')
print(facts_df_html)

# %% [markdown]
# Mars Hemispheres

# %%
#setup the browser
executable_path = {'executable_path': 'C:\\Users\\nagen\\OneDrive\\Documents\\GitHub\\GT-ATL-DATA-PT-09-2020-U-C-2\\GT-ATL-DATA-PT-09-2020-U-C-2\\12-Web-Scraping-and-Document-Databases\\Homework\\Resources\\chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# Mars Hemispheres (images)
#visit the website
url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url4)

#Scrape the page into BeautifulSoup
html = browser.html
soup = BeautifulSoup(html, "html.parser")

# Locate information for all four Hemisphere 
hemispheres_results = soup.find_all('div', class_='item')


# %%
# Creating a list to hold Mars Hemispheres url
hemispheres_image_urls = []
url_hemispheres_main = 'https://astrogeology.usgs.gov'

# Retrieve the titles for hemispheres
for hem_url in hemispheres_results:
    hemispheres_title = hem_url.find('h3').text
    hemispheres_title = hemispheres_title.replace(" Enhanced","")

# Retrieve partial url for hemispheres image
    
    hemispheres_image = hem_url.find('a', class_='itemLink product-item')['href']
    browser.visit(url_hemispheres_main + hemispheres_image)
    
    hemispheres_image_html = browser.html
    hemispheres_soup = BeautifulSoup(hemispheres_image_html, 'html.parser')

# Merge hemispheres main URL & hemispheres image partial URLs
    
    hemispheres_image_url = url_hemispheres_main + hemispheres_soup.find('img', class_='wide-image')['src']
    
# Append merged URLs into list
    hemispheres_image_urls.append({"title": hemispheres_title, "img_url": hemispheres_image_url})

# Display results
hemispheres_image_urls


# %%



# %%



# %%



