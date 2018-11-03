
# coding: utf-8

# <h1>Amazon Dataset Processing</h1>

# <h3>1. Titles, links, ratings</h3>

# In[ ]:


import requests
from bs4 import BeautifulSoup

link_home = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books'
page = requests.get(link_home)
results_page = BeautifulSoup(page.content,'lxml')
all_links = results_page.find_all('li',class_='zg-item-immersion')

book_links = list()
book_titles = list()
book_ratings = list()
book_authors = list()
book_isbn10 = list()
book_isbn13 = list()
book_num_customer_reviews = list()
book_format = list()
book_prices = list()
book_category1 = list()
book_category2 = list()
book_description = list()

for i in all_links:
    m = 'https://www.amazon.com%s' %(i.find('a', class_='a-link-normal').get('href'))
    book_links.append(m)
    
for i in all_links:
    m = i.find('div',class_='p13n-sc-truncate p13n-sc-line-clamp-1').get_text()
    m = m.replace('\n','')
    m = m.strip()
    book_titles.append(m)

for i in all_links:
    m = i.find_all('a',class_='a-link-normal')[1].get_text()
    if '$' in m:
        book_ratings.append('No Rating')
    else:
        m = m.replace('\n','')
        m = m.strip()
        m = m[:3]
        book_ratings.append(m)


# <h3>2. Author, ISBN-10, ISBN-13, platform, price, category1, category2, description</h3>

# In[ ]:


def get_aiipp(link):
    """Returns lists of Author, ISBN-10, ISBN-13, platform, price, category1, category2, description for book"""
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(url)
    results_page = BeautifulSoup(page.content,'lxml')

    m = results_page.find('a', class_='a-link-normal contributorNameID').get_text()
    book_authors.append(m)
    n = results_page.find('div', class_='content').find_all('li')[5].get_text().replace('ISBN-10:','').strip()
    book_isbn10.append(n)
    p = results_page.find('div', class_='content').find_all('li')[6].get_text().replace('ISBN-13:','').strip()
    book_isbn13.append(p)
    q = int(results_page.find('span',class_='a-size-base').get_text().replace('customer reviews','').strip())
    book_num_customer_reviews.append(q)
    r = results_page.find('span',class_='a-button-selected a-spacing-mini a-button-toggle-format').find('a').find('span').get_text()
    book_format.append(r)
    s = float(results_page.find('span',class_='a-size-base a-color-price a-color-price').get_text()[1:])
    book_prices.append(s)
    t = results_page.find('div',class_='a-subheader a-breadcrumb feature').find_all('li')[2].find('a',class_='a-link-normal a-color-tertiary').get_text().replace('\n','').strip()
    book_category1.append(t)
    u = results_page.find('div',class_='a-subheader a-breadcrumb feature').find_all('li')[4].find('a',class_='a-link-normal a-color-tertiary').get_text().replace('\n','').strip()
    book_category2.append(u)
    
    v = # Need to figure out how to click 'read more', then add all text pieces into one string
    book_description.append(v)
    
    
    


# In[ ]:


for i in book_links:
    get_aiipp(i)


# <h1>Kaggle Dataset Processing</h1>

# <h1><font color='red'>IMPORTANT: </font color='red'></h1><h2>Run the following to convert .ipynb to .py before pushing to GIT</h2>

# In[ ]:


get_ipython().system('jupyter nbconvert --to script AZscraping.ipynb')

