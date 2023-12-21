#!/usr/bin/env python
# coding: utf-8

# In[59]:


# REALIZANDO UMA BUSCA POR PALAVRAS E PRINTANDO A BUSCA DE VERMELHO AO IDENTAR A PAGINA

import fitz  # PyMuPDF

nome_arquivo_local = "pinochio.pdf"
palavra_filtro = "Polendina"

# ABRINDO O PDF QUE IREI TRABALHAR OS DADOS
documento = fitz.open('C:/Users/Helena/Downloads/pinochio.pdf') # AQUI É O DIRETORIO EM QUE ESTA O PDF

# Itera sobre todas as páginas do PDF
for pagina_num in range(documento.page_count):
    pagina = documento[pagina_num]
    texto = pagina.get_text()

    # Verifica se a palavra de filtro está na página
    if palavra_filtro.lower() in texto.lower():
        # Substitui a palavra de filtro pelo texto formatado com cores
        texto_formatado = texto.replace(palavra_filtro, f"\033[1;31;43m{palavra_filtro}\033[0m")

        # Imprime o número da página e o texto formatado
        print(f"Palavra '{palavra_filtro}' encontrada na página {pagina_num + 1}:\n{texto_formatado}\n")


# In[58]:


# AQUI UTILIZEI O SPLIT PARA BUSCAR E PRINTAR UMA LISTA DE PALAVRAS POR PAGINA

import fitz  # PyMuPDF

nome_arquivo_local = "pinochio.pdf"

# Abre o arquivo baixado
documento = fitz.open('C:/Users/Helena/Downloads/pinochio.pdf')

for pagina_num in range(documento.page_count):
    pagina = documento[pagina_num]  # Corrigi o índice da página
    texto = pagina.get_text()

    # Exemplo: imprimir as primeiras 10 palavras de cada página
    palavras = texto.split()

    # Verifica se a palavra de filtro está na página
    if palavras:
       
    
    #   IMPRIMINDO LISTA DE PALAVRAS    
        print(f"Palavras na página {pagina_num + (10)}: {palavras[:5]}")
        


# In[48]:


# BUSCANDO PALAVRAS NO DOCUMENO, REGISTRANDO PAGINA, E TOTAL DE OCORRENCIA DA PALAVRA

import fitz  # PyMuPDF

nome_arquivo_local = "pinochio.pdf"
palavra_filtro = "Pinocchio"  # Substitua pela sua palavra-chave

# Abre o arquivo baixado
documento = fitz.open('C:/Users/Helena/Downloads/pinochio.pdf')

# Inicializa a contagem de ocorrências
ocorrencias_totais = 0

for pagina_num in range(documento.page_count):
    pagina = documento[pagina_num]
    texto = pagina.get_text()

    # Verifica se a palavra de filtro está na página
    if palavra_filtro.lower() in texto.lower():
        
        # Incrementa a contagem de ocorrências
        ocorrencias_totais += texto.lower().count(palavra_filtro.lower())

        # Imprime a ocorrência na página
        print(f"Palavra '{palavra_filtro}' encontrada na página {pagina_num + 1}.")

# Imprime o total de ocorrências
print(f"Total de ocorrências da palavra '{palavra_filtro}': {ocorrencias_totais}")


# In[ ]:




