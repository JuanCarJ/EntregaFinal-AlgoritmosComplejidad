def isPalindrome(x):
        S = str(x)
        if S == S[::-1]:
            return True
        else:
            return False
x = 121
result = isPalindrome(x)
print("El numero", x, "es palindromo:", result)
