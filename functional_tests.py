from selenium import webdriver

browser = webdriver.Edge()
browser.get('http://localhost:8000')
# we see To Do title and header
assert "To-Do!" in browser.title

# нам предлагается ввести элемент списка

# мы набираем "Find work"

# после нажатия Enter страница обновляется и теперь содержит "1: Find work"

# текстовое поле по-прежнему приглашает нас добавить еще один элемент

browser.quit()
