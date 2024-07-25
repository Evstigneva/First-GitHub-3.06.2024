a={
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}
a1=0
a2=0
s=input()
for i in a:
    if s in a[i]:
        a1+=1
    else:
        a1+=0
if a1>=1:
    print(f'INFO: {s} is a city in {i}')
else:
    print(f'ERROR: Country for {s} not found')