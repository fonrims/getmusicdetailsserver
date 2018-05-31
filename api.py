from flask import Flask, request
import itunesmusicsearch


app = Flask(__name__)

@app.route('/')
#This page is made only as an exemple
def homepage():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>exemple</title>
</head>

<body>
 <form method="GET" action="http://127.0.0.1:5000/musicsearch">
 Song name: <input type=text name="name">
 Song detail: <select name='detail'>
     <option value='primary_genre_name' >genre</option>
     <option value='track_name'>track name</option>
     <option value='track_censored_name'>track censored name</option>
     <option value='track_view_url'>track url</option>
     <option value='preview_url'>preview url</option>
     <option value='artwork_url_30'>icon url 30px</option>
     <option value='artwork_url_60'>icon url 60px</option>
     <option value='artwork_url_100'>icon url 100px</option>
     <option value='artwork_url_512'>icon url 512px</option>
     <option value='collection_name'>album name</option>
     <option value='track_price'>track price</option>
     <option value='release_date'>release date</option>
     <option value='track_time'>track time</option>
     <option value='country'>country</option>
     <option value='currency'>currency</option>
     <option value='copyright'>copyright</option>
     <option value='price'>price</option>
     </select>
 <input type=submit name=press value="OK">
 </form>
</body>

</html>
"""


@app.route('/musicsearch')
def api_musicsearch():
#Here are the endpoints with api from the first task
    try:
        if 'name' in request.args and 'detail' in request.args:
            track = itunesmusicsearch.search_track(request.args['name'])
            track = track[0]

            if 'primary_genre_name' == request.args['detail']:
                return request.args['detail'] + ': ' + track.primary_genre_name

            if 'track_name' == request.args['detail']:
                return request.args['detail'] + ': ' + track.track_name

            if 'track_censored_name' == request.args['detail']:
                return request.args['detail'] + ': ' + track.track_censored_name

            if 'track_view_url' == request.args['detail']:
                return request.args['detail'] + ': ' + track.track_view_url

            if 'preview_url' == request.args['detail']:
                return request.args['detail'] + ': ' + track.preview_url

            if 'artwork_url_30' == request.args['detail']:
                return request.args['detail'] + ': ' + track.artwork_url_30

            if 'artwork_url_60' == request.args['detail']:
                return request.args['detail'] + ': ' + track.artwork_url_60

            if 'artwork_url_100' == request.args['detail']:
                return request.args['detail'] + ': ' + track.artwork_url_100

            if 'artwork_url_512' == request.args['detail']:
                return request.args['detail'] + ': ' + track.artwork_url_512

            if 'collection_name' == request.args['detail']:
                return request.args['detail'] + ': ' + track.collection_name

            if 'track_price' == request.args['detail']:
                return request.args['detail'] + ': ' + str(track.track_price)

            if 'release_date' == request.args['detail']:
                return request.args['detail'] + ': ' + track.release_date

            if 'track_explicitness' == request.args['detail']:
                return request.args['detail'] + ': ' + track.track_explicitness

            if 'track_time' == request.args['detail']:
                return request.args['detail'] + ': ' + str(track.track_time)

            if 'country' == request.args['detail']:
                return request.args['detail'] + ': ' + track.country

            if 'currency' == request.args['detail']:
                return request.args['detail'] + ': ' + track.currency

            if 'copyright' == request.args['detail']:
                return request.args['detail'] + ': ' + track.copyright

            if 'price' == request.args['detail']:
                return request.args['detail'] + ': ' + str(track.price)

        else:
            return 'Not found'
    except LookupError:
        return 'Not found: ' + request.args['name']
    except AttributeError:
        return '"' + request.args['name'] + '" - ' + ' has no attribute ' + request.args['detail']


if __name__ == '__main__':
    app.run()