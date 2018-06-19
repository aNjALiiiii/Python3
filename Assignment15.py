#Ques1 Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com"
#"jeff42@amazon.com"
import re
emails=["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
for i in range(len(emails)):
    email=emails[i]
    email=re.split('[@.\s_]+',email)
    emails[i]=email
print(emails)

#Ques2 Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
result=re.findall(r'\b[bB]\w+',text)
print(result)

#Ques3 Split the following irregular sentence into words
sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
sentence1=" ".join(re.split('[;,\s_]+', sentence))
print(sentence1)

#Ques4

def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

tweet = '''Good advice! RT @TheNextWeb: What I would do
differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print(clean_tweet(tweet))

