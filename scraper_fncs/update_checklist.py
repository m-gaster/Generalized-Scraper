import pandas as pd
import numpy as np

def update_checklist_table(checklist:pd.DataFrame,
                           checklist_path:str, 
                           scraped_bool_col:str,
                           URL_col:str,
                           URL_of_newly_scraped:str,
                           log_as_nan=False
                           ):
    
    # checklist = pd.read_csv(checklist_path)

    # confirm that bools are numerical and not True, False
    unique_bools = checklist[scraped_bool_col].unique().tolist()
    
    if log_as_nan:
        pos_bool = np.nan
    else:
        if not any(num_bool in unique_bools for num_bool in [0,1]): # if 0 and 1 aren't in 
            assert any(bool_ in unique_bools for bool_ in [True, False])
            pos_bool = True
        elif not any(bool_ in unique_bools for bool_ in [True, False]):
            assert any(num_bool in unique_bools for num_bool in [0,1])
            pos_bool = 1


    # update value
    checklist.set_index(URL_col, 
                        inplace=True)
    checklist.loc[URL_of_newly_scraped, scraped_bool_col] = pos_bool

    # save/export
    checklist.to_csv(checklist_path,
                     index=True)