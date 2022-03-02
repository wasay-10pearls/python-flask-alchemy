from error_class import ChasisNumberNotValid


class Car:
    def __init__(self, _model: int, _car: str):
        self._model = _model
        self._car = _car


    def __repr__(self):
        return(
            f"Car model is {self._model} and color is {self.color}"
        )

    def isCorolla(self, chassis: int):
        if (chassis<=0):
            raise ChasisNumberNotValid(
                f"Chasis cant be 0 or less"
            )
            print("Car is corolla")
        else:
         print("any other car")


car = Car(0, "white")
try:
    car.isCorolla(0)
except ChasisNumberNotValid as e:
    print(e)

    