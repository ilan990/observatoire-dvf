from mappings import DVF_COLUMN_MAPPING
from validations import validate_row
from database import insert_rows
from datetime import datetime

def ingest_dvf(data):
    batch = []
    total = 0
    
    with open(data, 'r') as f:
        header = f.readline()

        for line in f:  
            line = line.strip()
            if not line: 
                continue
            
            line_parse = parse_line(line, header)
            line_parse["is_valid"], line_parse["reject_reason"] = validate_row(line_parse)

            batch.append(line_parse)
            if len(batch) == 1000:
                insert_rows(batch)
                total += len(batch)
                print(f"✅ {total} lignes insérées")
                batch = [] 
                
        if len(batch) > 0:
            insert_rows(batch)
            total += len(batch)
            print(f"✅ Total final : {total} lignes")

def parse_line(line, headers):
    headers_array = headers.strip().split('|')
    line_array = line.strip().split('|')
    dico = {}
    
    for i in range(len(headers_array)):
        dico[DVF_COLUMN_MAPPING[headers_array[i]]] = line_array[i]
    
    # Nettoyer les DECIMAL
    numeric_fields = [
        'valeur_fonciere',
        'surface_carrez_lot_1',
        'surface_carrez_lot_2',
        'surface_carrez_lot_3',
        'surface_carrez_lot_4',
        'surface_carrez_lot_5',
        'surface_reelle_bati',
        'surface_terrain'
    ]
    
    for field in numeric_fields:
        if dico[field]:
            dico[field] = dico[field].replace(',', '.')
        else:
            dico[field] = None
    
    # Nettoyer les INT
    int_fields = ['nombre_de_lots', 'nombre_pieces_principales']
    for field in int_fields:
        if not dico[field]:
            dico[field] = None
    
    # Convertir la date
    if dico['date_mutation']:
        try:
            date_obj = datetime.strptime(dico['date_mutation'], '%d/%m/%Y')
            dico['date_mutation'] = date_obj.strftime('%Y-%m-%d')
        except ValueError:
            dico['date_mutation'] = None
    else:
        dico['date_mutation'] = None

    return dico

ingest_dvf("ValeursFoncieres-2024.txt")