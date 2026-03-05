class Vehicle:
    def __init__(self, brand, model):
        if not brand or not model:
            raise ValueError("Brand dan model tidak boleh kosong")

        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)

        if doors <= 0:
            raise ValueError("Jumlah pintu harus lebih dari 0")

        self.doors = doors

    def honk(self):
        print("Beep! Beep!")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)

        if load_capacity <= 0:
            raise ValueError("Kapasitas muatan harus lebih dari 0")

        self.load_capacity = load_capacity

    def load(self, weight):
        try:
            if weight > self.load_capacity:
                raise ValueError("Beban melebihi kapasitas truk")
            print(f"Loaded {weight} kg.")

        except ValueError as e:
            print("Error:", e)


def main():
    try:
        my_car = Car("Toyota", "Corolla", 4)
        my_truck = Truck("Ford", "F-150", 1000)

        my_car.drive()
        my_car.honk()

        my_truck.drive()
        my_truck.load(1200)

    except ValueError as e:
        print("Terjadi error:", e)


if __name__ == "__main__":
    main()