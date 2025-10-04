from datetime import datetime

def validate_prix(valeur_fonciere):
    if valeur_fonciere is None or valeur_fonciere == "":
        return False, "prix_vide"
    try:
        prix = float(valeur_fonciere.replace(',', '.'))
        if prix <= 0:
            return False, "mauvais_prix"
    except (ValueError, TypeError):
        return False, "prix_invalide"
    return True, None

def validate_date(date):
    if date is None or date == "":
        return False, "date_vide"
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return False, "format_date"
    return True, None
  
def validate_code_commune(code_commune):
    if code_commune is None or code_commune == "":
        return False, "code_commune_vide"
    return True, None

def validate_row(row):
    
    # Valider le prix (obligatoire)
    is_valid, reason = validate_prix(row.get("valeur_fonciere"))
    if not is_valid:
        return False,reason

    # Valider la date (obligatoire)
    is_valid, reason = validate_date(row.get('date_mutation'))
    if not is_valid:
        return False, reason

    # Valider le code de la commune (obligatoire)
    is_valid, reason = validate_code_commune(row.get('code_commune'))
    if not is_valid:
        return False, reason    


    return True, None