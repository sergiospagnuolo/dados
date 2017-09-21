# coding: utf8

import tweepy #https://github.com/tweepy/tweepy
import csv

#credenciais da API do Twitter
consumer_key = "DmC8swONtERKWnnSVk8iylQhT"
consumer_secret = "zJyozzGxfVHk1ViPrC5OrI1KkvpC0LkyzGD7OFFcjSsci3J6OG"
access_key = "2295005041-IX1PiWtXPNtcxops6nED5hajFvGTIKqnRObEFr3"
access_secret = "O27v8Pea8MCLCsUVd18ew7yH7f1BnrxZmv0ShqXuNynod"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    #Requiste inicial para tweets mais recentes
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    alltweets.extend(new_tweets)

    #salva o ID to Tweet
    oldest = alltweets[-1].id - 1

    #continua pegando Tweets até o final
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(alltweets)))

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

    #escreve o csv
    with open('%s_tweets.csv' % screen_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("brwikiedits")
