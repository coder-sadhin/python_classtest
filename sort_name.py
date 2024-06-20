def sort_name(lst):
    return sorted(lst, key=lambda x: (len(x.split()[-1]), x.lower()))

vla=[
    "jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Micole Yoder",
    "Melissa Hoffman"
]
print(sort_name(vla))

