import ninja
import pet

new_pet = pet.Dog("Barney", ["roll over","shake","speak","stay"])
new_ninja = ninja.Ninja("Chris", "Matthews", new_pet)

new_ninja.feed()
new_ninja.walk()
new_ninja.bathe()

new_pet2 = pet.Cat("Tabby", ["none"])
new_ninja2 = ninja.Ninja("Shiloh", "Matthews", new_pet2)

new_ninja2.feed()
new_ninja2.walk()
new_ninja2.bathe()

