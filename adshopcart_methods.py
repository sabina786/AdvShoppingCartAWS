import datetime
from time import sleep
from selenium import webdriver #import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # -----add this import for drop down list
from selenium.webdriver import Keys


from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)



def setUp():
    print(f'Launch {locators.app} App')
    print(f'Test Started at: ¨{datetime.datetime.now()}')
    print(f'--------------------***-----------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.advshoppingcart_homepage_url)

    if driver.current_url == locators.advshoppingcart_homepage_url and driver.title == locators.advshoppingcart_home_page_title:
        print(f'Yey! {locators.app} App website launched successfully!!!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        print(driver.title)
        sleep(1)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'--------------------***-----------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def signup():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').click()
    sleep(0.5)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenum)
    sleep(0.5)
    driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
    sleep(0.5)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.5)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(0.5)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.5)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(2)
    print(f' ---- New Account Created ------')


def check_full_name():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    # driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="My_account"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "My_account"]').click()
    sleep(0.5)

    if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
        print(f'--- The Full name of the User: {locators.full_name} ------')
    else:
        print(f'-----Something went wrong please check you Open Account page code----')
    sleep(0.5)


def check_orders():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    sleep(3)
    no_order = driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    if no_order == True:
        print(f'-----There is no order-------')
    else:
        print(f'----Something is wrong---Check the code-------')


def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(5)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="Sign_out"]').click()
    sleep(0.5)


def log_in():
    if driver.current_url == locators.advshoppingcart_homepage_url:
        print(f'---- Your are in Home Page -----')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(1)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(2)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
        print(f'------ Successfully login with new account -------- ')
    else:
        print(f'----Something went wrong check your code please --------')

def delete_test_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(5)
    # driver.find_element(By.XPATH, '//h3[contains(., "MY ACCOUNT")]').click()
    # driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate="My_account"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').click()
    sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    sleep(3)



def verify_account_deleted():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(5)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)

    #     driver.find_element(By.ID, 'signInResultMessage').is_displayed():
    # if driver.find_element(By.XPATH, '//label[@id = "signInResultMessage"]').text == 'Incorrect user name or password.':
    if driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]'
                                  '[contains(., "Incorrect user name or password")]').is_displayed():
        sleep(5)
        print(f'-----Account successfully deleted!!Account name is {locators.username}------')
    else:
        print(f'--Something went wrong check the code')


def check_home_page():
    driver.get(locators.advshoppingcart_homepage_url)
    lst_opts1 = ['SPEAKERS', 'TABLETS', 'HEADPHONES', 'LAPTOPS', 'MICE']
    for e in lst_opts1:
        if driver.find_element(By.XPATH, f"//span[contains(., '{e}')]").is_displayed():
            sleep(0.5)
            print(f"We can see '{e}' link on the homepage")
        else:
            print("'{element}' link is not displayed on the homepage!")

    lst_opts2 = ['SPECIAL OFFER', 'POPULAR ITEMS', 'CONTACT US']
    # for l in lst_opts2:
    #     if driver.find_element(By.XPATH, f'//a[contains(., "{l}")]').click():
    #         sleep(0.5)
    #         driver.find_element(By.XPATH, f'//a[contains(., "{l}")]').is_displayed()
    #         sleep(0.5)
    #         if driver.find_element(By.XPATH, f"//*[self::h1 or self::h3][contains(., '{item}')]").is_displayed():
    #         sleep(0.5)
    #         print(f'----{l} is displayed------')
    #     else:
    #         print(f'----{l} does not displayed-----')

    for l in lst_opts2:
        if driver.find_element(By.XPATH, f'//a[contains(., "{l}")]').is_displayed():
            sleep(0.5)
            driver.find_element(By.XPATH, f'//a[contains(., "{l}")]').click()
            sleep(1)
            if driver.find_element(By.XPATH, f"//*[self::h1 or self::h3][contains(., '{l}')]").is_displayed():
                sleep(0.5)
                print(f'****{l} is displayed.****')
            else:
                print(f'{l} is not displayed.')

    if driver.find_element(By.XPATH, f'//span[contains(., "dvantage")]').is_displayed()\
            and driver.find_element(By.XPATH, f'//span[contains(., "DEMO")]').is_displayed():
        sleep(1)
        print(f'------Logo is Displayed-------')
    else:
        print(f'---The logo is not displayed------')

    driver.find_element(By.XPATH, f'//a[contains(., "CONTACT US")]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, f'//h1[contains(., "CONTACT US")]').is_displayed()
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Headphones')
    sleep(0.5)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('Bose SoundLink Around-ear Wireless Headphones II')
    sleep(0.5)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(0.5)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a').is_displayed():
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a').click()
        print('-----Continue shopping button is displayed.------')
    else:
        print('-----Something went wrong check the code for continue shopping button--------')




# setUp()
# signup()
# check_full_name()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# verify_account_deleted()
# check_home_page()
# tearDown()

