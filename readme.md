Scraping framework to use with a list of target URLs to scrape (the 'checklist' file) and a specific function to use on each URL.

Instructions:
1. Determine URLs you want to scrape. Create a dataframe of these URLs with each row containing (at least):
    * The URL.
    * A boolean column (0/1; not False/True) that records whether the row has been scraped yet.
        * Set all to 0 at first, unless you want to skip any rows for some reason.
    * An ID. Ideally this field has short elements, since they will become part of filepaths and there's a character limit.
2. Save this dataframe as 'checklist.csv' in the 'checklist' folder.
3. Modify 'code/Generalized Scraper.ipynb':
    * Configure the names of your dataframe's URL, bool, & ID columns in the 'CONFIG' code block.
    * Add the scraping function to the 'SCRAPING UNIQUE TO THIS PROJECT' code block, where a comment says 'scrape here ...'
4. Run, and make sure to abide by ethical scraping practices!
    * https://www.zyte.com/learn/web-scraping-best-practices/
    * https://en.wikipedia.org/wiki/Robots_exclusion_standard