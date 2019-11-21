def format_string_list(string_list):
    
    new_string_list = []
    
    if len(string_list) > 0:
        
        for string in string_list:
            new_string = string.replace(',', '').encode("utf-8","ignore")
            new_string_list.append(new_string.decode("utf-8", "ignore"))
        
        new_string_list = list(filter(None,new_string_list)) 
        
        return new_string_list

    else: 
        return string_list



def get_value_tostring(data, key):
    return str(data[key])

def get_value_tolist(data,key):
    return list(data[key])
