import json


def load_data(filepath):
    json_file_utf8 = open(filepath, encoding="utf8")
    json_file_utf8_content = json.load(json_file_utf8)
    json_file_utf8.close()
    return json_file_utf8_content

def get_collection(json_file_utf8_content):
    s=[]
    k=0
    for i in json_file_utf8_content["features"]:
        s.append(json_file_utf8_content["features"][k]["properties"]["Attributes"]["SeatsCount"])
        k=k+1
    print (s)
    print(max(s))
    x=0
    for x in range(len(s)):
            if max(s)==s[x]:
                print(x)
                z=x
    #print(json_file_utf8_content["features"][z])
    return json_file_utf8_content["features"][z]

def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


def pretty_print_json(json_file_utf8_content):
    print(json.dumps(json_file_utf8_content, indent=4, ensure_ascii=False, sort_keys=True))

if __name__ == '__main__':
    pretty_print_json(get_collection(load_data('C:/Users/galinov.ea/Documents/GitHub/etc/3_bars/bars_cut.json')))



##import json
##
##with open('C:/Users/galinov.ea/Documents/GitHub/etc/3_bars/bars_cut.json',  encoding="utf8") as data_file:    
##    data = json.load(data_file)
##    print(data["features"][1]["geometry"]["coordinates"])
