from scripts.validations import validate_row

# Test avec une ligne valide
row_valide = {
    "identifiant_document": "000001",
    "valeur_fonciere": "329500,00",
    "date_mutation": "03/01/2024",
    "code_commune": "01173"
}
print(validate_row(row_valide))  # Devrait retourner (True, None)

# Test avec un prix vide
row_invalide = {
    "identifiant_document": "000001",
    "valeur_fonciere": "",
    "date_mutation": "03/01/2024",
    "code_commune": "01173"
}
print(validate_row(row_invalide))