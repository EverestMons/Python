

def draw_stars(lst):
    for i in lst:
        if isinstance(i, str):
            print i[0] * len(i)
        else:
            i = i * "*"
            print i

x = ["joe",4,6,1,3,5,7,25,"tikjgkgm", "year"]
print draw_stars(x)
