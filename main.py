name = 'Vasiliy'
x = 10
y = 15


def testF(a, b):
    if a < b:
        name = 'Cocol'
    else:
        name = name
    return name


print(testF(5, 3))