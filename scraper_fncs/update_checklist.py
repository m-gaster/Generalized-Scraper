import pandas as pd
import numpy as np

def update_checklist_table(checklist_path:str, 
                           scraped_bool_col:str,
                           ID_col:str,
                           ID_of_newly_scraped:str,
                           log_as_nan=False
                           ):
    
    checklist = pd.read_csv(checklist_path)

    # confirm that bools are numerical and not True, False
    unique_bools = checklist[scraped_bool_col].unique().tolist()
    
    if all(num_bool in unique_bools for num_bool in [0,1]):
        pos_bool = 1
    elif all(bool_ in unique_bools for bool_ in [True, False]):
        pos_bool = True
    
    if log_as_nan:
        pos_bool = np.nan

    # update value
    checklist.set_index(ID_col, 
                        inplace=True)
    checklist.loc[ID_of_newly_scraped, scraped_bool_col] = 1

    # save/export
    checklist.to_csv(checklist_path,
                     index=True)