# TheSkyDiary

## Overview

TheSkyDiary.com will be a website that users can go to see a sky 
drawing from a day that is important to them (from Sep 1st 1973
to present), and allow them to easily buy prints via an email.     

I'm currently selling skies and there is a lot of manual work and no
current way for users to see proofs of the sky online.  

This project will use Django, as well as an email API and perhaps a
shipping cost API.  
 
## Functionality

The Sky Diary will consist of the following pages:
- Homepage where the user enters a date.  
- page that tells more about the story and let's user enter email
    - message if the date is before Sep 1 1973
    - message if it's the day the artist was unconscious for surgery 
    - message if it's in the future
- page after info was entered with a link to follow on instagram 
    - At this point, the email and name are stored in the database 
- Footer links: privacy policy, content, contact, about the artist, sitemap

Once the user has filled out the information, they will receive an email
at 8am the next morning with a watermarked proof of the sky and a link to 
purchase.  The email will tell the story, try and get the user to buy,   

- I will be able to upload skies via an admin panel.  
- There will be an automatic watermark when uploading.  

I will use Bootstrap for the CSS. 

## Data 

There will be 4 tables:

- Skies
    - diary_date (string like YYYY.MM.DD)
    - watermarked_proof (image field)
    - print_proof (image field)
    - number of purchases for a given sky 
- Customer
    - first name
    - last name
    - email
    - phone number
    - notes
- Order
    - customer id
    - date
    - items 
- Order Items
    - sky ID: YYYY.MM.DD.####
    - Order Number (many of these to one order)


##Schedule
Week 1
- Get Django environment setup (3 hours)
- Get models setup (2 hours)
        - https://github.com/PdxCodeGuild/20180116-FullStack-Day/blob/master/4%20Django/docs/06%20-%20Media%20Files.md
- Get template setup for homepage (3 hours)
- Get some data entered to test (4 hours)
- create conditions for dates that don't work. (2 hours)
Week 2
- Get admin panel to allow uploading of proofs 
- Get auto-watermark setup. 
- Get email api setup 
- get book of sky diary entered 
Week 3
- Test and make improvements    


![test](test.jpg)


