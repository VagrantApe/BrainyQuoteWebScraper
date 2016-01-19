# Brainy Quotes WebScraper

I was looking to pull quotes from famous people and wasn't having much luck.  
This is a quick and dirty fix to that in python using Beautiful Soup.
It will make a json file called *quotes.json* that uses the page as key and the values as an array of quotes.

Usage
```$ BrainyQuotesWebScraper.py mike_tyson 3```

The first argument is the authors first name and last name  seperated by an underscore and the second argument is the number of pages of quotes you want pulled in, approx 26 per page.

