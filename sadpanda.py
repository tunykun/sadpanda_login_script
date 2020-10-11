from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass

pass_entered = False

# ask for user information
username = input('Username: ')

# using getpass to obscure the text
while pass_entered == False:
	password = getpass.getpass('Password: ')
	yn_value = input(f'The length of the password you entered is {len(password)}. Re-enter your password? (y/n) ')
	yn_value = yn_value.lower()
	if(yn_value == 'n'):
		pass_entered = True

search_keys = input('Search keys: ')

# For windows, erases the command line to protect password
# if not on windows, delete this
os.system('cls')

# create webdriver and add arguments
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options = options)

# log into the website and find all th elements
driver.get('https://forums.e-hentai.org/index.php?act=Login&CODE=00')
user_in = driver.find_element_by_name('UserName')
pass_in = driver.find_element_by_name('PassWord')
login_button = driver.find_element_by_name('submit')

# input our information
user_in.send_keys(username)
pass_in.send_keys(password)
login_button.click()

# wait until the page is finished loading
while(driver.current_url != "https://forums.e-hentai.org/index.php?"):
	pass

# now go to sadpanda
driver.get('https://exhentai.org/')
select = Select(driver.find_element_by_xpath('//*[@id="dms"]/div/select'))
select.select_by_value('t')

# turn off all options except for manga and doujin (just personal preference)
for i in range(0,10):
	cat_num = 2**i
	if(cat_num != 2 and cat_num != 4):
		driver.find_element_by_xpath(f'//*[@id="cat_{cat_num}"]').click()


# input search keys
search_in = driver.find_element_by_name('f_search')
search_in.send_keys(search_keys)
filter_btn = driver.find_element_by_xpath('//*[@id="searchbox"]/form/p[1]/input[2]')
filter_btn.click()
