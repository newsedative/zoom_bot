from time import sleep
from selenium import webdriver


browserl = webdriver.Chrome(r'C:\Users\1\Downloads\chromedriver_win32\chromedriver.exe')
browserl.implicitly_wait(5)
browserl.get('https://us04web.zoom.us/j/77519853821?pwd=HHsw1UuKZSICVx5uHhcRns--puVf67.1#success')
sleep(15)
browserl.get('https://us04web.zoom.us/signin')
email = browserl.find_element_by_id('email')
email.send_keys('nonetype324@gmail.com')
password = browserl.find_element_by_id('password')
password.send_keys('zoom123ZOOM')
signin = browserl.find_element_by_class_name('.btn btn-primary signin user')
signin.click()
browserl.get('https://us04web.zoom.us/j/77519853821?pwd=HHsw1UuKZSICVx5uHhcRns--puVf67.1#success')
open_in_br = browserl.find_element_by_link_text('Войдите с помощью браузера')
open_in_br.click()
