from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import json

driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()


def index(request):
    return render(request, 'index.html')

def getResults(request):
    mood = request.GET['mood']
    streaming = request.GET['streaming']
    sort = request.GET['sort']
    titles = []
    ratings = []

    sortTitles = []
    sortRatings = []
    sortedList = []


    def mainFunction():
        
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)
                rating = row.find_element_by_class_name("css-1px39yc")
                ratingMain = rating.text
                ratingMain = float(ratingMain[0:3])
                ratings.append(ratingMain)

        except:
            print("Error in Clicking Loading")

        if(sort == 'random'):
            random1, random2, random3 = random.sample(titles, 3)
            movietitles = []
            movietitles.append(random1)
            movietitles.append(random2)
            movietitles.append(random3)
            return movietitles
            #return(HttpResponse(json.dumps(movietitles)))
        elif(sort == 'rating'):
            #Rating1
            rating1 = max(ratings)
            rating1Index = ratings.index(rating1)
            sortRatings.append(rating1)
            sortTitles.append(titles[rating1Index])
            ratings.pop(rating1Index)
            titles.pop(rating1Index)
            #Rating2
            rating2 = max(ratings)
            rating2Index = ratings.index(rating2)
            sortRatings.append(rating2)
            sortTitles.append(titles[rating2Index])
            ratings.pop(rating2Index)
            titles.pop(rating2Index)
            #Rating3
            rating3 = max(ratings)
            rating3Index = ratings.index(rating3)
            sortRatings.append(rating3)
            sortTitles.append(titles[rating3Index])
            ratings.pop(rating3Index)
            titles.pop(rating3Index)
            sortedList.append(sortRatings)
            sortedList.append(sortTitles)
            return sortedList
            #return(HttpResponse(json.dumps(sortedList)))

    if(mood=='happy' and streaming=="netflix"):
        driver.get('https://reelgood.com/movies/genre/comedy/on-netflix')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == 'happy' and streaming == 'prime'):
        driver.get('https://reelgood.com/movies/genre/comedy/on-amazon')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "sad" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/drama/on-netflix')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "sad" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/drama/on-amazon')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "angry" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/drama/on-netflix')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "angry" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/drama/on-amazon')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "depressed" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/fantasy/on-netflix')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "depressed" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/fantasy/on-amazon')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "excited" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/thriller/on-netflix')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "excited" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/thriller/on-amazon')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "loved" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/romance/on-netflix')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))

    elif(mood == "loved" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/romance/on-amazon')
        finalList = mainFunction()
        return(HttpResponse(json.dumps(finalList)))