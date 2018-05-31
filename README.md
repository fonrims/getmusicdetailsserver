# getmusicdetailsserver

getmusicdetailsserver is made only to complete the second test task. Using it you can request certain song details fetched fron iTunes. getmusicdetailsserver is made for Python 3.X.

## How to run getmusicdetailsserver
You should install dependencies:

    pip install itunesmusicsearch
    pip install flask

After that you can simply clone this project anywhere in your computer:

    git clone hhttps://github.com/fonrims/getmusicdetailsserver

And then enter the cloned repo and execute:

    python api.py
## Dependencies

getmusicdetailsserver requires [flask](https://github.com/pallets/flask) installed.
getmusicdetailsserver requires [itunesmusicsearch](https://github.com/fonrims/itunesmusicsearch) installed.

## Exemples

The easiest way to try it is acces http://127.0.0.1:5000/
You will see:

![Screenshot](http://185.28.101.85/screenshot.png "Screenshot")

Here you can enter any song name and choose one of certain details:

*   primary_genre_name
*   track_name
*   track_censored_name
*   track_view_url
*   preview_url
*   artwork_url_30
*   artwork_url_60
*   artwork_url_100
*   artwork_url_512
*   collection_name
*   track_price
*   release_date
*   track_explicitness
*   track_time
*   country
*   currency
*   copyright
*   price