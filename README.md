# scrape_grailed
This script was made in Python to scrape the digital marketplace [Grailed](https://www.grailed.com) for images of a search. It was intended to acquire images that I could use as filler for a website I made called [Adorn](https://adorn-frontend.vercel.app) which I have recently published. 

This script has multiple helper functions that come together to take url and extracts the image from the urls. This was done on more than 50 Grailed posts tagged with Yohji Yamamoto. The urls were compiled into a dataframe and exported as a csv using Pandas to make the url parsing easier. 

To use this you can change the name Yohji Yamamoto to whatever you want be it a brand or clothing article like pants or shoes. 