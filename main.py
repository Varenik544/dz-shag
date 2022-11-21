result = []


def divider(a, b):
    try:
        if a < b:
            result.append(res)
        if b > 100:
            result.append(res)
        if type(a) == "str":
            result.append(res)
        if b == 0:
            raise ZeroDivisionError
    except IndexError:
        print('Index Error')
    except ValueError:
        print('Value Error')
    except TypeError:
        print('Type Error')
        return
    except ZeroDivisionError:
        print('Zero Division Error')
        return
    return a/b


data = {10: 2, 2: 5, "123": 4, 18: 0, '[]': 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)

class Counter:
    def init(self, max_number):
        self.i = 0
        self.max_number = max_number

    def iter(self):
        self.i = 0
        return self

    def next(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


def generator(count):
    i = 0
    for i in count:
        yield i
    return i

count = Counter(10)
# for i in count:
#     print(i, end = ' ')
res = generator(count)


print(res.next())
print(res.next())
print(res.next())
print(res.next())