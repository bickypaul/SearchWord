# SearchWord
A Django based Word Search WebApp
This WebApp basically renders a search box on browser where the user can type in a word as an input to search that word in a dataset containing 333,333 English words and the frequency of their usage in some corpus.

## Requirements (Tested on)
1. Ubuntu 18.04
2. Python 3
3. django 2.1.2

## How to execute it to run on your local machine.
1. git clone https://github.com/bickypaul/SearchWord/
2. cd SearchWord/
3. python3 manage.py runserver
4. Goto http://localhost:8000

## Frontend.
An simple jQuery based HTML template of Search Box with a Search button.

## API Endpoints.
1. GET http://localhost:8000
This endpoint renders a search box in the browser.

2. GET http://localhost:8000/search/?term=prac

the service might receive this sequence of requests, like:
  1. GET http://localhost:8000/search/?term=prac
  2. GET http://localhost:8000/search/?term=pract
  3. GET http://localhost:8000/search/?term=practi
and based on this search beahavior, suggestions for searching words will show up in the browser.

3. GET http://localhost:800/searchResults/?term=prac

This endpoint finally returns a response which is of JSON array containing 25 results, ranked by criteria (see below):
1. Matches occurs anywhere in the string, not just at the beginning. For example, eryx matches archaeopteryx (among others).
2. Matches at the start of a word ranks higher, For example, for the input pract, the result practical ranks higher than impractical.
3. Common words (those with a higher usage count) ranks higher than rare words.
4. Short words ranks higher than long words. For example, given the input environ, the result environment ranks
  higher than environmentalism.
5. An exact match should always be ranked as the first result.

## Hosted Publicly, you can access it on below provided address:
website: https://bicky.pythonanywhere.com/
