def decrypt(encrypted_text, n):
    counter = 0
    string = ''
    if n == 0:
        return encrypted_text
    elif encrypted_text is None:
        return None
    else:
        if n > 0:
            while n != 0:
                if len(encrypted_text) % 2 == 0:
                    for i in range(len(encrypted_text)):
                        string += encrypted_text[(len(encrypted_text) // 2) + i]
                        string += encrypted_text[i]
                        counter += 1
                        if counter == len(encrypted_text) // 2:
                            counter = 0
                            break
                else:
                    for j in range(len(encrypted_text)):
                        string += encrypted_text[(len(encrypted_text) // 2) + j]
                        string += encrypted_text[j]
                        counter += 1
                        if counter == len(encrypted_text) // 2:
                            counter = 0
                            break
                    string += encrypted_text[-1]
                n -= 1
                encrypted_text = string
                string = ''
            return encrypted_text
        else:
            return encrypted_text


def encrypt(text, n):
    string = ''
    if n == 0:
        return text
    elif text is None:
        return None
    else:
        if n > 0:
            while n != 0:
                for i in range(len(text)):
                    if i % 2 == 1:
                        string += text[i]
                if len(string) == len(text) // 2:
                    for j in range(len(text)):
                        if j % 2 == 0:
                            string += text[j]
                n -= 1
                text = string
                string = ''
            return text
        else:
            return text

