
import nltk
import re
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk import punkt
from nltk.tag.stanford import StanfordNERTagger
from nltk.corpus import wordnet as wn
import pandas as pd
 
#print(get_stop_words('english'))
excel = pd.ExcelFile("D:/machine learning/software-design-usingNLP-master v2/data/final_output_banking_2.xlsx")
SimMean = excel.parse("Sheet1")

temp_df=SimMean[SimMean["ID"].duplicated(keep=False)]
merged_df=temp_df.astype(str).groupby(temp_df.ID, as_index=False).agg(','.join)
temp_df=SimMean.drop(temp_df.index,axis=0).append(merged_df,ignore_index=True).sort_values("ID").drop(columns="ID")
SimMean = temp_df
SimMean['User']=temp_df['User'].str.split(',').apply(set).str.join("")


writer = pd.ExcelWriter('D:/machine learning/software-design-usingNLP-master v2/data/sorted_out.xlsx')
temp_df.to_excel(writer, sheet_name='Sheet1',index=False)
writer.save()





