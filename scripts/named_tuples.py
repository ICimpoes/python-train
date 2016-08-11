from collections import namedtuple

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])

bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])

print(bob)
print(bob._asdict())
print('age - {0}. name = {1} jobs {2}'.format(bob.age, bob.name, bob.jobs))
