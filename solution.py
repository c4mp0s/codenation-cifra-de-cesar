import cifra_cesar as cifra
import requests_api as requests
import hashlib
import json


class Solution():
    def __init__(self, token):
        self._requests = requests.Requests(token)
        self._cifra_cesar = cifra.Cesar()

    @staticmethod
    def write_file(text):
        with open('answer.json', 'w', encoding='utf8') as file:
            json.dump(text, file)
            file.close()

    @staticmethod
    def sha1_encryption(text):
        text_sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
        return text_sha1

    def solve(self):
        try:
            response = self._requests.get()
            unencrypted_text = self._cifra_cesar.decrypt(
                response['cifrado'], response['numero_casas'])
            response['decifrado'] = unencrypted_text
            response['resumo_criptografico'] = self.sha1_encryption(
                unencrypted_text)
            self.write_file(response)
            print(self._requests.post())
        except:
            print('Error when performing the solution')


def main():
    token = input('Informe seu token: ')
    Solution(token).solve()


if __name__ == "__main__":
    main()
