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
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.chrome.options import Options

def main_program():

    # Go to leads page
    driver.find_element_by_class_name("global-nav__content").find_elements_by_tag_name("a")[-1].click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(waiting_for_page)

    # Search Education
    driver.implicitly_wait(waiting_for_page)  # seconds
    driver.find_element_by_id("global-typeahead-search-input").send_keys(search_parameter)
    time.sleep(2)

    try:
        driver.find_elements_by_class_name("artdeco-button--tertiary")[2].click()
    except:
        driver.find_elements_by_class_name("artdeco-button--tertiary")[1].click()

    bnts = driver.find_element_by_class_name("search-filter__list").find_elements_by_tag_name("li")

    bnts[2].find_element_by_class_name("search-filter").click()
    time.sleep(2)


    driver.find_element_by_class_name("link-without-visited-state").click()
    time.sleep(2)



    bnts[3].find_element_by_class_name("search-filter").click()
    time.sleep(2)

    bnts[3].find_element_by_tag_name("input").send_keys("Bangladesh")
    time.sleep(2)


    bnts[3].find_element_by_class_name("search-filter-typeahead__list").find_element_by_tag_name("button").click()
    time.sleep(2)


    input("Enter something to continue the script : \n")

    time.sleep(waiting_for_page)

    pages = int(
        driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
            "…")[-1])
    # TODO: Lets Make a funcation for that and CAll That Funcation
    for i in range(pages):

        # Go trough the page users and check if they can be messaged
        all_people_in_page = driver.find_elements_by_class_name("pv5")

        aux_count = 0

        for people in all_people_in_page:

            driver.execute_script("window.scrollTo(0, {})".format(aux_count))

            buttons = people.find_elements_by_tag_name("button")

            try:
                for b in range(len(buttons)):
                    buttons = people.find_elements_by_tag_name("button")
                    # No 2 : Change
                    # Change to "Save" in your script
                    if "Save" in buttons[b].text:
                        time.sleep(2)
                        buttons[b].click()
                        time.sleep(1)

                        lists = people.find_element_by_class_name("save-to-list-dropdown").find_elements_by_tag_name("li")[
                            2].find_elements_by_tag_name("li")

                        for ls in lists:

                            nm = ""

                            try:
                                nm = ls.text.split("\n")[0]
                            except:
                                nm = ls.text
                            # No 3 : Change
                            # You have to change this name for your desired list
                            if "it farm" == nm:

                                ls.click()

                                time.sleep(2)

                                try:
                                    driver.find_element_by_class_name("lead-cta-form__save-without-company").click()
                                    break
                                except Exception as e:
                                    break

                            time.sleep(1)


            except Exception as e:
                print(e)
                pass

        pages = int(
            driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split(
                "…")[-1])
        # TODO: Lets Make a funcation for that and CAll That Funcation

        for i in range(pages):

                time.sleep(time_per_user)
                aux_count += 80

                driver.find_element_by_class_name("search-results__pagination-next-button").click()
                time.sleep(waiting_for_page)

                # # Close one and Start another
                # Close the current browser
                driver.close()

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("E:\\Python\\Project\\ITLinkdinAutomationLeadFinder\\chromedriver.exe",chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds


# No 1 : Change
# What will be searched
search_parameter = "it farm"

# Time waiting for page
waiting_for_page = 5

# Time per user
time_per_user = 2

driver.get("https://www.linkedin.com/")
time.sleep(2)


# Function to check
can_login = True

try:
    us = driver.find_element_by_id("session_key")
except:
    can_login = False


if can_login:
    # I use environment variable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
    username = os.environ.get('my_Linkdin_username')
    password = os.environ.get('my_Linkdin_password')

    driver.find_element_by_id("session_key").send_keys(username)
    driver.find_element_by_id("session_password").send_keys(password)
    time.sleep(1)

    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    time.sleep(waiting_for_page)

    input("Enter something to continue the script : \n")


#Check if he has sales navigator
bar = driver.find_element_by_class_name("global-nav__primary-items").find_elements_by_tag_name("li")

has_navigator = False

for b in bar:
    if "Sales" in b.text:
        has_navigator = True

if has_navigator:
    main_program()
else:
    #TODO: Make a pop up
    print("Update you linkedin to run this script")






