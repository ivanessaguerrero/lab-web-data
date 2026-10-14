import matplotlib.pyplot as plt
import json

tweets = []
for year in range(2009, 2019):
    with open(f'master_{year}.json', encoding='utf-8') as f:
        tweets += json.load(f)

total = len(tweets)
print(total)

phrases = ['obama', 'trump', 'mexico', 'russia', 'fake news',
           'america', 'maga', 'mainstream media']

counts = {}
for phrase in phrases:
    count = 0
    for tweet in tweets:
        message = tweet.get('full_text') or tweet.get('text') or ''
        if phrase.lower() in message.lower():
            count += 1
    counts[phrase] = count
    print(phrase, count)

print('| phrase            | percent of tweets |')
print('| ----------------- | ----------------- |')
for phrase in phrases:
    percent = counts[phrase] / total * 100
    print(f'| {phrase:>17} | {percent:05.2f}             |')
percents = [counts[phrase] / total * 100 for phrase in phrases]

plt.figure(figsize=(8, 5))
plt.barh(phrases, percents)
plt.xlabel('Percent of tweets')
plt.ylabel('Phrase')
plt.title('How often each phrase appears in the tweet archive')
plt.tight_layout()
plt.savefig('tweets.png')