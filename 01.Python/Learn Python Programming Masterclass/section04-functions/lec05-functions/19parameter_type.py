def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword: ... {}, {}".format(p1, p2))
    print("var-positional: .......... {}".format(args))
    print("keyword: ................. {}".format(k))
    print("var-keyword: ............. {}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=8, key2=8)
print("*******************************")
func(1, 2, 3, 4, 5, 9, 11, k=6, key1=8, key2=8)

# TypeError: func() missing 1 required keyword-only argument: 'k'
# func(1, 2, 3, 4, 5, 9, 11, key1=8, key2=8)
