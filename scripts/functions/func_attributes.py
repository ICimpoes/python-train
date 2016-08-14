def mem_state(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = mem_state(0)

F('F - xxx')

F('F - xxx2')


H = mem_state(44)


H('H - xxx')

F('F - xxx3')

H('H - xxx1')

H('H - xxx2')

F('F - xxx1')

H.state = 9999

H('H - xxx3')

print(F.state)
print(H.state)
