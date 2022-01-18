from bs4 import BeautifulSoup
import tkinter as tk
import requests
import re

# Created By Prajwal!

headers = {
    'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

#Getting location info
def getWeather(window):
    try:
        city = textfield.get()
        url = requests.get('https://www.google.com/search?q={}+weather'.format(city), headers=headers).text
        soup = BeautifulSoup(url, 'lxml')
        location = soup.find('div',class_='wob_loc q8U8x').text
        temp = soup.find('span', class_='wob_t q8U8x').text
        info = soup.find('div', class_='wtsRwe').text
        time = soup.find('div', class_='wob_dts').text

        y = re.findall('[A-Z][^A-Z]*', info)
        x = ''
        for i in y[0:3]:
            x = x + i + '\n'

        # returning the data to label to print in the window(screen)
        label.config(text=location)
        label0.config(text=time)
        label1.config(text=temp + ' °F')
        label2.config(text=x[:-7])

    except AttributeError:
        label0.config(text='Invalid Location')

#initial start
window = tk.Tk()
#size
window.geometry('600x500')
#title of the app
window.title('Weather')

#Font Family
loc = ('Courier',25,'bold')
font_size = ('Courier', 15, 'bold')
t = ('Arial', 35, 'bold')

# Big Weather app title
weather_title = tk.Label(window, text='Weather App!')
#apply the font to the text
weather_title.config(font=t)
# spaces out the title
weather_title.pack()

# Creates a text field title
textfield = tk.Entry(window, font=font_size)
# Creates a space
textfield.pack(pady=30)
# Accept input from the textfield
textfield.focus()
# checks if pressed return, to get the function(getweather)
textfield.bind('<Return>', getWeather)


#from the function it takes in the value/data
label = tk.Label(window,font=loc)
label.pack()

label0 = tk.Label(window, font=font_size)
label0.pack()

label1 = tk.Label(window, font=t)
label1.pack()

label2 = tk.Label(window, font=font_size)
label2.pack()

# Label By: Prajwal
by = tk.Label(window, text='By: Prajwal!')
by.config(font=font_size)
# Spacing to the label
by.pack(pady=80)

window.mainloop()
