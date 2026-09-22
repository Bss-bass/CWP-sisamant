def array_of_names(persons):
    names = []
    for first_name, last_name in persons.items():
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        names.append(first_name + " " + last_name)
    return names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
