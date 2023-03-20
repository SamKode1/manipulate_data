import csv 

with open("/home/samkodde/curso_comprehension_python/final_challenge/world_population.csv") as data:
   reader = csv.DictReader(data) # Convert all the data into a dictionary, every item is now a dictionary example => {'Rank': '74', 'CCA3': 'ZWE', 'Country/Territory': 'Zimbabwe', 'Capital': 'Harare', 'Continent': 'Africa', '2022 Population': '16320537', '2020 Population': '15669666', '2015 Population': '14154937', '2010 Population': '12839771', '2000 Population': '11834676', '1990 Population': '10113893', '1980 Population': '7049926', '1970 Population': '5202918', 'Area (km²)': '390757', 'Density (per km²)': '41.7665', 'Growth Rate': '1.0204', 'World Population Percentage': '0.2'}
   population_col = {"2020 Population": []} # we create a new dictorinary with epty list as a value
   for record in reader:
      population_col["2020 Population"].append(record["2020 Population"]) #now we get from every dictionary key called "2020 Population" value and send to our empty list
   
   print(population_col)