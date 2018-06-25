#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).

Access tokens are the thing that applications use to make API requests on behalf of a user. The access token represents the authorization of a specific application to access specific parts of a user’s data.

Access tokens must be kept confidential in transit and in storage. The only parties that should ever see the access token are the application itself, the authorization server, and resource server. The application should ensure the storage of the access token is not accessible to other applications on the same device. The access token can only be used over an https connection, since passing it over a non-encrypted channel would make it trivial for third parties to intercept.

The token endpoint is where apps make a request to get an access token for a user. This section describes how to verify token requests and how to return the appropriate response and errors.

consumer_key="x4gCP3*************"
consumer_secret="XoXNqNOrI51***************"

access_token="2919790812************************"
access_token_secret="**************0DEgMGY**************u"
ass12_1.txt
Displaying ass12_4.txt.

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

C:\Users\Malay Kumar>nslookup facebook.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          157.240.16.35


C:\Users\Malay Kumar>nslookup youtube.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    youtube.com
Addresses:  2404:6800:4002:806::200e
          216.58.221.46
ass12_2.txt
Displaying ass12_4.txt.


#Q.3- Using Tweepy library try to extract tweets from Twitter.

import tweepy

consumer_key_038="x*******************8"
consumer_secret_038="*************************88"

access_token_038="2919*****************************"
access_token_secret_038="***************************"

auth=tweepy.OAuthHandler(consumer_key_038,consumer_secret_038)
auth.set_access_token(access_token_038,access_token_secret_038)
api=tweepy.API(auth)

hastag="#"+input("entet the hastag you want to find:")
num=int(input("enter the number of text you want tp fetch:"))

tweets=api.search(hastag,lang="en",count=num,tweet_mode="extended")

for tweet in tweets:
	print(".....................")
	print(tweet.full_text)
	print(".....................")

ass12_3.py
Displaying ass12_4.txt.

#Q.4- What is a difference between library and API . Figure it out with examples.

API:
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

Imagine you’re sitting at a table in a restaurant with a menu of choices to order from. The kitchen is the part of the “system” that will prepare your order. What is missing is the critical link to communicate your order to the kitchen and deliver your food back to your table. That’s where the waiter or API comes in. The waiter is the messenger – or API – that takes your request or order and tells the kitchen – the system – what to do. Then the waiter delivers the response back to you; in this case, it is the food.

LIBRARY:

A library is a collection of code built to perform common tasks. Library code tends to be relatively stable and bug free. Use of appropriate libraries can reduce the amount of code the need to be written. It will tend to reduce line of code counts for an application will increasing the rate at which functionality is delivered. In most cases, it is better to use a library routine than to write your own code.
