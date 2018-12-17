from tomorrow import threads
@threads(100)
def run():
    n = 10000000
    for i in range(n):
        if i >n:
            print('ok')
run()
