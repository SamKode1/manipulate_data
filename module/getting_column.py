import data_to_csv
import graph

def get_column():
   reader = data_to_csv.read_csv("/home/samkodde/curso_comprehension_python/final_challenge/world_population.csv")
   reader = list(filter(lambda x : x["Continent"] == "Oceania",reader))

   country = list(map(lambda x: x["Country/Territory"],reader))
   population = list(map(lambda x:x ["World Population Percentage"],reader))

   graph.create_pie_chart(country,population)

if __name__ == '__main__':
   get_column()