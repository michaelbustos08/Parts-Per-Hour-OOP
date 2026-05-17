import csv

class Product:
    def __init__(self, name, cycle_time, machine_count):
        self.name = name
        self.cycle_time = cycle_time
        self.machine_count = machine_count

    def __str__(self):
        return f"Name: {self.name} | {self.machine_count} Machines | {self.calculate()} "

    @property
    def cycle_time(self):
        return self._cycle_time
    
    @cycle_time.setter
    def cycle_time(self, cycle_time):
        if cycle_time <= 0:
            raise ValueError("Cycle time cannot be less than 0!")
        self._cycle_time = cycle_time
    
    
    def calculate(self):
        _ = (60 / self.cycle_time) * 60 
        return  _ * self.machine_count

def main():
    products = []
    while True:
        name = input("Name (Type 'quit' to quit): ").strip().lower()
        if name == 'quit':
            break
        machine_count = int(input("How many machines: "))
        cycle_time = int(input("Seconds per cycle: "))
        thing = Product(name, machine_count, cycle_time)
        products.append(thing)
        break
    with open("file.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Machine Count", "Cycle Time", "Parts per Hour"])
        writer.writerow({
            "Name": thing.name,
            "Machine Count": thing.machine_count,
            "Cycle Time": thing.cycle_time,
            "Parts per Hour": round(thing.calculate())
        })
        print(thing)

main()