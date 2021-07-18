"""
Check if an element in list begins with string
Print, return result
"""
# ........................................................ Main Function
def does_start_with(L,trigger,l):
    for i in L:
        if i.startswith(trigger):
            l.append(i)
    print("".join(l))
    return l
# ........................................................ On Run, Export
if __name__ == "__main__":
    does_start_with(L=["world","wide","spider","web","network"],trigger ="net", l=[])

