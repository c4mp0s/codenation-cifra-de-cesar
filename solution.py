import cifra_cesar as cifra
import requests_api as requests
import hashlib
import json

class Solution():
    def __init__(self,token):
        self._requests = requests.Requests(token)
        self._cifra_cesar = cifra.Cesar() 

    def write_file(self, text):
        file = open('answer.json','w', encoding='utf8')
        json.dump(text, file)
        file.close()
    
    def read_file(self):
        file = open('answer.json','r', encoding='utf8')
        data = json.load(file)
        file.close()
        return data
    
    def sha1_encryption(self,text):
        text_sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
        return text_sha1


def main():
    token = input('Informe seu token: ')
    solution = Solution(token)
    response = solution._requests.get()
    unencrypted_text = solution._cifra_cesar.decrypt(response['cifrado'], response['numero_casas'])
    response['decifrado'] = unencrypted_text
    response['resumo_criptografico'] = solution.sha1_encryption(unencrypted_text)
    solution.write_file(response)
    print(solution._requests.post())

if __name__ == "__main__":
    main()