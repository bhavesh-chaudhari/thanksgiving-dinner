__doc__ = """An object oriented solution to the problem."""


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class FamilyMember(Person):
    def __init__(self, name):
        self.name = name


def is_attendee_a_family_member(attendee):
    return isinstance(attendee, FamilyMember)


def get_solution(attendees, family_members):
    # head is always an attendee
    attendees_who_are_family_members = [family_members[0]]
    attendees_who_are_guests = []
    for attendee in attendees:
        if is_attendee_a_family_member(attendee):
            attendees_who_are_family_members.append(attendee)
        else:
            attendees_who_are_guests.append(attendee)

    # family members who are not attendees
    family_members_who_are_not_attendees = []
    for member in family_members:
        # the below if condition is a bit complicated and
        # relies again on family members' names being unique

        # check if the "name" of the family member is present in the "names" of the attendees who are family members
        # hence the "member.name" and "x.name" in the below line
        if member.name not in [x.name for x in attendees_who_are_family_members]:
            family_members_who_are_not_attendees.append(member)

    return (
        attendees_who_are_family_members,
        family_members_who_are_not_attendees,
        attendees_who_are_guests,
    )


if __name__ == "__main__":
    # # Example 1:
    # family_members = [
    #     "head",
    #     "member 1",
    #     "member 2",
    #     "member 3",
    #     "member 4",
    #     "member 5",
    # ]
    # attendees = ["member 1", "guest 1", "member 2", "member 5", "guest 5"]

    # # here the family members and attendees are still "STRING" objects.
    # # let's change that with relevant object type

    # family_members = [FamilyMember(x) for x in family_members]
    # # print(family_members)
    # # print([x.name for x in family_members])

    # attendees = [
    #     FamilyMember("member 1"),
    #     Person("guest 1"),
    #     FamilyMember("member 2"),
    #     FamilyMember("member 5"),
    #     Person("guest 5"),
    # ]

    # # print(attendees)
    # # print([(type(x).__name__, x.name) for x in attendees])

    # Example 2"
    family_members = ["Judy", "Jack", "Jessy", "David", "Gloria"]
    attendees = [
        "Jack",
        "David",
        "Judy",
    ]

    family_members = [FamilyMember(x) for x in family_members]
    # this part is somewhat ugly, have to manually create the "types" from names here
    attendees = [FamilyMember("Jack"), FamilyMember("David"), Person("Judy")]

    a, b, c = get_solution(attendees, family_members)

    print("i", a)
    print("ii", b)
    print("iii", c)
