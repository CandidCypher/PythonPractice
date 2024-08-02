# Requirements
# Create a 'SuperList' class that inherits from a standard list
# Override the __len__ method to always return 1000


class SuperList(list):
    """
    Info: SuperList class that is an extension of the standard list class
    """

    def __len__(self):
        return 1000
    