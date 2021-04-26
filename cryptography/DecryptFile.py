from cryptography.fernet import Fernet

key = "9dDB2TVbDNtNPXFV2lRA9be2JdUL-eto9AizsyIB5-g="

# system_information_e = 'e_system.txt'
# clipboard_information_e = 'e_clipboard.txt'
keys_information_e = 'e_keys_logged.txt'



encrypted_files = [ keys_information_e]
count = 0


for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        if count == 2:
            print("sjdhf")
        
        f.write(decrypted +  bytes(0))
    

    count += 1