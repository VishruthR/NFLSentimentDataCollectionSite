from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Count, Tweets

# Create your views here.
def render_page( request ):
    row = Count.objects.raw( 'SELECT * from count' )
    count = ( row[0].count_num )
    Tweets.objects.filter(index=count)
    tweet_data = Tweets.objects.filter(index = ( (str) (count) ) )
    print( type( tweet_data[0].link ) )
    tweet = (tweet_data[0].link)
    player = tweet_data[0].player

    return render( request, 'index.html', { 'tweet' : tweet, 'count' : count, 'player' : player } )

def positive( request ):
    #html = '<h4 id="count">Count: ' + str_count + '</h4>'
    html = updatePage( request, '2' )
    return HttpResponse( html )

def negative( request ):
    html = updatePage( request, '0' )
    return HttpResponse( html )

def neutral( request ):
    html = updatePage( request, '1' )
    return HttpResponse( html )

def dontknow( request ):
    html = updatePage( request, '-1' )
    return HttpResponse( html )

def updatePage( request, sentiment ):
    #Updates count element
    row = Count.objects.raw( 'SELECT * from count' )
    str_count = ( row[0].count_num )
    count = (int) ( str_count )
    count += 1
    Count.objects.filter(counter='main').update(count_num=(str)(count))

    #Gets the count # index tweets entry to use to update html and modify data
    #Score of 2 is positive, score of 1 is neutral, score of 0 is negative
    #str_count points to last tweet, count points to current one that you want to pull up
    Tweets.objects.filter(index=str_count).update(score=sentiment)
    tweet_data = Tweets.objects.filter(index = ( (str) (count) ) )
    tweet = tweet_data[0].link
    player = tweet_data[0].player

    #html = '{% autoescape off %}{% tweet_tags ' + tweet + ' %}{% endautoescape %}Count: ' + (str)(count) + '</h4><p>How does this tweet describe ' + player + '</p>'

    #return html
    return render( request, 'index.html', { 'tweet' : tweet, 'count' : count, 'player' : player } )



