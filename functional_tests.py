# start selenium webdriver to create Firefox browser window
from selenium import webdriver

browser = webdriver.Firefox()

# Home page
browser.get('http://localhost:8000')

# Page title and header mention to-do lists
assert 'To-Do' in browser.title

# Invite to enter a to-do item immediately

# Type entry into a text box

# Upon hitting enter, page should update, and then page should list
# "1: " previous entry, as an item in a to-do list

# There should still be a text box to enter another item

# Page should update again, and should show 2 items

# Site should generate a unique URL, with explanatory text

# Upon visiting the URL, the to-do list with 2 items should still be there

browser.quit()
