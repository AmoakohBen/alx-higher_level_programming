#!/usr/bin/python3

"""Define a locked class"""


Class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    from anything but attributes called 'first_name'.
    """

    __slot__ =["first_name"]
