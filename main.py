import re

f = open('biblio.bib', 'r', encoding='utf8')
input_string = f.read()
matches = [item for item in re.split(r'@', input_string) if not re.fullmatch(r'\s+', item)] # Создание коллекции строк из книжек
matches.pop(0) # Удаление ненужной информации
pattern = re.compile(r'(?P<key>\w+)\s+=\s{\s?(?P<value>[^}]+)}')
for item in matches:
    dictionary = dict(pattern.findall(item)) # Создание словаря
    author = re.sub("[ ,]and", ",", dictionary.get("Author").replace('\n', '') + ' ') if dictionary.get("Author") else "" # Проверка наличия автора и форматирование
    title = dictionary['Title'].replace('\n', '') + ' ' # Название книги
    journal = "// " + dictionary["Journal"].replace('\n', '') + ".- " if dictionary.get("Journal") else ""
    year = dictionary["Year"] + ".- " if dictionary.get("Year") else ""
    vol = "Vol. " + dictionary["Volume"] + ".- " if dictionary.get("Volume") else ""
    pages = "P. " + dictionary["Pages"] + ". " if dictionary.get("Pages") else ""
    doi = "DOI: " + re.sub(r':|\..+', '', dictionary["File"]) if dictionary.get("File") else ""
    print(f'{author}{title}{journal}{year}{vol}{pages}{doi}')