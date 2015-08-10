#Import the required media and fresh_tomatoes modules
import media
import fresh_tomatoes

#Create 12 movie instances using the Movie class contained in the media module
avatar = media.Movie("Avatar","2009","PG-13",
                      "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                      "James Cameron","Sam Worthington, Zoe Saldana, Sigourney Weaver",
                      "../images/avatar.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
the_departed = media.Movie("The Departed","2006","R",
                      "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
                      "Martin Scorsese","Leonardo DiCaprio, Matt Damon, Jack Nicholson",
                      "../images/the_departed.jpg","https://www.youtube.com/watch?v=SGWvwjZ0eDc")
crash = media.Movie("Crash","2004","R",
                      "Los Angeles citizens with vastly separate lives collide in interweaving stories of race, loss and redemption.",
                      "Paul Haggis","Don Cheadle, Sandra Bullock, Thandie Newton",
                      "../images/crash.jpg","https://www.youtube.com/watch?v=durNwe9pL0E")
titanic = media.Movie("Titanic","1997","PG-13",
                      "A seventeen-year-old aristocrat falls in love with a kind, but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "James Cameron","Leonardo DiCaprio, Kate Winslet, Billy Zane",
                      "../images/titanic.jpg","https://www.youtube.com/watch?v=zCy5WQ9S4c0")
the_matrix = media.Movie("The Matrix","1999","R",
                      "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                      "The Wachowski Brothers","Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                      "../images/the_matrix.jpg","https://www.youtube.com/watch?v=m8e-FF8MsqU")
safe_house = media.Movie("Safe House","2012","R",
                      "A young CIA agent is tasked with looking after a fugitive in a safe house. But when the safe house is attacked, he finds himself on the run with his charge.",
                      "Daniel Espinosa","Denzel Washington, Ryan Reynolds, Robert Patrick",
                      "../images/safe_house.jpg","https://www.youtube.com/watch?v=1IfQY4fNcnw")
iron_man = media.Movie("Iron Man","2008","PG-13",
                      "After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight evil.",
                      "John Favreau","Robert Downey Jr., Gwyneth Paltrow, Terrence Howard",
                      "../images/iron_man.jpg","https://www.youtube.com/watch?v=8hYlB38asDY")
the_avengers = media.Movie("The Avengers","2012","PG-13",
                      "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                      "Joss Whedon","Robert Downey Jr., Chris Evans, Scarlett Johansson",
                      "../images/the_avengers.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")
robocop = media.Movie("RoboCop","2014","PG-13",
                      "In 2028 Detroit, when Alex Murphy - a loving husband, father and good cop - is critically injured in the line of duty, the multinational conglomerate OmniCorp sees their chance for a part-man, part-robot police officer.",
                      "Jose Padilha","Joel Kinnaman, Gary Oldman, Michael Keaton",
                      "../images/robocop.jpg","https://www.youtube.com/watch?v=jBeSfnIT_Bw")
inception = media.Movie("Inception","2010","PG-13",
                      "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                      "Christopher Nolan","Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
                      "../images/inception.jpg","https://www.youtube.com/watch?v=66TuSJo4dZM")
gladiator = media.Movie("Gladiator","2000","R",
                      "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                      "Ridley Scott","Russell Crowe, Joaquin Phoenix, Connie Nielsen",
                      "../images/gladiator.jpg","https://www.youtube.com/watch?v=owK1qxDselE")
three_hundred = media.Movie("300","2006","R",
                      "King Leonidas and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
                      "Zack Snyder","Gerard Butler, Lena Headey, David Wenham",
                      "../images/three_hundred.jpg","https://www.youtube.com/watch?v=UrIbxk7idYA")

#Add the 12 movie instances created into a list
movies = [avatar,the_departed,crash,titanic,the_matrix,safe_house,iron_man,the_avengers,robocop,inception,gladiator,three_hundred]

#Call the open_movies_page function contained in the fresh_tomatoes module, passing in the movies list as input
fresh_tomatoes.open_movies_page(movies)
