def group_by_city(scores_dataset):
    cities = {}
    for entries in scores_dataset:
        city = entries["City"]
        name = entries["Name"]  
        if city not in cities:
            cities[city] = []
        
        cities[city].append(name)

    return cities
    
def busy_cities(scores_dataset):
    maxi = 0
    busyc = []
    cities = group_by_city(scores_dataset)
    for city, students in cities.items():
        if len(students) > maxi:
            maxi = len(students)
            busyc = [city]
        elif len(students) == maxi:
            busyc.append(city)

    return busyc