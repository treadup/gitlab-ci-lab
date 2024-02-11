"""
This is a trivial python module used to test
different GitLab CI configurations.
"""


def greeting(name):
    """
    Generates a greeting message for the given name.
    """
    return "Hello {}".format(name)


if __name__ == "__main__":
    print(greeting("World"))
