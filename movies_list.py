movies_list = [
    {"id": 1, 
     "title": "The Matrix", 
     "year": 1999,
    "overview": "A hacker discovers a dystopian world hidden within the real one.",
    "rating": 8.7},

    {"id": 2, 
     "title": "Inception", 
     "year": 2010,
    "overview": "A skilled thief enters the dreams of others to steal secrets.", "rating": 8.8},

    {"id": 3, "title": "Interstellar", 
     "year": 2014,
    "overview": "A team of explorers travel through a wormhole in space.", 
    "rating": 8.6},

    {"id": 4, "title": "The Dark Knight", "year": 2008,
    "overview": "Batman faces the Joker in a struggle for Gotham's soul.", 
    "rating": 9.0},
    
    {"id": 5, "title": "Pulp Fiction", "year": 1994,
    "overview": "The lives of two mob hitmen, a boxer, and others intertwine.", 
    "rating": 8.9},

    {"id": 6, "title": "The Lord of the Rings: The Return of the King", 
     "year": 2003,
    "overview": "The final battle for Middle-earth begins.", 
    "rating": 8.9},

    {"id": 7, "title": "Fight Club", 
     "year": 1999,
    "overview": "An insomniac office worker forms a fight club.", 
    "rating": 8.8},

    {"id": 8, "title": "Forrest Gump", 
     "year": 1994,
    "overview": "The story of a man who witnesses and influences pivotal events.", 
    "rating": 8.8},

    {"id": 9, "title": "The Shawshank Redemption", 
     "year": 1994,
    "overview": "Two imprisoned men bond over several years.", 
    "rating": 9.3},

    {"id": 10, "title": "Gladiator", 
     "year": 2000,
    "overview": "A betrayed Roman general seeks vengeance.", 
    "rating": 8.5},

    {"id": 11, "title": "The Godfather", 
     "year": 1972,
    "overview": "The aging patriarch of a crime dynasty transfers control.", 
    "rating": 9.2},

    {"id": 12, "title": "The Silence of the Lambs", 
     "year": 1991,
    "overview": "A young FBI agent seeks the help of a cannibalistic serial killer.", 
    "rating": 8.6},

    {"id": 13, "title": "Schindler's List", 
     "year": 1993,
    "overview": "A businessman saves hundreds of Jews during the Holocaust.", 
    "rating": 9.0},

    {"id": 14, "title": "The Prestige", 
     "year": 2006,
    "overview": "Two magicians engage in a battle of wits and deception.", 
    "rating": 8.5},

    {"id": 15, "title": "Avatar", 
     "year": 2009,
    "overview": "A paraplegic Marine is sent to the moon Pandora.", 
    "rating": 7.8},

    {"id": 16, "title": "Star Wars: Episode IV - A New Hope", 
     "year": 1977,
    "overview": "A young farm boy embarks on an adventure to defeat an empire.", 
    "rating": 8.6},

    {"id": 17, "title": "The Avengers", 
     "year": 2012,
    "overview": "Earth's mightiest heroes must stop an alien invasion.", 
    "rating": 8.0},

    {"id": 18, "title": "Jurassic Park", 
     "year": 1993,
    "overview": "A theme park full of dinosaurs turns deadly.", 
    "rating": 8.1},

    {"id": 19, "title": "Saving Private Ryan", 
     "year": 1998,
    "overview": "A group of soldiers go on a mission to save one man during WWII.", 
    "rating": 8.6},

    {"id": 20, "title": "The Lion King", 
     "year": 1994,
    "overview": "A young lion prince is cast out of his pride and must find his way back.", 
    "rating": 8.5},

    {"id": 21, "title": "The Godfather Part II", 
     "year": 1974,
    "overview": "The early life and career of Vito Corleone is portrayed.", 
    "rating": 9.0},

    {"id": 22, "title": "The Green Mile", 
     "year": 1999,
    "overview": "A death row corrections officer forms a bond with an inmate.", 
    "rating": 8.6},

    {"id": 23, "title": "Se7en", 
     "year": 1995,
    "overview": "Two detectives hunt a serial killer who uses the seven deadly sins.", 
    "rating": 8.6},
    {"id": 24, "title": "The Usual Suspects", 
     "year": 1995,
    "overview": "A sole survivor recounts the twisted events leading up to a crime.", 
    "rating": 8.5},
    {"id": 25, "title": "Braveheart", 
     "year": 1995,
    "overview": "Scottish warrior William Wallace leads his countrymen in rebellion.", 
    "rating": 8.3},

    {"id": 26, "title": "Good Will Hunting", 
     "year": 1997,
    "overview": "A janitor at MIT has a gift for mathematics, but needs help to find direction.", 
    "rating": 8.3},

    {"id": 27, "title": "Memento", 
     "year": 2000,
    "overview": "A man with short-term memory loss attempts to track down his wife's murderer.", 
    "rating": 8.4},

    {"id": 28, "title": "American History X", 
     "year": 1998,
    "overview": "A former neo-nazi skinhead tries to prevent his brother from going down the same path.", 
    "rating": 8.5},

    {"id": 29, "title": "The Departed", 
     "year": 2006,
    "overview": "An undercover cop and a mole in the police attempt to identify each other.", 
    "rating": 8.5},
    {"id": 30, "title": "Whiplash", 
     "year": 2014,
    "overview": "A young drummer struggles under the ruthless training of a perfectionist teacher.", 
    "rating": 8.5},

    {"id": 31, "title": "The Great Dictator", 
     "year": 1940,
    "overview": "Charlie Chaplin plays a satirical version of Hitler.", 
    "rating": 8.5},

    {"id": 32, "title": "Coco", 
     "year": 2017,
    "overview": "A young boy embarks on an extraordinary journey to the Land of the Dead.", 
    "rating": 8.4},

    {"id": 33, "title": "La La Land", 
     "year": 2016,
    "overview": "A jazz musician and an aspiring actress struggle to make it in Los Angeles.", 
    "rating": 8.0},

    {"id": 34, "title": "The Social Network", 
     "year": 2010,
    "overview": "The story behind the creation of Facebook and its early struggles.", 
    "rating": 7.7},

    {"id": 35, "title": "Her", 
     "year": 2013,
    "overview": "A lonely man develops an emotional relationship with an AI operating system.", 
    "rating": 8.0},

    {"id": 36, "title": "The Revenant", 
     "year": 2015,
    "overview": "A frontiersman on a fur trading expedition fights for survival after being mauled by a bear.", 
    "rating": 8.0},

    {"id": 37, "title": "Mad Max: Fury Road", 
     "year": 2015,
    "overview": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler.", 
    "rating": 8.1},

    {"id": 38, "title": "Blade Runner 2049", 
    "year": 2017,
    "overview": "A young blade runner discovers a long-buried secret.", 
    "rating": 8.0},

    {"id": 39, "title": "Logan", 
     "year": 2017,
    "overview": "In a future where mutants are nearly extinct, an aging Logan must protect a young mutant.", 
    "rating": 8.1},

    {"id": 40, "title": "Parasite", 
    "year": 2019,
    "overview": "A poor family schemes to become employed by a wealthy family.", 
    "rating": 8.6}
    
]
