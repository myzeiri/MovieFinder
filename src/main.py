from get_movies import scrape_movies, create_movie_list
from html_print import html_print

print("Welcome to the Gateway Film Scraper. Please wait while we download the upcoming movies.")

# Get the movie information
scraped_movies = scrape_movies()
print("Getting movie information...")
movie_list = create_movie_list(scraped_movies)

users_picks = []
#testing
# Get user's commands
choice = 0
while choice != 4:
    print("\nEnter the genres you are interested in seperated by commas. Or enter \"All\" for every movie.")
    genres_input = input()
    genres = genres_input.split(",")

    if genres_input == "All":
        users_picks = movie_list
    else:
        for m in movie_list:
            for g in genres:
                if g in m.genre:
                    users_picks.append(m)
                    break

    print("Choose print location: (1) Terminal, (2) HTML, (3) Both, (4) Quit")
    choice = int(input())

    if choice == 1 or choice == 3:
        for m in users_picks:
            m.prettyPrint()
    if choice == 2 or choice == 3:
        html_print(users_picks)
