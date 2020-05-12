def only_keep_municipalities_and_Hele_Landet(df):
    """ delete all non-municipalities

    Args:
        df (pd.DataFrame): pandas dataframe with the column "municipality" as a string

    Returns:
        df (pd.DataFrame): pandas dataframe

    """ 
    
    for val in ['Christiansø']:
        
        I = df.municipality.str.contains(val)
        df = df.loc[I == False] # keep everything else
    
    return df
