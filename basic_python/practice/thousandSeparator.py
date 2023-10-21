def thousandSeparator(n: int):
    n_list = list(a for a in str(n))
    m = 0
    for i in range(3, len(n_list), 3):
        n_list.insert(-i-m, ".")
        m += 1
    n_str = "".join(n_list)
    return n_str


print(thousandSeparator(1))
