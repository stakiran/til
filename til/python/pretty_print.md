# Python で pretty print

## dict

```
# Pretty Print Person
def ppp(person):
    import pprint
    print('{}({})'.format(person.name, person.id))
    pprint.pprint(person.parameters)
```
