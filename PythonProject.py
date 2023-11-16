import schedule 
import smtplib 
import requests 
from bs4 import BeautifulSoup 


def umbrellaReminder(): 
	city = "Mumbai"
	
	# creating url and requests instance 
	url = "https://www.google.com/search?q=" + "weather" + city 
	html = requests.get(url).content 
	
	# getting raw data 
	soup = BeautifulSoup(html, 'html.parser') 
	temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
	time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
	
	#print(html)

	# formatting data 
	sky = time_sky.split('\n')[1] 

	if sky == "Smoke" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy": 
		print("Sending email...")
		smtp_object = smtplib.SMTP('smtp.gmail.com', 587) 
		
		# start TLS for security 
		smtp_object.starttls() 
		
		# Authentication 
		smtp_object.login("srk.ddk@gmail.com", "xwhgueqolymlzdzm") 
		subject = "Umbrella Reminder"
		body = f"Take an umbrella before leaving the house.Weather condition for today is {sky} and temperature is {temperature} in {city}." 
		msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nPythonProject".encode('utf-8') 
		
		# sending the mail 
		smtp_object.sendmail("srk.ddk@gmail.com", "srk.ddk@gmail.com", msg) 
		
		# terminating the session 
		smtp_object.quit() 
		print("Email Sent!") 

 
schedule.every().day.at("17:37").do(umbrellaReminder) 

while True: 
	schedule.run_pending() 

