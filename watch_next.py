# a program to take a selection of films and use spacy to find which of the films is similar to 
# a description of another film

# import spacy
import spacy

# load specific language model 'MD'
nlp = spacy.load('en_core_web_md')


# function which takes films listed in a text file and finds the similarity to a seperate film description
def next_movie(description):

    comparable_film = nlp(description)

    # open and prepare info in movies txt file 
    with open('movies.txt', 'r') as file:
        other_movies = [line.strip() for line in file.readlines()]

        # holding lists for the films once split and compared
        similar_list = []
        similar_list_desc = []

        for sentence in other_movies:
                similarity = nlp(sentence).similarity(comparable_film)
                str_sim = (str(similarity))
                str_desc = (str(sentence))
                similar_list_desc.append(str_desc)
                similar_list.append(str_sim)
                best_match_film = max(similar_list)
                rounded_best_match_film = (best_match_film[2:4])
                best_match_film_index = similar_list.index(best_match_film)

    # returns the film with the highest similarity amount plus an added % match            
    return (f'{similar_list_desc[best_match_film_index]} {rounded_best_match_film}% Match.')


# here is the movie which has just been watched and will be compared with the list
# this could also be a description input by the user
original_movie = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator'
            
print("We recommend your next film to watch based on previous should be: " + next_movie(original_movie))

# end of program