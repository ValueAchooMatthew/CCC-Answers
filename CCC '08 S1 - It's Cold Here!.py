temperatures = []
cities = []


while True:
    city, temperature  = input().split()
    temperatures.append(int(temperature))
    cities.append(city)

    if city == "Waterloo":
        break

minTemp = min(temperatures)

print(cities[temperatures.index(minTemp)])
