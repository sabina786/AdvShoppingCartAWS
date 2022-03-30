import datetime
from faker import Faker
fake = Faker(locale='en_CA')

# ------------------ Moodle web App DATA PARAMETERS ---------------------
app = 'Advantageshoppingcart'
advshoppingcart_homepage_url = "https://advantageonlineshopping.com/#/"
advshoppingcart_home_page_title = "\xa0Advantage Shopping"

username = fake.user_name()[4:15]
email = fake.email()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'

phonenum = fake.phone_number()
country = fake.current_country()
city = fake.city()
address = fake.address().replace("\n", " ")[0: 50]
province = fake.province()[0: 10]
postal_code = fake.postalcode()

subject = f'--Todays date is:- {datetime.datetime.now()}. '



