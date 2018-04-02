import media
import fresh_tomatoes

x_men = media.Movie(
    "X_Men: Dark Phoenix",
    "Mystique, Beast, Storm, Nightcrawler and the rest of the X-Men spring into action when a malevolent, power-hungry force threatens to overtake Jean Grey's mind.",
    "https://image.tmdb.org/t/p/w600_and_h900_bestv2/6qmsupE0opYPIaBGe7T5D2FBzLs.jpg",
    "https://youtu.be/uup2JFXH68g"
     )
Dr_strange = media.Movie(
    "Dr. Strange",
    "After his career is destroyed, a brilliant but arrogant surgeon gets a new lease on life when a sorcerer takes him under his wing and trains him to defend the world against evil.",
    "https://image.tmdb.org/t/p/w185_and_h278_bestv2/4PiiNGXj1KENTmCBHeN6Mskj2Fq.jpg",
    "https://www.youtube.com/watch?v=C4K7Nze9kmU"
    )
Life_of_Pi = media.Movie(
    "LIfe of Pi",
    "The story of an Indian boy named Pi, a zookeeper's son who finds himself in the company of a hyena, zebra, orangutan, and a Bengal tiger after a shipwreck sets them adrift in the Pacific Ocean.",
    'https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg',
    "https://youtu.be/j9Hjrs6WQ8M"
)
Time_Bandits = media.Movie(
    "Time Bandits",
    "Young history buff Kevin can scarcely believe it when six dwarfs emerge from his closet one night. Former employees of the Supreme Being, they've purloined a map charting all of the holes in the fabric of time and are using it to steal treasures from different historical eras. Taking Kevin with them, they variously drop in on Napoleon, Robin Hood and King Agamemnon before the Supreme Being catches up with them.",
    "https://upload.wikimedia.org/wikipedia/en/8/82/Time_bandits.jpg",
    "https://youtu.be/JwnjENpIyq0"
)

Ready_player_one = media.Movie(
    "Ready player one",
    "When the creator of a popular video game system dies, a virtual contest is created to compete for his fortune.",
    "https://image.tmdb.org/t/p/w600_and_h900_bestv2/pU1ULUq8D3iRxl1fdX2lZIzdHuI.jpg",
    "https://youtu.be/cSp1dM2Vj48"
)

Jumanji_welcome_to_the_Jungle = media.Movie(
    "Jumanji: welcome to the Jungle",
    "The tables are turned as four teenagers are sucked into Jumanji's world - pitted against rhinos, black mambas and an endless variety of jungle traps and puzzles. To survive, they'll play as characters from the game.",
    "https://image.tmdb.org/t/p/w600_and_h900_bestv2/bXrZ5iHBEjH7WMidbUDQ0U2xbmr.jpg",
    "https://youtu.be/2QKg5SZ_35I"
)


# print(doctor.storyline)
movies = [x_men, Dr_strange, Time_Bandits, Life_of_Pi, Ready_player_one, Jumanji_welcome_to_the_Jungle]
fresh_tomatoes.open_movies_page(movies)

