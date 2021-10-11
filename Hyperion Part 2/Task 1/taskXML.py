import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

for movie in root.iter('movie'):
	print(movie.attrib)  # child tags of the movie element

for descrip in root.iter('movie'):
	print("".join(descrip.itertext()))  # prints out the descriptions

# store the elements in a list
movie_list = []
for movie in root.iter('movie'):
	movie_list.append(movie.attrib)

# print(movie_list)

# create empty lists to store favorite and non favorite movies
favorite_movies = []
not_favorite = []

for item in movie_list:
	if item['favorite'] == 'True':
		favorite_movies.append(item)
	else:
		# if favorite movie == False
		not_favorite.append(item)

print(f"Number of favorite movies : {len(favorite_movies)}")
print(f"Number of NON favorite movies: {len(not_favorite)}")





