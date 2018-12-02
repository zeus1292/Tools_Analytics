![alt text](https://static1.squarespace.com/static/565d55a7e4b0924c37da3b36/565f1f3fe4b02e4017e2c55a/565f20fce4b0db530927e504/1449075077804/logo_mahalo2rgb.jpg?format=110w)
## Contributors
Members: Akshay Kumar, Emilia Dwyer, Zhuo (Lily) Wang, Muskan Jain
<br />Section: 002
## Description
Mahalo is designed for publishers/writers looking for guidance on how to describe their book on Amazon to garner the most positive reviews. It is meant to be a preliminary tool to facilitate initial brainstorming sessions when constructing a new book’s landing page. The tool provides Word Clouds printed by category and topic for the best selling books. Categories and topics are generated from a [static dataframe provided by Kaggle](https://www.kaggle.com/ucffool/amazon-sales-rank-data-for-print-and-kindle-books) and a corresponding scrape of data by unique key,  ASIN. 

## Branch Setup
<ul>
  <li> <b> Master</b>: Contains FinalCode 
  <li> <b> Storage</b>: WordCloud images, batch files of Amazon scrape

## Run Instructions
You have a paramount decision to make that will define who you are as a human. You can either hit Ctrl+Enter or Shift+Enter to run code cells. Choose wisely. Good luck. Use 'Final Code' file on <b>master</b> branch.

<p>The following is a high level overview of how the code runs:
<ol>
<li> Read in download Kaggle df and instantiate a new file in your directory in the variable my_csvfile
<li>Run scraper for entirety of Kaggle df and save to new file to include amazon's data (note: the team ran in batches and merged all files in the end)
<li>Using processed csv clean df to prepare for analysis
<li> Produce WordCloudfor entire df
<li> Using cleaned data to present a plot of gamma distribution for 'Rating'
<li> To get a sense of data, produce a bargraph for top and bottom 15 publishers
<li> Finding the proportion of books in each category through a pie chart analysis
<li> In order to understand which price range has the highest rating, plotting a graph between category and the mean of user rating in each price range
<li>Topic Modeling for each category (df grouped by rating) {three topics per category} with a WordCloud representation
<li> Create LSI model from entire df
<li> Create LDA model from entire df to compute conditional probabilities for topic word set
</ol>

## Key Takeaways 

<u1>
  <li> abc
    <li> def
