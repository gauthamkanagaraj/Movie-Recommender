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
    titles = []
    if(mood=='happy' and streaming=="netflix"):
        driver.get('https://reelgood.com/movies/genre/comedy/on-netflix')

        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))
        
    elif(mood == 'happy' and streaming == 'prime'):
        driver.get('https://reelgood.com/movies/genre/comedy/on-amazon')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "sad" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/drama/on-netflix')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "sad" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/drama/on-amazon')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "angry" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/drama/on-netflix')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "angry" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/drama/on-amazon')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "depressed" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/fantasy/on-netflix')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "depressed" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/fantasy/on-amazon')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "excited" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/thriller/on-netflix')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "excited" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/thriller/on-amazon')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "loved" and streaming == "netflix"):
        driver.get('https://reelgood.com/movies/genre/romance/on-netflix')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))

    elif(mood == "loved" and streaming == "prime"):
        driver.get('https://reelgood.com/movies/genre/romance/on-amazon')
        try:
            movies = driver.find_element_by_tag_name("main")
            table = movies.find_element_by_tag_name("tbody")
            rows = table.find_elements_by_tag_name("tr")

            for row in rows:
                title = row.find_element_by_class_name("css-1u7zfla")
                titles.append(title.text)

        except:
            print("Error in Clicking Loading")

        random1, random2, random3 = random.sample(titles, 3)
        movietitles = []
        movietitles.append(random1)
        movietitles.append(random2)
        movietitles.append(random3)
        return(HttpResponse(json.dumps(movietitles)))