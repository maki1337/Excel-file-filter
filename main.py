import pandas as pd
import os

# Specify the directory where the Excel file is stored
directory = './excel'

# List of invalid values
invalid_values = [-1, -2, -3, -4, -5, -6, -96, -97, -98, -99]

# Columns to check while filtering
columns_to_check = ['Q9aa','Q9ab','Q9ac','Q9ad','Q9ae','Q9af','Q9ag','Q9ah','Q9ai','Q9aj','Q9ak','Q9al','Q9am','Q9an','Q9ao','Q9ap','Q9aq','Q9ar','Q9as','Q9at','Q9au','Q9av','Q9aw','Q9ax','Q9ay','Q9az','Q9ba','Q9bb','Q9bc','Q9bd','Q9be','Q9bf','Q9bg','Q9bh','Q9bi','Q9bj','Q9bk','Q9bl','Q9bm','Q9bn','Q9bo','Q9bp','Q9bq','Q9br','Q9bs','Q9bt','Q9bu','Q9bv','Q9bw','Q10a', 'Q10b', 'Q10c', 'Q10d', 'Q10e', 'Q10f', 'Q10g', 'Q10h', 'Q10i', 'Q10j', 'Q10k', 'Q10l', 'Q10m', 'Q10n', 'Q10o', 'Q10p', 'Q10q', 'Q10r', 'Q10s', 'Q10t', 'Q10u', 'Q10v', 'Q10w', 'Q10x', 'Q10y', 'Q10z','Q11a', 'Q11b', 'Q11c', 'Q11d', 'Q11e', 'Q11f', 'Q11g', 'Q11h', 'Q11i', 'Q11j', 'Q11k', 'Q11l', 'Q11m', 'Q11n', 'Q11o', 'Q11p','Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q24a', 'Q24b', 'Q24c', 'Q24d', 'Q24e', 'Q24f', 'Q24g', 'Q24h', 'Q24i', 'Q24j', 'Q24k', 'Q24l', 'Q24m', 'Q24n', 'Q24o', 'Q24p', 'Q24q', 'Q24r', 'Q25a', 'Q25b', 'Q25c', 'Q25d', 'Q25e', 'Q25f', 'Q25g', 'Q25h', 'Q25i', 'Q25j', 'Q25k', 'Q25l']  # Add or remove column names as needed

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename == 'Anketa_podatki_neobdelani.xlsx':
        # Read the Excel file into a DataFrame
        df = pd.read_excel(os.path.join(directory, filename))

        # Remove rows where any of the checked column's value is in the list of invalid values
        df = df[~df[columns_to_check].isin(invalid_values).any(axis=1)]

        # Write the DataFrame back to the Excel file
        df.to_excel(os.path.join(directory, filename), index=False)
    
