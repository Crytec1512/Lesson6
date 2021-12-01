import requests

class BasePokemon:
    def __init__(self, name: str):
        self.name = name

    def printer(self):
        print(self.name, self.id, self.height, self.weight)

class Pokemon(BasePokemon):
    def __init__(self, id, name: str, height: int, weight: int) -> None:
            self.name = name
            self.id = id
            self.height = height
            self.weight = weight


class PokeAPI:
    def __init__(self):
        pass

    def get_pokemon(self):
        Poke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.id}').json()
        Pokeid = Poke["name"]
        return Pokeid

    def get_all(self):
        pass

    PokeID = get_pokemon(5)
Poke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.id}').json()
print(Poke["name"])
