import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.request.URLError:
    print (f'\033[1:31mNão foi possivel acessar o site Pudim\033[m')
except:
    print('\033[1:31mOcorreu um erro inesperado\033[m')
else:
    print(f'\033[1:32mConsegui abrir o site Pudim')