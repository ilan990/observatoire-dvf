from scripts.validations import validate_row


def test_ligne_valide():
    row = {
        "identifiant_document": "000001",
        "valeur_fonciere": "329500,00",
        "date_mutation": "03/01/2024",
        "code_commune": "01173"
    }
    is_valid, error = validate_row(row)
    assert is_valid == True
    assert error is None

def test_prix_vide():
    row = {
        "identifiant_document": "000001",
        "valeur_fonciere": "",
        "date_mutation": "03/01/2024",
        "code_commune": "01173"
    }
    is_valid, error = validate_row(row)
    assert is_valid == False
    assert error is not None

def test_prix_negatif():
    row = {
        "identifiant_document": "000001",
        "valeur_fonciere": "-5",
        "date_mutation": "03/01/2024",
        "code_commune": "01173"
    }
    is_valid, error = validate_row(row)
    assert is_valid == False
    assert error is not None

def test_date_invalide():
    row = {
        "identifiant_document": "000001",
        "valeur_fonciere": "329500,00",
        "date_mutation": "03-01-2024",
        "code_commune": "01173"
    }
    is_valid, error = validate_row(row)
    assert is_valid == False
    assert error is not None

def test_code_commune_court():
    row = {
        "identifiant_document": "000001",
        "valeur_fonciere": "329500,00",
        "date_mutation": "03/01/2024",
        "code_commune": "073"
    }
    is_valid, error = validate_row(row)
    assert is_valid == False
    assert error is not None   