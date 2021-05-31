from os import environ

OMDB_API_KEY = '2798667a' if environ.get(
    'OMDB_API_KEY') is None else environ.get('OMDB_API_KEY')

GRID_SIZE = (10, 10)
PLAYER_INIT_POSITION = (0, 0)

START_BALL_AMOUNT = 15

TOTAL_MON_LIST = []

IN_GAME_MON_LIST = []

CAPTURE_MON_LIST = [{'tt0468492': {'title': 'The Host', 'year': '2006', 'director': 'Bong Joon Ho', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTE3N2IwNmMtOGE0Ny00NWFlLTliNmUtNjY3ODExYjgxNmUyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg', 'rating': 7.1, 'plot': "A monster emerges from Seoul's Han River and begins attacking people. One victim's loving family does what it can to rescue her from its clutches.", 'actors': 'Kang-ho Song, Byun Hee-Bong, Park Hae-il, Bae Doona'}, 'tt5034838': {'title': 'Godzilla vs. Kong', 'year': '2021', 'director': 'Adam Wingard', 'poster': 'https://m.media-amazon.com/images/M/MV5BZmYzMzU4NjctNDI0Mi00MGExLWI3ZDQtYzQzYThmYzc2ZmNjXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_SX300.jpg', 'rating': 6.5, 'plot': 'The epic next chapter in the cinematic Monsterverse pits two of the greatest icons in motion picture history against one another - the fearsome Godzilla and the mighty Kong - with humanity caught in the balance.', 'actors': 'Alexander Skarsgård, Millie Bobby Brown, Rebecca Hall, Brian Tyree Henry'}, 'tt0078748': {'title': 'Alien', 'year': '1979', 'director': 'Ridley Scott', 'poster': 'https://m.media-amazon.com/images/M/MV5BMmQ2MmU3NzktZjAxOC00ZDZhLTk4YzEtMDMyMzcxY2IwMDAyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 'rating': 8.4, 'plot': 'After a space merchant vessel receives an unknown transmission as a distress call, one of the crew is attacked by a mysterious life form and they soon realize that its life cycle has merely begun.', 'actors': 'Tom Skerritt, Sigourney Weaver, Veronica Cartwright, Harry Dean Stanton'}, 'tt0087363': {'title': 'Gremlins', 'year': '1984', 'director': 'Joe Dante', 'poster': 'https://m.media-amazon.com/images/M/MV5BZDVjN2FkYTQtNTBlOC00MjM5LTgzMWEtZWRlNGUyYmNiOTFiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 7.3, 'plot': 'A young man inadvertently breaks three important rules concerning his new pet and unleashes a horde of malevolently mischievous monsters on a small town.', 'actors': 'Hoyt Axton, John Louie, Keye Luke, Don Steele'}, 'tt0073195': {'title': 'Jaws', 'year': '1975', 'director': 'Steven Spielberg', 'poster': 'https://m.media-amazon.com/images/M/MV5BMmVmODY1MzEtYTMwZC00MzNhLWFkNDMtZjAwM2EwODUxZTA5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg', 'rating': 8.0, 'plot': "When a killer shark unleashes chaos on a beach community, it's up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.", 'actors': 'Roy Scheider, Robert Shaw, Richard Dreyfuss, Lorraine Gary'}, 'tt8235660': {'title': 'Megalodon', 'year': '2018', 'director': 'James Thomas', 'poster': 'https://m.media-amazon.com/images/M/MV5BNjBlNDUzMzAtMTdkNC00NzZiLWFmYjMtMzYyYjZjZjljY2VmXkEyXkFqcGdeQXVyNDcyOTc1OTk@._V1_SX300.jpg', 'rating': 2.9, 'plot': 'A military vessel on the search for an unidentified submersible finds themselves face to face with a giant shark, forced to use only what they have on board to defend themselves from the monstrous beast.', 'actors': 'Michael Madsen, Caroline Harris, Ego Mikitas, Aimee Stolte'}, 'tt0118615': {'title': 'Anaconda', 'year': '1997', 'director': 'Luis Llosa', 'poster': 'https://m.media-amazon.com/images/M/MV5BZDc4ODcyNWMtMzI2Zi00YzcwLWE4ZTUtYWM3OWI1MTgwYTc1XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_SX300.jpg', 'rating': 4.8, 'plot': 'A "National Geographic" film crew is taken hostage by an insane hunter, who forces them along on his quest to capture the world\'s largest - and deadliest - snake.', 'actors': 'Jennifer Lopez, Ice Cube, Jon Voight, Eric Stoltz'}, 'tt0105643': {'title': 'Troll 2', 'year': '1990', 'director': 'Claudio Fragasso', 'poster': 'https://m.media-amazon.com/images/M/MV5BZmQ4MzZlZTAtNDRhMC00MTQ2LTkyN2YtNTQ1ZTliM2UwMWNhXkEyXkFqcGdeQXVyMTQ2MjQyNDc@._V1_SX300.jpg', 'rating': 3.0, 'plot': "A vacationing family discovers that the entire town they're visiting is inhabited by goblins, disguised as humans, who plan to eat them.", 'actors': 'Michael Paul Stephenson, George Hardy, Margo Prey, Connie Young'}, 'tt1844770': {'title': 'Sand Sharks', 'year': '2012', 'director': 'Mark Atkins', 'poster': 'https://m.media-amazon.com/images/M/MV5BMzg5NjgwNTE0Nl5BMl5BanBnXkFtZTcwNTQ0NzAzOA@@._V1_SX300.jpg', 'rating': 2.6, 'plot': 'The residents of a small town team up to kill a group of evolved sharks that can swim in sand, and are terrorizing local beaches.', 'actors': 'Corin Nemec, Brooke Hogan, Vanessa Evigan, Eric Scott Woods'}, 'tt0329101': {'title': 'Freddy vs. Jason', 'year': '2003', 'director': 'Ronny Yu', 'poster': 'https://m.media-amazon.com/images/M/MV5BODNlNWVjOTMtZjVjYy00MzRjLTg2MmQtNTM3MWVmZjFjYzgwXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_SX300.jpg', 'rating': 5.7, 'plot': "Freddy Krueger and Jason Voorhees return to terrorize the teenagers of Elm Street. Only this time, they're out to get each other, too.", 'actors': 'Robert Englund, Ken Kirzinger, Monica Keena, Jason Ritter'}, 'tt0372873': {'title': 'Dragon Wars: D-War', 'year': '2007', 'director': 'Hyung-rae Shim', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTc2OTk1MzUzMl5BMl5BanBnXkFtZTcwNjE0ODI1MQ@@._V1_SX300.jpg', 'rating': 3.5, 'plot': 'Once in 500 years, ancient mythical creatures come to Earth, wreaking havoc and destruction. This time they must be stopped.', 'actors': 'Jason Behr, Amanda Brooks, Robert Forster, Craig Robinson'}, 'tt1934381': {'title': 'Sector 7', 'year': '2011', 'director': 'Ji-hoon Kim', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTU0MzA0NTc4Nl5BMl5BanBnXkFtZTgwNTQ1MTAzMjE@._V1_SX300.jpg', 'rating': 4.7, 'plot': 'A crew, drilling offshore for oil south of Jeju island, finds a lethal alien life form instead.', 'actors': 'Ha Ji-Won, Sung-Ki Ahn, Ji-Ho Oh, Ye-ryeon Cha'}, 'tt1270797': {'title': 'Venom', 'year': '2018', 'director': 'Ruben Fleischer', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_SX300.jpg', 'rating': 6.7, 'plot': 'A failed reporter is bonded to an alien entity, one of many symbiotes who have invaded Earth. But the being takes a liking to Earth and decides to protect it.', 'actors': 'Tom Hardy, Michelle Williams, Riz Ahmed, Scott Haze'}, 'tt3967856': {'title': 'Okja', 'year': '2017', 'director': 'Bong Joon Ho', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjQxMTcxNDgxN15BMl5BanBnXkFtZTgwOTczNTIzMjI@._V1_SX300.jpg', 'rating': 7.3, 'plot': 'A young girl risks everything to prevent a powerful, multinational company from kidnapping her best friend - a fascinating beast named Okja.', 'actors': 'Tilda Swinton, Sheena Kamal, Michael Mitton, Colm Hill'}, 'tt10240612': {'title': 'Critters Attack!', 'year': '2019', 'director': 'Bobby Miller', 'poster': 'https://m.media-amazon.com/images/M/MV5BYzIzYTY0N2UtNDI5Ni00OTM4LTkyMTUtMDQ1ODJiMTg2MDRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 3.7, 'plot': 'A reluctant babysitter must protect three kids from an invasion of ravenous critters.', 'actors': 'Tashiana Washington, Ava Preston, Jack Fulton, Jaeden Noel'}, 'tt0406728': {'title': 'Dungeons & Dragons: Wrath of the Dragon God', 'year': '2005', 'director': 'Gerry Lively', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTUzNzg2OTI2Nl5BMl5BanBnXkFtZTgwNzQzODkwMzE@._V1_SX300.jpg', 'rating': 4.7, 'plot': 'Together, four heroes build their own army to retrieve the orb, using elemental forces to defeat Damodar before he summons the sleeping black dragon.', 'actors': 'Bruce Payne, Mark Dymond, Clemency Burton-Hill, Ellie Chidzey'}, 'tt0317676': {'title': 'House of the Dead', 'year': '2003', 'director': 'Uwe Boll', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzlmNTFlN2QtM2IxZi00NDc0LTgyMTQtNDNjNTBmODQzZDVjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 2.0, 'plot': 'A group of college students travels to a mysterious island to attend a rave, which is soon taken over by bloodthirsty zombies.', 'actors': 'Jonathan Cherry, Tyron Leitso, Clint Howard, Ona Grauer'}, 'tt1489946': {'title': 'The Blackout', 'year': '2009', 'director': 'Robert David Sanders', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjg3NzQ1YWItZDY4Ny00OTVhLWI4MTAtOGI1NTNjZTFjMWExXkEyXkFqcGdeQXVyNzMzMjU5NDY@._V1_SX300.jpg', 'rating': 3.3, 'plot': "It's Christmas Eve, the city goes dark, and the few remaining tenants of The Ravenwood find themselves trapped in their building. And they are not alone.", 'actors': 'Barbara Streifel Sanders, Joseph Dunn, Ian Malcolm, Michael Caruso'}, 'tt1714203': {'title': 'Piranha 3DD', 'year': '2012', 'director': 'John Gulager', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjAzMzY4NTk0M15BMl5BanBnXkFtZTcwMDA4ODU3Nw@@._V1_SX300.jpg', 'rating': 3.7, 'plot': 'After the events at Lake Victoria, the pre-historic school of blood-thirsty piranhas make their way into a newly opened waterpark.', 'actors': 'Danielle Panabaker, Matt Bush, Katrina Bowden, Jean-Luc Bilodeau'}, 'tt5639976': {'title': 'The Mist', 'year': '2017', 'director': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BMzE3MDk0ODkwM15BMl5BanBnXkFtZTgwMzA5NTk5MTI@._V1_SX300.jpg', 'rating': 5.4, 'plot': 'After an eerie mist rolls into a small town, the residents must battle the mysterious mist and its threats, fighting to maintain their morality and sanity.', 'actors': 'Morgan Spector, Alyssa Sutherland, Gus Birney, Danica Curcic'}, 'tt6644200': {'title': 'A Quiet Place', 'year': '2018', 'director': 'John Krasinski', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_SX300.jpg', 'rating': 7.5, 'plot': 'In a post-apocalyptic world, a family is forced to live in silence while hiding from monsters with ultra-sensitive hearing.', 'actors': 'Emily Blunt, John Krasinski, Millicent Simmonds, Noah Jupe'}, 'tt0198781': {'title': 'Monsters, Inc.', 'year': '2001',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'director': 'Pete Docter, David Silverman(co-director), Lee Unkrich(co-director)', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTY1NTI0ODUyOF5BMl5BanBnXkFtZTgwNTEyNjQ0MDE@._V1_SX300.jpg', 'rating': 8.1, 'plot': 'In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, two monsters realize things may not be what they think.', 'actors': 'John Goodman, Billy Crystal, Mary Gibbs, Steve Buscemi'}, 'tt0091064': {'title': 'The Fly', 'year': '1986', 'director': 'David Cronenberg', 'poster': 'https://m.media-amazon.com/images/M/MV5BODcxMGMwOGEtMDUxMi00MzE5LTg4YTYtYjk1YjA4MzQxNTNlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 'rating': 7.6, 'plot': 'A brilliant but eccentric scientist begins to transform into a giant man/fly hybrid after one of his experiments goes horribly wrong.', 'actors': 'Jeff Goldblum, Geena Davis, John Getz, Joy Boushel'}, 'tt4680182': {'title': 'Colossal', 'year': '2016', 'director': 'Nacho Vigalondo', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTY2NTExOTA2MF5BMl5BanBnXkFtZTgwNTMwMjE2MTI@._V1_SX300.jpg', 'rating': 6.2, 'plot': 'Gloria is an out-of-work party girl forced to leave her life in New York City and move back home. When reports surface that a giant creature is destroying Seoul, she gradually comes to the realization that she is somehow connected to this phenomenon.', 'actors': 'Anne Hathaway, Jason Sudeikis, Austin Stowell, Tim Blake Nelson'}, 'tt2231461': {'title': 'Rampage', 'year': '2018', 'director': 'Brad Peyton', 'poster': 'https://m.media-amazon.com/images/M/MV5BNDA1NjA3ODU3OV5BMl5BanBnXkFtZTgwOTg3MTIwNTM@._V1_SX300.jpg', 'rating': 6.1, 'plot': 'When three different animals become infected with a dangerous pathogen, a primatologist and a geneticist team up to stop them from destroying Chicago.', 'actors': 'Dwayne Johnson, Naomie Harris, Malin Akerman, Jeffrey Dean Morgan'}, 'tt0100814': {'title': 'Tremors', 'year': '1990', 'director': 'Ron Underwood', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTEzNjkwMzIyMjZeQTJeQWpwZ15BbWU4MDI2NTU5ODYx._V1_SX300.jpg', 'rating': 7.1, 'plot': 'Natives of a small isolated town defend themselves against strange underground creatures which are killing them one by one.', 'actors': 'Kevin Bacon, Fred Ward, Finn Carter, Michael Gross'}, 'tt5688868': {'title': 'Primal Rage: The Legend of Konga', 'year': '2018', 'director': 'Patrick Magee', 'poster': 'https://m.media-amazon.com/images/M/MV5BNjc5MjUyZTctNGQ1YS00ZTkyLWJmMDktZWNjNjcyNjU3MjU0XkEyXkFqcGdeQXVyNzc0MTgzMzU@._V1_SX300.jpg', 'rating': 4.9, 'plot': "A newly reunited young couple's drive through the Pacific Northwest turns into a nightmare as they are forced to face nature, unsavory locals, and a monstrous creature, known to the Native Americans as Oh-Mah.", 'actors': 'Casey Gagliardi, Andrew Joseph Montgomery, Jameson Pazak, Marshal Hilton'}, 'tt4374286': {'title': 'Monstrum', 'year': '2018', 'director': 'Jong-ho Huh', 'poster': 'https://m.media-amazon.com/images/M/MV5BN2IyOTdhOTQtNTkyYy00OWU1LWE1OGYtMzBkZGQ5YmI0YjQ5XkEyXkFqcGdeQXVyNDcyMjQ4MzU@._V1_SX300.jpg', 'rating': 6.1, 'plot': "Yoon Gyeom is a loyal subject of King Jung Jong of Joseon. He struggles to fight against a monster that threatens King Jung Jong's life and a group of people trying to depose King Jung Jong.", 'actors': 'Myung-Min Kim, In-kwon Kim, Hyeri Lee, Woo-sik Choi'}, 'tt0069005': {'title': 'Night of the Lepus', 'year': '1972', 'director': 'William F. Claxton', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjM5NTk3N2EtNGZkMy00NTdhLWE0NGQtZDhkNzA4NjJjNWNiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 4.2, 'plot': 'Giant mutant rabbits terrorize the south-west.', 'actors': 'Stuart Whitman, Janet Leigh, Rory Calhoun, DeForest Kelley'}, 'tt0100260': {'title': 'Nightbreed', 'year': '1990', 'director': 'Clive Barker', 'poster': 'https://m.media-amazon.com/images/M/MV5BMmFlMWFiM2ItNWQ1Yy00ZDE2LWEzNmUtOTE0MDM4YjVjNmYxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 6.5, 'plot': 'A troubled young man is drawn to a mythical place called Midian where a variety of friendly monsters are hiding from humanity. Meanwhile, a sadistic serial killer is looking for a patsy.', 'actors': 'Craig Sheffer, Anne Bobby, David Cronenberg, Charles Haid'}, 'tt0089469': {'title': 'Legend', 'year': '1985', 'director': 'Ridley Scott', 'poster': 'https://m.media-amazon.com/images/M/MV5BYTAxZmQ4YzktNTI3Yi00MjgzLTg0YzMtODdmMWVmODUzNjJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SX300.jpg', 'rating': 6.5, 'plot': 'A young man must stop the Lord of Darkness from destroying daylight and marrying the woman he loves.', 'actors': 'Tom Cruise, Mia Sara, Tim Curry, David Bennent'}, 'tt0055894': {'title': 'Invasion of the Triffids', 'year': '1963', 'director': 'Steve Sekely, Freddie Francis', 'poster': 'https://m.media-amazon.com/images/M/MV5BY2U3NDcxM2UtYTE2Ny00OWEzLTgyZmUtZTliOTVhMDM5N2U0XkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SX300.jpg', 'rating': 6.2, 'plot': 'After an unusual meteor shower leaves most of the human population blind, a merchant navy officer must find a way to conquer tall, aggressive plants which are feeding on people and animals.', 'actors': 'Howard Keel, Nicole Maurey, Janette Scott, Kieron Moore'}, 'tt1396484': {'title': 'It', 'year': '2017', 'director': 'Andy Muschietti', 'poster': 'https://m.media-amazon.com/images/M/MV5BZDVkZmI0YzAtNzdjYi00ZjhhLWE1ODEtMWMzMWMzNDA0NmQ4XkEyXkFqcGdeQXVyNzYzODM3Mzg@._V1_SX300.jpg', 'rating': 7.3, 'plot': 'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.', 'actors': 'Jaeden Martell, Jeremy Ray Taylor, Sophia Lillis, Finn Wolfhard'}, 'tt0065163': {'title': 'The Valley of Gwangi', 'year': '1969', 'director': "Jim O'Connolly", 'poster': 'https://m.media-amazon.com/images/M/MV5BYWNlNjk0MTAtMjExYi00Yjc4LWEyNzEtZjlkYjllNjNkMzliXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 6.3, 'plot': 'A cowboy named Tuck Kirby seeks fame and fortune by capturing an Allosaurus living in the Forbidden Valley and putting it in a Mexican circus. His victim, called the Gwangi, turns out to have an aversion to being shown in public.', 'actors': 'James Franciscus, Gila Golan, Richard Carlson, Laurence Naismith'}, 'tt0090190': {'title': 'The Toxic Avenger', 'year': '1984', 'director': 'Michael Herz, Lloyd Kaufman', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzViNmQ5MTYtMmI4Yy00N2Y2LTg4NWUtYWU3MThkMTVjNjk3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 6.3, 'plot': 'Tromaville has a monstrous new hero. The Toxic Avenger is born when meek mop boy Melvin falls into a vat of toxic waste. Now evildoers will have a lot to lose.', 'actors': 'Andree Maranda, Mitch Cohen, Jennifer Babtist, Cindy Manion'}, 'tt0084745': {'title': 'Swamp Thing', 'year': '1982', 'director': 'Wes Craven', 'poster': 'https://m.media-amazon.com/images/M/MV5BYWNjMTZiM2YtMDkwOS00ZmJhLThmNzItZjFhMjEyZDliM2Y5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 5.4, 'plot': 'After a violent incident with a special chemical, a research scientist is turned into a swamp plant monster.', 'actors': 'Louis Jourdan, Adrienne Barbeau, Ray Wise, David Hess'}, 'tt0457430': {'title': "Pan's Labyrinth", 'year': '2006', 'director': 'Guillermo del Toro', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTU3ODg2NjQ5NF5BMl5BanBnXkFtZTcwMDEwODgzMQ@@._V1_SX300.jpg', 'rating': 8.2, 'plot': 'In the Falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world.', 'actors': 'Ivana Baquero, Sergi López, Maribel Verdú, Doug Jones'}, 'tt0093177': {'title': 'Hellraiser', 'year': '1987', 'director': 'Clive Barker', 'poster': 'https://m.media-amazon.com/images/M/MV5BOGRlZTdhOGYtODc5NS00YmJkLTkzN2UtZDMyYmRhZWM1NTQwXkEyXkFqcGdeQXVyMzU4Nzk4MDI@._V1_SX300.jpg', 'rating': 7.0, 'plot': 'A woman discovers the newly resurrected, partially formed, body of her brother-in-law. She starts killing for him to revitalize his body so he can escape the demonic beings that are pursuing him after he escaped their sadistic underworld.', 'actors': 'Andrew Robinson, Clare Higgins, Ashley Laurence, Sean Chapman'}, 'tt0083907': {'title': 'The Evil Dead', 'year': '1981', 'director': 'Sam Raimi', 'poster': 'https://m.media-amazon.com/images/M/MV5BODc2MmVjZmUtNjAzMS00MDNiLWIyM2YtOGEzMjg0YjRhMzRmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'rating': 7.5, 'plot': 'Five friends travel to a cabin in the woods, where they unknowingly release flesh-possessing demons.', 'actors': 'Bruce Campbell, Ellen Sandweiss, Richard DeManincor, Betsy Baker'}, 'tt5884052': {'title': 'Pokémon Detective Pikachu', 'year': '2019', 'director': 'Rob Letterman', 'poster': 'https://m.media-amazon.com/images/M/MV5BNDU4Mzc3NzE5NV5BMl5BanBnXkFtZTgwMzE1NzI1NzM@._V1_SX300.jpg', 'rating': 6.6, 'plot': 'In a world where people collect Pokémon to do battle, a boy comes across an intelligent talking Pikachu who seeks to be a detective.', 'actors': 'Ryan Reynolds, Justice Smith, Kathryn Newton, Bill Nighy'}, 'tt3794354': {'title': 'Sonic the Hedgehog', 'year': '2020', 'director': 'Jeff Fowler', 'poster': 'https://m.media-amazon.com/images/M/MV5BMDk5Yzc4NzMtODUwOS00NTdhLTg2MjEtZTkzZjc0ZWE2MzAwXkEyXkFqcGdeQXVyMTA3MTA4Mzgw._V1_SX300.jpg', 'rating': 6.5, 'plot': 'After discovering a small, blue, fast hedgehog, a small-town police officer must help him defeat an evil genius who wants to do experiments on him.', 'actors': 'Ben Schwartz, James Marsden, Jim Carrey, Tika Sumpter'}, 'tt7504864': {'title': 'The Mask', 'year': '2017', 'director': 'Jason Gerbay', 'poster': 'https://m.media-amazon.com/images/M/MV5BMWY5MjM3MmQtNmMzNi00ODc1LTg1YjAtMTgyYjRkZGNlOTk3XkEyXkFqcGdeQXVyMTQ0MzMwNQ@@._V1_SX300.jpg', 'rating': 5.3, 'plot': "After the events of the the first movie, Stanley Ipkiss has a daughter. The daughter finds the mask in Stanley's room and starts wearing it! It is so spooky and scary that the police try to...", 'actors': 'Jamie Summers, Cody Anderson, Annie Landkammer, J.G. Busse'}, 'tt1415872': {'title': 'Digimon X-Evolution', 'year': '2005', 'director': 'Hiroyuki Kakudo', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTU0ZGNjN2MtNjE2MC00NmYxLTljZjgtNzQ5NGUwYjVhYWM4XkEyXkFqcGdeQXVyNjM2Njk3NDc@._V1_SX300.jpg', 'rating': 6.6, 'plot': 'A virtual world was created called the "Digital World" and the "Digital Monster" was born. However, it developed the X Program of fear to eliminate all Digimon in the old world and develop a new Digital World for only certain Digimon.', 'actors': 'Doug Erholtz, Hiroaki Hirata, Akira Ishida, Kokoro Kikuchi'}, 'tt7904362': {'title': 'Conjuring the Devil', 'year': '2020', 'director': 'Max Dementor', 'poster': 'https://m.media-amazon.com/images/M/MV5BMzM0MjY0YzItMjAwOS00MDdmLWJiM2UtZjQ2MmI0N2UwMDI5XkEyXkFqcGdeQXVyMTA0Mzg1Mjg@._V1_SX300.jpg', 'rating': 1.7, 'plot': 'A woman who is struggling with the conflict between her faith and her personal life must defend herself against the spirit of a demonic nun who is bent on destroying her.', 'actors': 'April Love, Maria de Jesus Castellon, Johnny Stevenson, Darren Barcomb'}, 'tt1788453': {'title': 'The Amazing Bulk', 'year': '2012', 'director': 'Lewis Schoenbrun', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTQ2OTYwMzQwNl5BMl5BanBnXkFtZTgwMzc1NjkyNDE@._V1_SX300.jpg', 'rating': 1.7, 'plot': "Henry 'Hank' Howard works as a scientist in a military lab, trying to create a superhuman formula but with little success. He is also in love with the daughter of his boss, a general. In an...", 'actors': 'Terence Lording, Shevaun Kastl, Randal Malone, Juliette Angeli'}}]

IMDB_LIST = [
    "tt0468492",
    "tt5034838",
    "tt0078748",
    "tt0087363",
    "tt0073195",
    "tt8235660",
    "tt0118615",
    "tt0105643",
    "tt1844770",
    "tt0329101",
    "tt0372873",
    "tt1934381",
    "tt1270797",
    "tt3967856",
    "tt10240612",
    "tt0406728",
    "tt0317676",
    "tt1489946",
    "tt1714203",
    "tt5639976",
    "tt6644200",
    "tt0198781",
    "tt0091064",
    "tt4680182",
    "tt2231461",
    "tt0100814",
    "tt5688868",
    "tt4374286",
    "tt0069005",
    "tt0100260",
    "tt0089469",
    "tt0055894",
    "tt1396484",
    "tt0065163",
    "tt0090190",
    "tt0084745",
    "tt0457430",
    "tt0093177",
    "tt0083907",
    "tt5884052",
    "tt3794354",
    "tt7504864",
    "tt1415872",
    "tt7904362",
    "tt1788453",
]
