#!C:/Program Files/Python37/python.exe

import cgi
import scrapping
import algorithm

form = cgi.FieldStorage()
movie = form.getvalue('movie_name')
reviews = scrapping.getReviews(movie)
sentiment = algorithm.test(reviews)
sent = sentiment[0]
print("Content-type:text/html\r\n\r\n")
html = """\
    <link href="./main.css"/>
    <div id="user-input">
        <form action="">
            <input>
            <input type="submit">
        </form>
    </div>
    <div id="user-reviews">
    <h1 style="text-alignment:center">Movie Review</h1>
    <table border='1'> """
for row in sentiment:
    html = html + "<tr>"
    for col in row:
        html = html + "<td>" + col + "</td>"
    html = html + "</tr>"
html = html + "</table> </div>"

print (html)


