#twttr
#Remove vowels from a string

vowels = "aeiouAEIOU"
tweet = ""
user_input = input("Write your tweet: ")

for char in user_input:
    if char not in vowels:
        tweet += char

print(tweet)
