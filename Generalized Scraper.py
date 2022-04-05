# %% [markdown]
# # OUTLINE

# %% [markdown]
# 1. Find list of items (checklist) we want scraped in the same way (include URLS and IDs (IDs can just be URL)). Finding this checklist is outside of the scope of this file/scraper. 
# 2. For each item X we want to scrape:
#     * Run scraping function on X (and store scrape of X in folder)
#         * scraper.py
#     * Update checklist to reflect that X has been scraped (and save updated version of checklist)
#         * update_checklist.py
# 
# 

# %% [markdown]
# # CONFIG

# %%
CHECKLIST_REL_PATH = ...
SCRAPED_DATA_FOLDER_REL_PATH = ...

CHECKLIST_COL_NAMES=dict(
    ID=...,
    URL=...,
    SCRAPED_BOOL=...,
)

# %% [markdown]
# # IMPORT PACKAGES

# %%
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

import time

# %% [markdown]
# # IMPORT FUNCTION(S)

# %%
from scraper_fncs.scraper import scrape_and_update_checklist

# %% [markdown]
# # RUN

# %%
def main():
    checklist = pd.read_csv(CHECKLIST_REL_PATH)
    for url_to_scrape in checklist.query(f'{CHECKLIST_COL_NAMES["SCRAPED_BOOL"]}==1')[CHECKLIST_COL_NAMES['URL']]:
        scrape_and_update_checklist(checklist=checklist,
                                    scraped_bool_col=CHECKLIST_COL_NAMES['SCRAPED_BOOL'],
                                    URL_col=CHECKLIST_COL_NAMES['ID'],
                                    URL_to_scrape=url_to_scrape,
                                    scraped_data_save_path=SCRAPED_DATA_FOLDER_REL_PATH)


if __name__ == "__main__":
    main()


