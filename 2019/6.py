class Planet:
    def __init__(self, orbits_planet):
        self.orbits_planet = orbits_planet
    def get_orbits_planet(self):
        return self.orbits_planet
    def set_orbits_planet(self, orbits_planet):
        self.orbits_planet = orbits_planet

with open("input_6.txt", 'r') as f:
    inp = [i.strip("\n").split(')') for i in f.readlines()]
planets = {}
for i in inp:
    if i[0] not in planets:
        planets[i[0]] = Planet(None)
    if i[1] not in planets:
        planets[i[1]] = Planet(planets[i[0]])
    else:
        planets[i[1]].set_orbits_planet(planets[i[0]])

counter = 0
for p in planets.values():
    curr_planet = p
    while curr_planet != None:
        curr_planet = curr_planet.get_orbits_planet()
        counter += 1 if curr_planet != None else 0
print(counter)
