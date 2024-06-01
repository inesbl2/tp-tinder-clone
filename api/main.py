from flask import Flask, jsonify
import requests
import random
from flask_cors import CORS
apiRoute = "https://randomuser.me/api/?results=20&nat=fr"
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_profile():
    url = apiRoute.format(10)
    personne = requests.get(url).json()
    results = personne.get('results', [])
    peoples= get_attribut(results)
    return jsonify(peoples)


def get_attribut(results :jsonify)-> list :
    list_person=[]
    for personne in results :
        first_name=personne.get('name').get('first')
        last_name=personne.get('name').get('last')
        gender=personne.get('gender')
        age=personne.get('dob').get('age')
        country=personne.get('location').get('country')
        picture=personne.get('picture').get('large')
        descritpion = get_descriptions(first_name, age)
        list_person.append({"name":first_name,"last_name":last_name,"gender":gender,"age":age,"country":country,"url":picture, "description": descritpion})
    return list_person

def get_descriptions(name, age)-> str :
    descriptions = ["Hey there! I'm " + name + ", " + str(age) + ", and always up for a challenge. When I'm not working, you can find me hiking, trying new restaurants, or planning my next big trip. Looking for someone who shares my sense of adventure and loves to laugh",
                    "Coffee fuels my soul. I'm " + name + ", " + str(age) + ", and a self-proclaimed coffee connoisseur. When I'm not sipping on a latte, you can find me reading, practicing yoga, or trying out new brunch spots. Looking for someone who can keep up with my caffeine habit",
                    "Music is my passion. I'm " + name + ", " + str(age) + ", and always on the lookout for new tunes and artists. When I'm not working, you can find me at concerts, music festivals, or jamming out to my favorite playlists. Looking for someone who shares my love for music and good vibes",
                    "Food coma is my love language. I'm " + name + ", " + str(age) + ", and always on the hunt for the best eats in town. When I'm not cooking up a storm, you can find me trying new restaurants, taking foodie pics, or experimenting with new recipes. Looking for someone who loves food as much as I do",
                    "Get lost in a good book with me. I'm " + name + ", " + str(age) + ", and a total bookworm. When I'm not reading, you can find me writing, daydreaming, or planning my next literary adventure. Looking for someone who shares my love for words and wisdom",
                    "Level up with me! I'm " + name + ", " + str(age) + ", and a gamer at heart. When I'm not working, you can find me playing video games, watching esports, or attending gaming events. Looking for someone who shares my love for gaming and good company",
                    "Creativity is my happy place. I'm " + name + ", " + str(age) + ", and an artistic soul. When I'm not working, you can find me painting, drawing, or attending art events. Looking for someone who shares my love for art and self-expression"]
    
    return random.choice(descriptions)


if __name__ == '__main__':
    app.run(debug=True)
    