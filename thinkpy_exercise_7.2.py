def eval_loop():
    while True:
        user = input('evaluate what...')
        eval(user)
        if user == 'done':
            break
        last = eval(user)
        print(last)
    return last 

print(eval_loop())





