#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import json
import pandas as pd


# In[79]:


pattern = '<script id="data-state" data-state="true" type="application/json">(.*?)</script>'


# In[80]:


# insert a link from AirBnb
url = 'https://www.airbnb.ru/s/Выборгский-район--Санкт~Петербург--Россия/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&query=Выборгский%20район%2C%20Санкт-Петербург%2C%20Россия&place_id=ChIJwROo_KI1lkYRZohzlad4XhI&_set_bev_on_new_domain=1614368532_NTU3MWNkMzAxNTJi'

pages = 15 # number of pages needen to parse


# In[81]:


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.3'}
# this block is to collect data


# In[82]:


data = list() 


# In[83]:


for j in range(1, pages+1):
    url_p = url + f'&items_offset={str((j - 1) * 20)}&section_offset=3'
    r = requests.get(url_p, headers=headers).text
    d = json.loads(re.findall(pattern, r)[0])
    try:
        needed_data = d['niobeMinimalClientData'][1][1]['data']['dora']['exploreV3']['sections'][0]['items']
    except:
        continue
    
    for i in needed_data:
        # here are some variables im intrested in
        data.append({'id': i['listing']['id'],
                    'name': i['listing']['name'],
                     'lat': i['listing']['lat'],
                    'lng': i['listing']['lng'],
                    'avgRating': i['listing']['avgRating'],
                     'personCapacity': i['listing']['personCapacity'],
                     'previewAmenityNames': ', '.join(i['listing']['previewAmenityNames']),
                     'reviewsCount': i['listing']['reviewsCount'],
                     'isSuperhost': i['listing']['isSuperhost'],
                     'isNewListing': i['listing']['isNewListing'],
                    'price': i['pricingQuote']['rate']['amount']})
        
        


# In[84]:


dataframe = pd.DataFrame(data).drop_duplicates()


# In[85]:


dataframe.to_csv('vyborgsky_rayon.csv', index=False)


# In[ ]:




