
# coding: utf-8

# <h1>Amazon Dataset Processing</h1>

# <h3>1. Function to return: Author, ISBN-10, ISBN-13, platform, price, category1, category2, description</h3>

# In[ ]:


def get_aiipp(link):
    """Returns lists of Author, ISBN-10, ISBN-13, platform, price, category1, category2, description for book"""
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(link)
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
    
    #v = # Need to figure out how to click 'read more', then add all text pieces into one string
    #book_description.append(v)
    
    from time import sleep
    sleep(20)
    


# <h3>2. Titles, links, ratings</h3>

# In[ ]:


import requests
from bs4 import BeautifulSoup
from time import sleep

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


# In[ ]:


for i in book_links:
    get_aiipp(i)


# <h3>3. Zip all elements together & create pd.df</h3>

# In[ ]:


zip_az = list(zip(book_isbn13,book_isbn10,book_titles,book_authors,book_ratings,book_prices,book_format,book_category1,
         book_category2,book_num_customer_reviews,book_links,book_description))
labels = ['ISBN-13','ISBN-10','title','author','rating','price',
                 'format','category1','category2','num_reviews','link','description']
df_az = pd.DataFrame.from_records(zip_az,columns=labels)


# <h3>4. Rename ISBN-13 to ASIN for future merge</h3>

# In[ ]:


df_az.rename(columns={'ISBN-13':'ASIN'})


# <h1>Kaggle Dataset Processing</h1>

# <h4><font color='red'>Note:</font color='red'> you will need to change the path to your directory when you want to run/edit</h4>

# <h3>1. File import</h3>

# In[ ]:


import pandas as pd
path_kaggle = r'C:\Users\endwy\Documents\Columbia MSBA\Fall 2018\E4501 - Tools for Analytics\Project\kaggle data\amazon_com_extras.csv'

with open(path_kaggle):
    df_kaggle = pd.read_csv(path_kaggle, encoding='latin1', dtype=str)


# <h3>2. Remove "spill over" unnamed rows from df</h3>

# In[ ]:


cols_unnamed = ['Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9',
                'Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14']
for i in cols_unnamed:
    for index, row in df_kaggle.iterrows():
        if df_kaggle.loc[index,[str(i)]].isnull().any()==False:
                df_kaggle.drop([index],inplace=True)
df_kaggle.drop(['Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9',
                'Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14'], axis=1, inplace=True)


# <h3>3. Merge Amazon scrape andKkaggle dfs</h3>

# In[ ]:


merge = pd.merge(df_az,df_kaggle, on='ASIN',how='left')


# <h3>##. Save out</h3>

# In[ ]:


merge.to_csv('C:\Users\endwy\Documents\Columbia MSBA\Fall 2018\E4501 - Tools for Analytics\Project\kaggle data\processed.csv', index=False)


# <h1><font color='red'>IMPORTANT: </font color='red'></h1><h2>Run the following to convert .ipynb to .py before pushing to GIT</h2>

# In[ ]:


get_ipython().system('jupyter nbconvert --to script AZscraping.ipynb')

