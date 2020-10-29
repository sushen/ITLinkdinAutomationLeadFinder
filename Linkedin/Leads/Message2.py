#  Copyright (c) 2020.
#  Version : 1.0.2
#  Script Author : Sushen Biswas
#
#  Sushen Biswas Github Link : https://github.com/sushen
#
#  !/usr/bin/env python
#  coding: utf-8

from selenium import webdriver
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

#No 1 : Change
#Change the messages as you wish, one of them will be randomly picked
subjects = [
    "I have one idea for sale.",
    "I need your opinion about one idea.",
    "I need your mentoring in this field. ",
    "I need your partnership in this reason. "
]

#No 2 : Change
#Change the messages as you wish, one of them will be randomly picked
messages = [
    "আমাদের ফেসবুকে কোন গুরুপ নেই, লিংডিনের গুরুপ গুলোতে যারা ব্লকচেইন সম্পর্কে যানে তারাই আছেন । এর মধ্যে বিভিন্ন বিশ্ববিদ্যালয়ের শিক্ষক আছেন, মেধাবি প্রগ্রামরবা আছেন আরও আছেন ব্যাবসায়িরা । \nhttps://www.linkedin.com/groups/13907711/",
    "আমাদের গুরুপে বিভিন্ন বিশ্ববিদ্যালয়ের শিক্ষক আছেন, মেধাবি প্রগ্রামরবা আছেন আরও আছেন ব্যাবসায়িরা । আমাদের ফেসবুকে কোন গুরুপ নেই, লিংডিনের গুরুপে যারা ব্লকচেইন সম্পর্কে যানে তারাই আছেন ।  \nhttps://www.linkedin.com/groups/13907711/",
    "যারা ব্লকচেইন সম্পর্কে যানে তারাই এই গুরুপে আছেন ।আমাদের ফেসবুকে কোন গুরুপ নেই, এই গুরুপে বিভিন্ন বিশ্ববিদ্যালয়ের শিক্ষক আছেন, মেধাবি প্রগ্রামরবা আছেন আরও আছেন ব্যাবসায়িরা । \nhttps://www.linkedin.com/groups/13907711/"
]


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("E:\\Python\\Project\\blockchainbd\\chromedriver.exe"
                          , chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds

#What will be searched

#Time waiting for page
waiting_for_page = 10



driver.get("https://www.linkedin.com/")

# Login

# Login
try:
    # I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
    username = os.environ.get('my_Linkdin_username')
    password = os.environ.get('my_Linkdin_password')

    driver.find_element_by_id("session_key").send_keys(username)
    driver.find_element_by_id("session_password").send_keys(password)
    time.sleep(1)

    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    time.sleep(waiting_for_page)
except:
    pass

#No 3 : Change
#Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6714413487227072512"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split("…")[-1])
except:
    pages = 1

#change the names of the list
list_to_remove = "Blockchain Connection Message"

list_to_add = "Blockchain Connection Second Message"

for i in range(pages):

    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]
    n_people = len(people)

    p = 0
    aux_count = 0
    while n_people > 0:
        time.sleep(5)
        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]

        time.sleep(1)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")

        for m in range(len(aux)):
            # No 4 : Change to "Message"
            if "Message" in aux[m].text:

                aux[m].click()

                time.sleep(2)

                try:

                    try:
                        driver.find_element_by_class_name("compose-form__subject-field").send_keys(random.choice(subjects))
                        time.sleep(1)
                    except:
                        pass

                    driver.find_element_by_class_name("compose-form__message-field").send_keys(random.choice(messages))
                    time.sleep(2)

                    # Click send

                    main_aux = driver.find_element_by_class_name("pr3")
                    main_aux.find_element_by_class_name("ml4").click()

                    time.sleep(1)

                    try:
                        driver.find_element_by_class_name("message-overlay").find_element_by_tag_name("header").find_elements_by_tag_name("button")[-1].click()
                    except:
                        pass

                    time.sleep(3)
                    break
                except:
                    driver.find_element_by_class_name("message-overlay").find_element_by_tag_name("header").find_elements_by_tag_name("button")[-1].click()
                    time.sleep(3)
                    break

        time.sleep(2)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")

        for m in range(len(aux)):
                # No 3 : Change
                # Change to "Add to another list"
                if "Add to another list" in aux[m].text:
                    aux[m].click()
                    time.sleep(3)

                    cont = driver.find_element_by_class_name("entity-lists-ta__ta-container")

                    btns = cont.find_elements_by_tag_name("button")

                    # Remove from list
                    for b in btns:
                        nm = ""
                        try:
                            nm = b.text.split("\n")[0]
                        except:
                            nm = b.text

                        if list_to_remove == nm:
                            b.click()

                    time.sleep(2)
                    mn = driver.find_element_by_class_name("entity-lists-ta__unselected-menu")
                    aux_btns = mn.find_elements_by_tag_name("button")

                    for xua in aux_btns:
                        nm = ""
                        try:
                            nm = xua.text.split(" (")[0]
                        except:
                            nm = xua.text

                        if list_to_add == nm:
                            xua.click()

                    time.sleep(1)
                    driver.find_element_by_class_name("edit-entity-lists-modal__save-btn").click()
                    break

        time.sleep(1)

        driver.find_element_by_id("content-main").click()

        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]
        n_people = len(people)


# TODO: ADD to Another List After Sending Massage - DONE
# Close the current browser
driver.close()


