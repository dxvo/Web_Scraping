
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
from splinter import Browser


# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#browse nasa site 
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order="            "publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)


# In[8]:


#Create bs object
html = browser.html
soup = bs(html,"html.parser")


# ## Nasa Mars News

# In[9]:


#Scapping 
news_title = soup.find("div", class_="content_title").text
news_p = soup.find("div", class_="article_teaser_body").text
print(f"Latest News Title: {news_title}\n")
print(f"Paragraph text: {news_p}")


# ## JPL Feature Image

# In[17]:


#Visit the image site and create 
image_page = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_page)


# In[18]:


#creat soup object 
img_html = browser.html
soup = bs(img_html, 'html.parser')
browser.click_link_by_partial_text('FULL IMAGE')


# In[20]:


#getting image url
img_html = browser.html
soup_img = bs(img_html, "html.parser")
img_url = soup_img.find("img", class_="fancybox-image")
feature_img_url = "https://jpl.nasa.gov" + img_url["src"]
print(feature_img_url)


# ## Mars Weather

# In[21]:


#browse twitter page 
weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(weather_url)


# In[44]:


#get data 
weather_html = browser.html
weather_soup = bs(weather_html, "html.parser")

mars_weather = weather_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# ## Mars Facts

# In[57]:


import pandas as pd
facts_url = "https://space-facts.com/mars/"
table = pd.read_html(facts_url)
mars_profile = table[0]
mars_profile


# In[63]:


#Rename columns 
mars_profile.columns = ["Variable Type", "Value"]
mars_profile.set_index(["Variable Type"], inplace=True)
mars_profile


# In[65]:


#Convert DataFrame to html
mars_html_profile = mars_profile.to_html()
mars_html_profile = mars_html_profile.replace("\n", "")
mars_html_profile


# ## Mars Hemispheres
# 

# In[66]:


hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hem_url)


# In[67]:


import time


# In[71]:


hem_html = browser.html
hem_soup = bs(html, 'html.parser')
mars_image_url_list=[]

for i in range (4):
    time.sleep(2)
    img = browser.find_by_tag('h3')
    img[i].click()
    new_html = browser.html
    new_soup = bs(new_html, 'html.parser')
    
    img_url = new_soup.find("img", class_="wide-image")["src"]
    img_title = new_soup.find("h2",class_="title").text
    img_url = "https://astrogeology.usgs.gov" + img_url
    
    img_details = {"title":img_title,"img_url":img_url}
    mars_image_url_list.append(img_details)
    browser.back()
    
print(mars_image_url_list)

