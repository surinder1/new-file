#Q.1- Extract the user id, domain name and suffix from the following email addresses. 
#emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"

import re

#method-1
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9]+)@([A-Za-z0-9]+).([a-z]+)")
result=p.findall(emails)
print(result)

p=re.compile(r"($@.\\b)")
result=p.find(emails)

print(result.group())


#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

import re

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

p=re.compile(r"\b[bB]\w+")

result=p.findall(text)

for r in result:
	print(r)

	
#Q.3- Split the following irregular sentence into words 

import re

sentence = "A, very very; irregular_sentence"

p=re.compile(r"[^A-Za-z0-9]")
result=p.sub(" ",sentence)
 
print(result)


# ##Q.4- Clean up the following tweet so that it contains only the user’s message. 
#That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 

tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
#desired_output = 'Good advice What I would do differently if I was learning to code today'

import re

p=re.compile(r"(.+)! (.+): (.+) http(.+)")
result=p.match(tweet)
 
print(result.group(1),result.group(3))