
class Rocket:
    def __init__(self, name, height, engine_count, fuel_type):
        self.name = name
        self.height = height
        self.engine_count = engine_count
        self.fuel = fuel_type

    def spec_sheet(self):
        print(f'The {self.name} stands at {self.height} tall.\nIt has {self.engine_count} engines and uses {self.fuel} fuel.')

    def __str__(self):
        return f'The {self.name} stands at {self.height} tall.\nIt has {self.engine_count} engines and uses {self.fuel} fuel.'

Delta_IV = Rocket(name="Delta IV Heavy", height="72m",engine_count="3",fuel_type="Liquid")

print(Delta_IV)