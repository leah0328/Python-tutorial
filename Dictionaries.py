# Dictionaries

# whenever we create a dictionaries, 
# always create them inside of curly brackets

jap_conversions={
    "Mon" : "月曜日",
    "Tues" : "火曜日",
    "Wed" : "水曜日",
    "Thurs" : "木曜日",
    "Fri" : "金曜日",
    "Sat" : "土曜日",
    "Sun" : "日曜日",

}

print(jap_conversions.get("Jan","Not a valid key"))