Supposons avoir fait :

d = pytesseract.image_to_data(img, output_type=Output.DICT)

#### d["level"] :

pour chaque boîte de texte (ou mot) détectée, associe une valeur selon la logique suivante

1.Item with no block_num, paragraph_num, line_num, word_num

2.Item with block_num and with no paragraph_num, line_num, word_num

3.Item with block_num, paragraph_num and with no line_num, word_num

4.Item with block_num, paragraph_num, line_num, and with no word_num

5.Item with all those numbers


#### d["page_num"] :

pour chaque boîte de texte (ou mot) détectée, associe la page du document sur laquelle elle se situe


#### d["block_num]

pour chaque boîte de texte (ou mot) détectée, associe l'identifiant du bloc dans lequel elle se situe


#### d["par_num]

pour chaque boîte de texte (ou mot) détectée, associe l'identifiant du paragraphe dans lequel elle se situe


#### d["line_num"]

pour chaque boîte de texte (ou mot) détectée, associe la ligne à laquelle elle se situe dans le texte


#### **d["word_num"]**

pour chaque boîte de texte (ou mot) détectée, indice du mot que constitue cette boîte dans la phrase qui la contient


#### **d["left"] d["top"] d["width"] d["height"]**

pour chaque boîte de texte (ou mot) détectée, informations sur sa position dans l'image


#### d["conf"]

pour chaque boîte de texte (ou mot) détectée, indice de confiance quant à la véracité de l'information trouvée par l'algorithme (0 à 100)


#### **d["text]**

pour chaque boîte de texte (ou mot) détectée, contenu textuel de la boîte