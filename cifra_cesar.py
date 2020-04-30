class Cesar:
    def __init__(self):
        self._alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def decrypt(self, encrypted_text, key):
        deciphered_text = ''
        encrypted_text = encrypted_text.lower()
        for character in encrypted_text:
            if character in self._alphabet:
                index = self._alphabet.find(character) - key
                deciphered_text += self._alphabet[index]
            else:
                deciphered_text += character
        return deciphered_text