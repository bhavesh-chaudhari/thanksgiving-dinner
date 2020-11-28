__doc__ = """An object oriented solution to the problem."""


class Person:
    def __init__(self, name):
        self.name = name


class FamilyMember(Person):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # Example 1:
    family_members = [
        "head",
        "member 1",
        "member 2",
        "member 3",
        "member 4",
        "member 5",
    ]
    attendees = ["member 1", "guest 1", "member 2", "member 5", "guest 5"]

    # here the family members and attendees are still "STRING" objects.
    # let's change that with relevant object type

    family_members = [
        FamilyMember(x) for x in family_members
    ]
    print(family_members)
    print([x.name for x in family_members])

    attendees = [
        FamilyMember("member 1"),
        Person("guest 1"),
        FamilyMember("member 2"),
        FamilyMember("member 5"),
        Person("guest 5")
    ]

    print(attendees)
    print([(type(x).__name__, x.name) for x in attendees])