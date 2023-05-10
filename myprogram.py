from typing import Optional
import logging

class Person:
  """
  Represent a person in python
  """
  def __init__(self, firstname, lastname, age):
    """
    Initialize a person with firstname, lastname and age
    """
    self.firstname = firstname
    self.lastname = lastname
    self.age = age


def average_age(persons: Optional[list[Person]]) -> Optional[int]:
    """
    Compute the average age of the list of persons
    """
    if persons:
        try:
            all_ages = list(map(lambda p: p.age, persons))
            return sum(all_ages) / len(all_ages)
        except Exception:
            logging.error("error happened when computing the average")
            return None
    return None
    print("computing all ages done")
  
p1 = Person("John", "Doe", 51)
p2 = Person("Luke", "Skywalker", 21)
list_of_persons = [p1, p2]
print("Average age")
print(average_age(list_of_persons))
