import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

def scrape_and_save(URL_to_scrape:str,
                    scraped_data_save_path:str) -> int: 
    """
    This function grabs data from the URL.
    MUST RETURN `True` if the scrape didn't work (i.e., if we want to log np.nan under "scraped_bool" field in 'checklist')
    """
    ... # scrape and save