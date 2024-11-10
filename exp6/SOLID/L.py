# L: Liskov Substitution Principle
class Bird:
    def fly(self):
        return "Flying"


class Sparrow(Bird):
    pass  # Inherits fly behavior


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")


def let_bird_fly(bird):
    try:
        print(bird.fly())
    except NotImplementedError as e:
        print(e)


# Using the classes
sparrow = Sparrow()
penguin = Penguin()

let_bird_fly(sparrow)  # Output: Flying
let_bird_fly(penguin)  # Output: Penguins can't fly
