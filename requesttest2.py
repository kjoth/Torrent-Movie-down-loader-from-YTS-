# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:17:52 2017

@author: Karthick
"""

from bs4 import BeautifulSoup
#from io import BytesIO
import urllib.request as urllib2
import subprocess
import time



def torrent_Link_finder(url_name, movie_name):
    try:
        #html_page = urllib2.urlopen("https://yts.ac/king-cobra-full-movie-2016-yify-torrent-download/")
        html_page = urllib2.urlopen(url_name)
        
        soup = BeautifulSoup(html_page,"lxml")
        magnet_link = ''
        for link in soup.findAll('a', href=True, text=' 720p'):
            #print(link.get('href'))
            magnet_link=link.get('href')
            #print(magnet_link)

        torrentPath = r'C:\Users\Karthick\AppData\Roaming\uTorrent\uTorrent.exe'
        subprocess.Popen("%s %s" % (torrentPath, magnet_link ))
        print("'" + movie_name + "' Found")
    
    except urllib2.HTTPError as err:
        if err.code == 404:
            print("'" + movie_name + "' Movie not found")
        else:
            #print(e)
            raise
        exit
    

def user_input_movie(movie_name):
    #user_input=input('Enter movie name as in IMDB: ')
    #a=user_input
    a=movie_name.replace(" ","-") 
    #print(a)
    url_name="https://yts.ac/" + a + "-full-movie-*"
    #print(url_name)
    torrent_Link_finder(url_name,movie_name)
    
def user_input_movie1(Movie_List=None):
    with open ("MoviesList.txt", "r") as f:
        Movie_List=f.readlines()
        Movie_List=[x.strip() for x in Movie_List]
        #print(Movie_List)
        
    for x in Movie_List:
        user_input_movie(x)
    
print("WELCOME")
print("Press 1 if you want to type a Movie name") 
print("Press 2 if you want to input a Movie file")

user_input_choice= input("Enter 1 or 2 : ")

if user_input_choice =="1":
    user_input=input('Enter movie name as in IMDB: ')
    movie_name=user_input
    user_input_movie(movie_name)
    
elif user_input_choice == "2":
    user_input=input('Enter movie file name: ')
    movie_filename=user_input
    user_input_movie1(movie_filename)
else:
    print("Retry again")
    print("Closing in 5 seconds")
    time.sleep(5)
    #exit()

#user_input_movie1()









    

#os.startfile(magnet_link)
   
    