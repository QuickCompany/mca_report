individual_hindu_undivided_family = {
        'indian' : [] ,
        'non-resident_Indian_(NRI)': [] ,
        'Foreign_national_(other_than_NRI)' : []
    }

def parse_share_holding():
    pass

def parse_string(value_element):
    desired_value = value_element
    object_element = desired_value.getparent()  # Get the parent element
    dict_elements = object_element.findall('.//string')
    if len(dict_elements) >= 5:
        return dict_elements[-1].text
    else:
        return None

def parse_table(value_element):

    desired_value = value_element
    object_element = desired_value.getparent()
    dict_elements = object_element.findall('.//string')

    if len(dict_elements) >= 5:
        return dict_elements[-1].text

    else:
        return None


def directors_data(table):
    directors_table = []
    for i in range(0,len(table),5):
        d = {}
        d['name'] = table[i]
        d['din/pan'] = table[i+1]
        d['designation'] = table[i+2]
        d['number_of_equity_shares_hold'] = table[i+3]
        d['date_of_cessation'] = table[i+4]

        directors_table.append(d)

    return directors_table