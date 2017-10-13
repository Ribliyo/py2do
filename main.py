import sqlib

if __name__ == '__main__':
    command = {'A': 'add', 'V': 'view', 'D': 'del', 'U': 'do'}
    while True:
        cmd = raw_input("your wish: ")
        if cmd in command:
            cmd = command[cmd]
        elif cmd in command.values():
            pass
        else:
            print 'wrong input. quit!'
            break

    # sqlib.add('test')
    # sqlib.get()