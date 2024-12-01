class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


# test = ClassTest()
# test.instance_method()
# ClassTest.class_method() # clas method don't need an instance to be called
# ClassTest.static_method()


class Car:
    TYPES = ("Sedan", "SUV", "Hatchback")

    def __init__(self, brand_name, model_name, car_type, car_color):
        self.brand_name = brand_name
        self.model_name = model_name
        self.car_type = car_type
        self.car_color = car_color

    def __repr__(self):
        return f"<Brand: {self.brand_name}, Model: {self.model_name}, Type: {self.car_type} Color: {self.car_color}>"

    @classmethod
    def show_car_type(cls, brand_name, model_name, car_color):
        return cls(brand_name, model_name, cls.TYPES[1], car_color)

    @staticmethod
    def is_valid_type(car_type):
        return car_type in Car.TYPES


car = Car.show_car_type("Toyota", "Corolla", "Black")
print(car)

print(Car.is_valid_type("SUV"))
