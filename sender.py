from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

name = input('Introduce el nombre del usuario o del grupo : ')
message = input('Introduce tu mensaje : ')
counter = int(input('Introduzca el numero de veces que se va a mandar el mensaje : '))

input('Presione cualquier tecla tras escanear el codigo QR')

user = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[20]/div/div/div[2]/div[1]/div[1]/span/span')
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(counter):
    msg_box.send_keys(message)
    button = driver.find_element_by_class_name('hnQHL')
    button.click()
    
