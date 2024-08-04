"""
Terminal application for providing providing an average temperature for
a given set of data over days. 
"""

# Requirements
# Terminal application that takes an input of the specified number of days
# then requests the temperatures for thhe specified number of days and then 
# prints the average for the days. 

if __name__ == "__main__":
    num_days = int(input("Please provide the number of days: "))
    temmperatures = []
    for i in range(num_days):
        temmperatures.append(int(input(f"Temperature for day {i+1}: ")))
    print(f"Average temperature for the specified {num_days} days was: {sum(temmperatures)/len(temmperatures)}")
