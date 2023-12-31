def is_palindrome(s):

    s = s.replace(" ", "").lower()

    # Membandingkan dengan kebalikan dari string
    return s == s[::-1]

# Meminta input dari pengguna
user_input = input("Masukkan kata atau kalimat: ")

# Menentukan apakah input pengguna adalah palindrom atau tidak
result = "eureeka!" if is_palindrome(user_input) else "suka blyat"

# Menampilkan hasil
print(f"{result}")
