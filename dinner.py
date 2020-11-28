__doc__ = """A simple program to learn Python."""


def is_attendee_a_family_member(attendee, family_members):
    return attendee in family_members


if __name__ == "__main__":
    family_members = [
        "head",
        "member 1",
        "member 2",
        "member 3",
        "member 4",
        "member 5",
    ]
    attendees = ["member 1", "guest 1", "member 2", "member 5", "guest 5"]

    # keep track of family members
    attendees_who_are_family_members = ["head"] # head is by default an attendee
    
    # keep track of guest with this variable
    attendees_who_are_guests = []
    
    for attendee in attendees:
        if is_attendee_a_family_member(attendee, family_members):
            print("I am a family member:", attendee)
            attendees_who_are_family_members.append(attendee)
        else:
            print("I am a guest:", attendee)
            attendees_who_are_guests.append(attendee)
    
    # so far, we are done with (i) and (iii)

    # how to find members who are NOT attending the thanksgiving dinner party?
    # this means we have to subtract attendees_who_are_family_members from family_members

    # define a variable to track family members who are not attending
    family_members_who_are_not_attending = []
    for member in family_members:
        if member in attendees_who_are_family_members:
            pass
        else:
            family_members_who_are_not_attending.append(member)
    
    print("(i)", attendees_who_are_family_members)
    print("(ii)", family_members_who_are_not_attending)
    print("(iii)", attendees_who_are_guests)