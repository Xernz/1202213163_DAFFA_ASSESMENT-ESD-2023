def decrypt_chat(chat):
    decrypted_chat = ""
    for char in chat:
        if char.isalpha():  
            if char.isupper():
                decrypted_chat += chr((ord(char) - ord('A') - 5) % 26 + ord('A'))
            else:
                decrypted_chat += chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
        else:
            decrypted_chat += char 
    return decrypted_chat

chat = ["xfqfr bfmdz",
"gjxtp lzj rfz ifkyfw jxi snm",
"gwt, gjxtp qz rfz rfpfs in bfwlty lfp?",
"fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz",
"dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"]

for line in chat:
    print(decrypt_chat(line))
