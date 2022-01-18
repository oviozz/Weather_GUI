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
        global temp
        temp = soup.find('span', class_='wob_t q8U8x').text
        info = soup.find('div', class_='wtsRwe').text
        time = soup.find('div', class_='wob_dts').text
        global celc
        celc = soup.find('span',id='wob_ttm').text

        # Current time:
        timeurl = requests.get('https://www.google.com/search?q={}+ current time'.format(city), headers=headers).text
        souptime = BeautifulSoup(timeurl,'lxml')
        timee = souptime.find('div',class_='gsrt vk_bk FzvWSb YwPhnf').text

        # Day afters
        dayurl = requests.get('https://www.google.com/search?q=tomorrow {}+weather'.format(city), headers=headers).text
        soupp = BeautifulSoup(dayurl, 'lxml')
        dayafter = soupp.find('div',class_='wob_dts').text
        atemp = soupp.find('span', class_='wob_t q8U8x').text

        label3.config(text=dayafter)
        label3.place(x=60, y=400)

        label3a.config(text=atemp + '°F')
        label3a.place(x=80, y=420)
        #----------------------------------
        # After Torrmow
        afterdayurl = requests.get('https://www.google.com/search?q=day after tomorrow {}+weather'.format(city), headers=headers).text
        souppp = BeautifulSoup(afterdayurl, 'lxml')
        afterdayafter = souppp.find('div', class_='wob_dts').text
        datemp = souppp.find('span', class_='wob_t q8U8x').text

        label4.config(text=afterdayafter)
        label4.place(x=240, y=400)

        label4a.config(text=datemp +'°F')
        label4a.place(x=260, y=420)
        #-----------------------------------
        # In 3 day Weather
        beforedayurl = requests.get('https://www.google.com/search?q={} +weather in 3 day'.format(city),headers=headers).text
        sp = BeautifulSoup(beforedayurl, 'lxml')
        afterda = sp.find('div', class_='wob_dts').text
        datmp = sp.find('span', class_='wob_t q8U8x').text
        #----------------------------------------------------------------
        label5.config(text=afterda)
        label5.place(x=400, y=400)

        label5a.config(text=datmp + '°F')
        label5a.place(x=420, y=420)

        y = re.findall('[A-Z][^A-Z]*', info)
        x = ''
        for i in y[0:3]:
            x = x + i + '\n'

        # returning the data to label to print in the window(screen)
        label.config(text=location)
        label0.config(text=f'{time[0:7]} '+ timee)
        label1.config(text=temp + ' °F')
        label2.config(text=x[:-7])
        firstButton = tk.Button(text="Convert to °C", command=ChangetoCButton)
        firstButton.place(x=450, y=245)
        secondButton = tk.Button(text="Convert to °F", command=CtoF)
        secondButton.place(x=450, y=275)





    except AttributeError:
        label0.config(text='Invalid Location')
        label.config(text='')
        label1.config(text='')
        label2.config(text='')



def ChangetoCButton():
    label1.config(text=celc + ' °C' )

def CtoF():
    label1.config(text=temp + ' °F' )


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
dayaf = ('Courier',15,'bold')

# Big Weather app title
weather_title = tk.Label(window, text='Weather App!')
#apply the font to the text
weather_title.config(font=t)
# spaces out the title
weather_title.pack()

# Label By: Prajwal
by = tk.Label(window, text='By: Prajwal!')
by.config(font=font_size)
by.pack()



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

# Weather 3 day Forecast Prediction
label3 = tk.Label(window, font=dayaf, anchor='w')
label3.pack()

label3a = tk.Label(window, font=dayaf, anchor='w')
label3a.pack()

label4 = tk.Label(window, font=dayaf, anchor='w')
label4.pack()

label4a = tk.Label(window, font=dayaf, anchor='w')
label4a.pack()

label5 = tk.Label(window, font=dayaf, anchor='w')
label5.pack()

label5a = tk.Label(window, font=dayaf, anchor='w')
label5a.pack()






window.mainloop()
