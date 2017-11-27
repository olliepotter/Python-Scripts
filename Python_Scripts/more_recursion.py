def list_reverse(n):
    if len(n) == 0:
        return
    else:
        list_reverse(n[1:])
        print(n[0])


print(list_reverse(range(20)))
print(range(20))


def algae(s, n=0):
    """
    Print S rewritten with the algae rule to recursion depth n
    """
    if n == 0:  # Base case
        print(s, end="")
        return
    # General case : transform each symbol in S
    for symbol in s:
        if symbol == "A":
            algae("AB", n - 1)
        else:
            algae("A", n - 1)


def build_algae(s, string, n=0):
    """
    Print S rewritten with the algae rule to recursion depth n
    """
    if n == 0:  # Base case
        string.append(s)
        return
    # General case : transform each symbol in S
    for symbol in s:
        if symbol == "A":
            build_algae("AB",string, n - 1)
        else:
            build_algae("A", string, n - 1)

list = []
build_algae("A", list,5)
print(list)