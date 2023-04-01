import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver.exe",  options=options)
driver.get('https://www.justdial.com/Delhi/Flower-Shops/nct-10212874')
x_path="//div[@class='jsx-a7b231d6699d108 results_listing_container']/div[@style='margin-top:20px'][1]//div[@class='resultbox_textbox']"
All_shop_detail_lst=[]
for i in range(1,10):
    current_shop_detail={}
    try:
        name_xpath=f"//div[@class='jsx-a7b231d6699d108 results_listing_container']/div[@style='margin-top:20px'][{str(i)}]//div[@class='resultbox_textbox']/div[@class='resultbox_title font22 fw500 color111 complist_title']"
        name_element = driver.find_element(By.XPATH, name_xpath)
        name_element_text_=name_element.text
        phone_no_xpath  =f"//div[@class='jsx-a7b231d6699d108 results_listing_container']/div[@style='margin-top:20px'][{str(i)}]//div[@class='resultbox_textbox']//span[@class='callcontent callNowAnchor']"
        phone_element = driver.find_element(By.XPATH, phone_no_xpath)
        phone_element_text_=phone_element.text
        open_time =f"//div[@class='jsx-a7b231d6699d108 results_listing_container']/div[@style='margin-top:20px'][{str(i)}]//div[@class='resultbox_textbox']//div[@class='resultbox_activity']"
        open_time_element = driver.find_element(By.XPATH, open_time)
        open_text_=open_time_element.text.split('\n')[0]
        add_xpath =f"//div[@class='jsx-a7b231d6699d108 results_listing_container']/div[@style='margin-top:20px'][{str(i)}]//div[@class='resultbox_textbox']//div[@class='resultbox_address mt-6']"
        add_element = driver.find_element(By.XPATH, add_xpath)
        add_element_text_=add_element.text
        current_shop_detail["Shop_name"]=name_element_text_
        current_shop_detail['phone_no']=phone_element_text_
        current_shop_detail['open_time']=open_text_
        current_shop_detail['address']=add_element_text_
        All_shop_detail_lst.append(current_shop_detail)
    except:
        pass
df = pd.DataFrame.from_dict(All_shop_detail_lst)
df.to_csv('Flower_shop_detail.csv',index=False)