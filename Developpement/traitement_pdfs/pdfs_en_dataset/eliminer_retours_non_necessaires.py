def eliminer_retours_non_necessaires(texte):
    lignes = texte.split('\n')
    nouveau_texte = []
    buffer = []

    for ligne in lignes:
        if ligne.strip():
            buffer.append(ligne.strip())
        else:
            if buffer:
                nouveau_texte.append(' '.join(buffer))
                buffer = []
            nouveau_texte.append('')

    if buffer:
        nouveau_texte.append(' '.join(buffer))

    return '\n'.join(nouveau_texte)

def modifier_fichier(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()

    nouveau_contenu = eliminer_retours_non_necessaires(contenu)

    with open(fichier, 'w', encoding='utf-8') as f:
        f.write(nouveau_contenu)

fichier = 'D:\\Cours\\Cycle_ingénieur\\proj104_artishow\\hnapp\\Developpement\\traitement_pdfs\\manuels_et_cours\\test.txt' 
modifier_fichier(fichier)
print(f'Le fichier "{fichier}" a été modifié avec succès.')
