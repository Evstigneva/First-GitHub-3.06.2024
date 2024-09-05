a=int(input())
s=int(input())
def f(a):
    def d(s):
        s+=123
        return s
    a+=s
    return d
print(f(a))