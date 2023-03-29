import csv 

def read_csv(path):
   with open(path, "r+") as data:
      reader = csv.reader(data, delimiter=",") # We process data in a csv format, using the parameter delimiter "," as a separator between data and data
      header = next(reader) # using iteratation next() we only reproduce 1 row of the data  and capture it as a header row
      #print(header)
      final_data = [] # then create a epty list waiting for assign the organized data


   # using zip() we can match the first item (header[0]) to the second item (reader[0]), to match in pair key: value with the metod dict().
   #  Finally using append we add all data into a epty list final data

      for row in reader:
         in_pairs = zip(header,row)
         convert_dict = {key: value for key, value in in_pairs}
         final_data.append(convert_dict)
      return final_data
   
if __name__=="__main__":
   read_csv("/home/samkodde/curso_comprehension_python/final_challenge/world_population.csv")
   