def my_args(*args, name):
    # print(args, name)
    for i in args:
        print(i, name)
    return args, name


savant_args, something = my_args(1, 2, 3, 4, 5, 6, name='vasanth')
print(savant_args)
print(something)
