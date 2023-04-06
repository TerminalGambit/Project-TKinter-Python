import tkinter as tk

piece_selectionnee = None
position_selectionnee = (0, 0)

def sur_clic_canvas(event):
    global piece_selectionnee, position_selectionnee

    colonne = event.x // taille_carreau
    ligne = event.y // taille_carreau

    if piece_selectionnee:
        # Si une pièce est déjà sélectionnée, essayez de la déplacer vers la case cliquée
        deplacer_piece(ligne, colonne)
        piece_selectionnee = None
    else:
        # Si aucune pièce n'est sélectionnée, essayez de sélectionner une pièce sur la case cliquée
        piece = pieces_initial[ligne][colonne]
        if piece:
            mettre_en_evidence_case(ligne, colonne)
            piece_selectionnee = piece
            position_selectionnee = (ligne, colonne)

def deplacer_piece(ligne, colonne):
    global pieces_initial

    # Retirer la pièce de sa position initiale
    ligne_initiale, colonne_initiale = position_selectionnee
    pieces_initial[ligne_initiale][colonne_initiale] = None

    # Placer la pièce à la nouvelle position
    pieces_initial[ligne][colonne] = piece_selectionnee

    # Mettre à jour l'affichage de l'échiquier
    canvas.delete("piece")
    creer_pieces()
    canvas.delete("mise_en_evidence")



def mettre_en_evidence_case(ligne, colonne):
    canvas.delete("mise_en_evidence") # p. 194
    couleur = "yellow"
    canvas.create_rectangle(
        colonne * taille_carreau,
        ligne * taille_carreau,
        (colonne + 1) * taille_carreau,
        (ligne + 1) * taille_carreau,
        outline=couleur,
        width=3,
        tags="mise_en_evidence"
    )

def creer_echiquier():
    for ligne in range(taille_echiquier):
        for colonne in range(taille_echiquier):
            couleur = couleur_echiquier_1 if (ligne + colonne) % 2 == 0 else couleur_echiquier_2
            canvas.create_rectangle(
                colonne * taille_carreau,
                ligne * taille_carreau,
                (colonne + 1) * taille_carreau,
                (ligne + 1) * taille_carreau,
                fill=couleur,
                outline=""
            )

def creer_pieces():
    for ligne in range(len(pieces_initial)):
        for colonne in range(len(pieces_initial[ligne])):
            piece = pieces_initial[ligne][colonne]
            if piece:
                canvas.create_text(
                    colonne * taille_carreau + taille_carreau // 2,
                    ligne * taille_carreau + taille_carreau // 2,
                    text=piece,
                    font=("Arial", 24),
                    tags="piece"
                )

# Constantes
taille_echiquier = 8
taille_carreau = 60
couleur_echiquier_1 = "#DDB88C"
couleur_echiquier_2 = "#A66D4F"

pieces_initial2 = [
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
    ["♙"] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ["♟"] * 8,
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
]
pieces_initial = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟"] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
    ["♙"] * 8,
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
]

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu d'échecs")

# Création du canvas
canvas = tk.Canvas(fenetre, width=taille_echiquier * taille_carreau, height=taille_echiquier * taille_carreau)
canvas.pack()

# Dessin de l'échiquier et des pièces
creer_echiquier()
creer_pieces()

# Liaison d'événement pour les clics sur le canvas
canvas.bind("<Button-1>", sur_clic_canvas) # p. 26

# Lancement de la boucle principale
fenetre.mainloop()
