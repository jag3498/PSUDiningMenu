# PSUDiningMenu
A python script to scrape menu data from Penn State's on campus dining site

Currently running as a Google cloud function, configured only for West Dining Hall. 
Call as HTTP GET: 
https://us-central1-getpsumenu.cloudfunctions.net/PSUMenu

Will throw "Error: could not handle the request" if no menus are available. 

This API is designed to be use by a web app, mobile app, or a Google Home app to show menu data.
