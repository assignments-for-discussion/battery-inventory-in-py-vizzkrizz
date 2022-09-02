def count_batteries_by_usage(cycles):
    #Initializing the count of all batteries to zero in a dictionary.
    dict_battery={
        "lowCount":0,
        "mediumCount":0,
        "highCount":0
    }
    #Parsing through cycles[list] to check how many times the battery has been charged.
    for charged in cycles:                                   
        if charged >= 0 and charged < 400:
            dict_battery["lowCount"] += 1      
        elif charged >= 400 and charged < 920:            #920 is not included in this elif
            dict_battery["mediumCount"] += 1
        else:
            dict_battery["highCount"] += 1               
         
    return dict_battery
    
def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n")
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  print(counts)
  assert(counts["lowCount"] == 2)
  
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
