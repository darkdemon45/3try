def my():
    yield "yo"
    yield "2"
    yield "end"
b=my()
print(next(b))
print(next(b))
print(next(b))