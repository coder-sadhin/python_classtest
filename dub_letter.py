def no_dublicate_letters(txt):
    dub=False
    ts=txt.split(" ")
    for word in ts:
        if(len(set(word)) == len(word)):
            dub=True
    return "True" if dub else "False"

s=input("you can lead a horse to water, but you can't")
print(no_dublicate_letters(s))