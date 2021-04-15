from selenium import webdriver
from my_cloud_imp import do_login
import json

def main():
    # Loading months.json file
    with open('months.json') as f:
        months_dict = json.load(f)

    # Looping over 3 properties from 1 to 3
    for p in range(1, 4):
        # Iterating over all the months in months_dict
        for v in months_dict.values():
            # Assigning start and end date
            start_date = v[0]
            end_date = v[1]
            # Initializing the driver
            driver = webdriver.Chrome()
            driver.maximize_window()

            # Calling login function to download data in default folder.
            try:
                do_login(driver, start_date, end_date, property=p)
            finally:
                driver.close()
            return


if __name__ == '__main__':
    main()