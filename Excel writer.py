#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xlsxwriter
df = pd.DataFrame({'Fruits': ["Apple","Orange","Mango","Kiwi"],
                     'City' : ["Shimla","Sydney","Lucknow","Wellington"]
                  })
print(df)
excel_writer = pd.ExcelWriter('pandas_df.xlsx', engine='xlsxwriter')
df.to_excel(excel_writer, sheet_name='first_sheet')
df.to_excel(excel_writer, sheet_name='second_sheet')
df.to_excel(excel_writer, sheet_name='third_sheet')
excel_writer.save()


# In[ ]:




