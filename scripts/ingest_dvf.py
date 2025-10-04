from mappings import DVF_COLUMN_MAPPING
def ingest_dvf(data):
    with open(data, 'r') as f:
        # for i in range(3):
        #     print(f.readline())
        header = f.readline()
        line = f.readline()
        result = parse_line(line,header)
        print(result)


def parse_line(line, headers):
    headers_array = headers.strip().split('|')
    line_array = line.strip().split('|')
    dico = {}
    for i in range(len(headers_array)):
        dico[DVF_COLUMN_MAPPING[headers_array[i]]] = line_array[i]
    return dico


ingest_dvf("ValeursFoncieres-2024.txt")