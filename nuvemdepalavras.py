# -*- coding: utf-8 -*-
"""
TCC DSA 231 - NUVEM DE PALAVRAS
@author: MARIANA DA SILVA ROSA DE OLIVEIRA
"""
! pip install wordcloud matplotlib pandas
! pip install nltk

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Baixar stop words, se necessário
nltk.download('stopwords')

# Carregar stop words em português
stop_words = set(stopwords.words('portuguese'))

# Lista personalizada de palavras a serem removidas
custom_stop_words = ['se ela quiser', 'De acordo com o meu trabalho vejo', 'ganhando a cada dia mais espaço no mercado de trabalh',
                     'As mulheres na sociedade de hoje são', 'Ao meu ver', 'e o reconhecimento dos seus gera cada vez mais visibilidade e conflitos',
                     'Não consigo descrever em apenas uma palavra', 'fazer', 'mão', 'apenas', 'ocupando', 'nenhum', 'dia', 'pois', 'ganhando', 'parece',
                     'ver', 'hoje', 'muita', 'também', 'quiser', 'ainda', 'cada', 'sempre']  # Adicione suas palavras aqui

# Combinar as stop words com a lista personalizada
combined_stop_words = stop_words.union(set(custom_stop_words))

#%%
# Carregar os dados
data = pd.read_excel("nuvemdepalavras.xlsx")

# Concatenar todas as respostas em uma única string
text = ' '.join(data['respostas'].dropna())

# Dividir o texto em palavras
words = text.split()

# Remover stop words
filtered_words = [word for word in words if word.lower() not in combined_stop_words]

# Juntar as palavras filtradas de volta em uma string
filtered_text = ' '.join(filtered_words)

# Criar a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)

# Exibir a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Não mostrar os eixos
plt.show()