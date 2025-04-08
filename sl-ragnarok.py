
#%%
# lista dos capitulos que srão baixados
mangaList = [
    # "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-47/",
    # "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-46/",
    # "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-45/",
    # "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-44/",
    # "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-43/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-42/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-41/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-40/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-39/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-38/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-37/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-36/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-35/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-34/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-33/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-32/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-31/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-30/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-29/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-28/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-27/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-26/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-25/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-24/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-23/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-22/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-21/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-20/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-19/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-18/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-17/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-16/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-15/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-14/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-13/",
    "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-12/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-11_1/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-10/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-09/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-08/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-07/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-06/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-05/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-04/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-03/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-02/",
# "https://mugiwarasoficial.com/manga/solo-leveling-ragnarok/capitulo-01/",
]
#%%
# funções que serão usadas para baixar os mangás
import requests
import os
def folderName(url):
    folder = url.split('/')[5].replace('.html','')
    num = folder.split('-')[1].split('_')[0]
    znum = num.zfill(4)
    return folder.replace(f'-{num}',f'-{znum}')

def fileName(url):
    result = url.split('/')[9]
    print(result)
    return result

def getManga(manga):
    url = manga
    folder = folderName(url)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # print('---')
    else:
        print('manga já baixado')
        return
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    imagesRaw = response.text.split('data-src="')
    i = 0
    listRawImages = []
    for chunk in imagesRaw:
        if 'https://mugiwarasoficial.com/wp-content/uploads/WP-manga/data' in chunk:
            listRawImages.append(chunk.split('" class="wp')[0])
            print(f'imagens {str(i)}: {listRawImages[i]}')
            i += 1
    
    # baixar imagens
    for image in listRawImages:
        img_data = requests.get(image).content
        file = fileName(image)
        with open(f'./{folder}/{file}', 'wb') as handler:
            handler.write(img_data)

    # return listImages

#%%
# loop para baixar os mangás

for manga in mangaList:
    getManga(manga)

# %%
# trata o nome das imagens
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        if len(file.split('.')[0]) <= 2:
            newfilename= file.replace(file.split('.')[0], file.split('.')[0].zfill(3))            
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
        if 'pagina_' in file or '-optimized' in file  or '-copiar' in file or '411409_' in file or '409788_' in file  or '430151_' in file:
            newfilename= file.replace('pagina_','').replace('-optimized','').replace('-copiar','').replace('411409_','').replace('409788_','').replace('430151_','')
            newfilename= newfilename.replace(newfilename.split('.')[0], newfilename.split('.')[0].zfill(3))            
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
    
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    print(f'{folder}:{onlyfiles}')


# %%
# cria os readme.md
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
onlyfolders.remove('.git')
print(onlyfolders)

conteudo = '# Solo Leveling: Ragnarok\n'
for folder in onlyfolders:
    #- [teste](/chap-0001/readme.md)
    conteudo += f'- [{folder}](/{folder}/readme.md)\n'
    # conteudo += f'<p style="text-align: center;"><button name="menu" onclick="/{folder}/readme.md">{folder}</button></p>'


print('./readme.md')
f = open('./readme.md', 'w')
f.write(conteudo)
f.close()

for i in range(len(onlyfolders)):
    chapterFolder = f'./{onlyfolders[i]}/'
    anterior = '/solo-leveling-ragnarok/'
    proximo = '/solo-leveling-ragnarok/'
    menu = '/solo-leveling-ragnarok/'
    if i - 1 >= 0: 
        anterior = f'/solo-leveling-ragnarok/{onlyfolders[i-1]}/'
    if i + 1 <= len(onlyfolders)-1: 
        proximo = f'/solo-leveling-ragnarok/{onlyfolders[i+1]}/'

    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    if 'readme.md' in onlyfiles:
        onlyfiles.remove('readme.md')
    # print(f'{onlyfolders[i]}:{onlyfiles}')
    navegacao = f'##### [ANTERIOR]({anterior})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MENU]({menu})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PRÓXIMO]({proximo})\n'
    conteudo = f'# {onlyfolders[i]}\n{navegacao}'

    for file in onlyfiles:
        conteudo += f'![{file}]({file})\n\n'
    
    conteudo += f'{navegacao}'

    print(f'{chapterFolder}readme.md')
    f = open(f'{chapterFolder}readme.md', 'w')
    f.write(conteudo)
    f.close()
# %%
# %%
# valida imagens
from os import listdir, lstat
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        size = lstat(f'./{folder}/{file}').st_size
        if size == 0:
            # onlyfiles.remove(file)
            print(f'./{folder}/{file} size {size}')

    # print(f'{folder}:{onlyfiles}')


# %%
