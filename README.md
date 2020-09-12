# Scrapy_example_quotes
This code shows how to scrape quotes from a website and save them to an SQLite database.
It will serve as an example to adapt to other uses. 

./quotes_spider.py - Contains CSS selectors  
./pipelines.py - Creation & Connection to SQLite Database  
./myquotes.db - empty database into which the quotes table will be created and populated  
./test - Basic example of sqlite connection  
./test2 - Example of sqlite connection fed from array of seed data  

## Install Dependencies:
- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [Scrapy 2.3.0](https://docs.scrapy.org/en/latest/intro/install.html)

## To run crawler & populate database type

``` 
scrapy crawl quotes
```

## To output JSON file

```
scrapy crawl quotes -o items.json
```

* Can also do CSV

