"""
THIS FILE DEFINES A LOW-LEVEL SCRAPING FUNCTION WHICH IS USED REPEATEDLY

TEMPLATES CAN'T BE USED HERE, SINCE THIS DEFINES THE SPECIFIC SCRAPING ACTION WE WANT TO ACCOMPLISH

HAS TO RETURN SOMETHING (usually pd.DataFrame)
"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

# from update_checklist import update_checklist_table
from scraping_unique_to_this_proj import scrape_and_save

def update_checklist_table(checklist_path:str, 
                        #    checklist:pd.DataFrame,
                           scraped_bool_col:str,
                           URL_col:str,
                           URL_of_newly_scraped:str,
                           log_as_nan=False
                           ):
    
    checklist = pd.read_csv(checklist_path) # this slows the code down a bit but unless we're scraping 00000s of things should be okay

    # confirm that bools are numerical and not True, False
    unique_bools = checklist[scraped_bool_col].unique().tolist()
    assert len(set(unique_bools) - set([0, 1, np.nan])) == 0 # only contains 0, 1, or np.nan

    # set value to update
    if log_as_nan:
        pos_bool = np.nan
    else:
        pos_bool = 1

    # update value
    checklist.set_index(URL_col, 
                        inplace=True)
    checklist.loc[URL_of_newly_scraped, scraped_bool_col] = pos_bool

    # save/export
    checklist.to_csv(checklist_path,
                     index=True)


def scrape_and_update_checklist(checklist,
                                scraped_bool_col:str,
                                URL_col:str,
                                URL_to_scrape:str,
                                scraped_data_save_path:str,
                                checklist_path:str,
                                ):
    """This is the main fnc which scrapes the data *AND* updates the checklist"""

    log_as_nan = scrape_and_save(URL_to_scrape=URL_to_scrape,
                                 scraped_data_save_path=scraped_data_save_path)

    scrape_and_update_checklist(checklist=checklist,
                                checklist_path=checklist_path,
                                scraped_bool_col=scraped_bool_col,
                                URL_col=URL_col,
                                URL_of_newly_scraped=URL_to_scrape,
                                log_as_nan=log_as_nan
                                )

