from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

loc = "C:/Users/navee/Desktop/Web-automation/github-secrets.txt"
password = str(open(loc).read())

driver = webdriver.Chrome("C:/Users/navee/Desktop/Web-automation/chromedriver")
github = driver.get("https://www.github.com/login")
time.sleep(2)

login_field = driver.find_element_by_id("login_field").send_keys("anjalishyamjith05@gmail.com")
time.sleep(0.5)
password = driver.find_element_by_id("password").send_keys(password)
time.sleep(0.5)
sign_in = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
time.sleep(1)

new_repo = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
time.sleep(0.5)
repo_name = driver.find_element_by_id("repository_name").send_keys(input("Enter the name of your new repo: "))
time.sleep(0.5)
repo_desc = driver.find_element_by_id("repository_description").send_keys(input("Enter the description of your new repo (optional): "))
time.sleep(0.5)

visibility_choice = input("Do you want your repo to be public or private: ")
if visibility_choice == "public" or visibility_choice == "Public":
    visibility = driver.find_element_by_id("repository_visibility_public").click()
elif visibility_choice == "private" or visibility_choice == "Private":
    visibility = driver.find_element_by_id("repository_visibility_private").click()
else:
    print("Invalid input.")
time.sleep(0.5)

readme_choice = input("Do you want a README file: ")
if readme_choice == "Yes" or readme_choice == "yes":
    add_readme = driver.find_element_by_id("repository_auto_init").click()
time.sleep(0.5)

gitignore_choice = input("Do you want a .gitignore file: ")
if gitignore_choice == "Yes" or gitignore_choice == "yes":
    add_gitignore = driver.find_element_by_id("repository_gitignore_template_toggle").click()
time.sleep(0.5)

license_choice = input("Do you want a license for your repo: ")
if license_choice == "Yes" or license_choice == "yes":
    add_license = driver.find_element_by_id("repository_license_template_toggle").click()
time.sleep(0.5)

create_repo = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()
