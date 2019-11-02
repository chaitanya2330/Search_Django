# My Search
A HTTP service that provides an endpoint for fuzzy search / autocomplete of English words.

*A Django based Word Search WebApp
*This WebApp basically renders a search box on browser where the user can type in a word as an input to search that word in a *dataset containing 333,333 English words and the frequency of their usage in some corpus.

# Requirements.txt
*Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

# Front-end
HTML template of Search Box with a Search button.

# API End Points
GET http://localhost:8000 :- *This endpoint renders a search box in the browser.

*When input is the(partial) word that the user has typed so far. For example, if the user is looking
up procrastination, the service might receive this sequence of requests:

GET http://localhost:8000/search/?term=proc

GET http://localhost:8000/search/?term=proca

GET http://localhost:8000/search/?term=procas

GET http://localhost:8000/search/?term=procasti 
and based on this search behavior, suggestions for searching words will show up in the browser.

The response is a JSON array containing upto 25 results, ranked by some criteria (see
below):-
Constraints
1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx
should match archaeopteryx (among others).
2. The ranking of results should satisfy the following:
a. We assume that the user is typing the beginning of the word. Thus, matches at the
start of a word should be ranked higher. For example, for the input pract, the result
practical should be ranked higher than impractical.
b. Common words (those with a higher usage count) should rank higher than rare
words.
c. Short words should rank higher than long words. For example, given the input
environ, the result environment should rank higher than environmentalism.
i. As a corollary to the above, an exact match should always be ranked as the
first result.
