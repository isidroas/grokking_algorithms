you = []
bob = []
alice = []
claire = []
anuj = []
peggy = []
thom = []
jonny = []

graph = [you, bob, alice, claire, anuj, peggy, thom, jonny]
print(graph)
print(type(you))

you.extend([alice, bob, claire])
bob.extend([anuj, peggy])
alice.extend([peggy,])
claire.extend([thom,jonny])


print(graph)
