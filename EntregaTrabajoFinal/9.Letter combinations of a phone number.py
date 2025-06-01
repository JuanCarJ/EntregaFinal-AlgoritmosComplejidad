def letterCombinations(digits):
        #Se ingresa en un diccionario las posibles letras que pueden darse al presionar un numero
        letrasCel = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits:
            return []
        result = [""]
        
    # Por cada dígito, se combinan las letras actuales con las letras correspondientes al dígito
        for digito in digits:
            letras = letrasCel[digito]
            result = [actuales + letrasDigitos for actuales in result for letrasDigitos in letras]
        return result
print(letterCombinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']