from flask import Flask, request, render_template

app = Flask(__name__)
books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def formulaire():
    authorfromsearch = request.args.get('author')
    if not authorfromsearch:
        return "Veuillez spécifier un auteur."
    
    for livre in books:
        if livre['author'].lower() == authorfromsearch.lower():
            return f"Livre : {livre['title']} ({livre['year']})"
    
    return "Aucun résultat trouvé."

@app.route('/ajout', methods=['POST'])
def ajout_Livre():
    titre = request.form.get("title")
    auteur = request.form.get("author")
    annee = request.form.get("year")

    # Vérification des champs vides
    if not titre or not auteur or not annee:
        return "Tous les champs (titre, auteur, année) doivent être remplis.", 400

    try:
        annee = int(annee)  # Vérification si l'année est un entier
    except ValueError:
        return "L'année doit être un nombre entier.", 400

    id = len(books) + 1
    books.append({"id": id, "title": titre, "author": auteur, "year": annee})
    return f"Livre ajouté : {titre} par {auteur} ({annee})."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
