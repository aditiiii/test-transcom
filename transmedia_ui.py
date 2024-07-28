from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def create_board():
    try:
        name_your_first_board_field = driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div/input")
        print('No board exists')
        name_your_first_board_field.send_keys("Test")
        name_your_first_board_field.send_keys(Keys.ENTER)
        print('New board created')
    except Exception as e:
        print('Already Board exists')
        existing_board_1 = driver.find_element(By.ID,"board-1")
        existing_board_1.click()
        print('Existing Board clicked')
    
    print("Board step completed")
    time.sleep(2)

def print_list():
    try:
        list_items = driver.find_elements(By.CSS_SELECTOR,'input[data-cy="list-name"]')
        print('List item count:',len(list_items))
        for list_item in list_items:
            if(list_item.get_attribute('value')):
                print(list_item.get_attribute('value'))
    except Exception as e:
        print('No list items found.')
        

def create_list():
    try:
        add_list_button = driver.find_element(By.CSS_SELECTOR,'[data-cy="create-list"]')
        add_list_button.click()
        print('add list button clicked') 
    except Exception as e: #existing list items
        print('List name input already open.')

    enter_list_title_input = driver.find_element(By.CSS_SELECTOR,'[data-cy="add-list-input"]')
    enter_list_title_input.send_keys("List-X")
    enter_list_title_input.send_keys(Keys.ENTER)
    
    enter_list_title_input = driver.find_element(By.CSS_SELECTOR,'[data-cy="add-list-input"]')
    enter_list_title_input.send_keys("List-Y")
    enter_list_title_input.send_keys(Keys.ENTER)
    
    time.sleep(3)
    print_list()

    
def delete_list():
    time.sleep(3)
    try:
        list_options = driver.find_elements(By.CSS_SELECTOR,'button[data-cy="list-options"]')
        if(len(list_options) > 0):
            print('List options found')
            list_options[0].click()
            delete_list_item = driver.find_elements(By.CSS_SELECTOR,'div[data-cy="delete-list"]')
            delete_list_item[0].click()
            time.sleep(2)
            print('List item deleted')
        else:
            print('Did not find any list opiton.')
    except Exception as e:
        print('Failed to delete list item.')
    print_list()

driver = webdriver.Chrome()
driver.get('http://localhost:3000/')
driver.maximize_window()
time.sleep(2)

create_board()
create_list()
delete_list()
print('Test completed')
time.sleep(50)
