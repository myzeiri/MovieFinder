def html_print(movie_list):
    file = open("../html/output.html", "w")
    file.write("<html>")
    file.write("<head>")
    file.write("<title>Movies out soon</title>")
    for m in movie_list:
        file.write("<h1>Title: " + m.original_title + "</h1>")
        file.write("<h2>Release Date: " + m.opening_date + "</h2>")
        if (m.genre == "genre"):
            file.write("<h2>Genre: genre unavailable</h2>")
        else:
            file.write("<h2>Genre: " + m.genre + "</h2>")
        if (m.rating == "rating"):
            file.write("<h2>Rating: rating unavailable</h2>")
        else:
            file.write("<h2>Rating: " + m.rating + "</h2>")
        file.write("<br><br>")
    file.write("</head>")
    file.write("</html>")
    file.close()
