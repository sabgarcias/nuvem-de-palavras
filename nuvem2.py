import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

texto_respostas = """
Foi ótimo aprendi com muita sabedoria Foi tudo top !!!!!!!! Não tenho nada que reclama Foi muito bom eu gostei muito Nao , ta normal , nao precisa melhorar Não Precisa melhorar nada está muito bom assim Não tenho nada pra crítica foi otimo Muito bom Muito bom👍 Não precisa melhorar nada assim está ótimo A atividade foi muito boa e fácil de entender. Como sugestão, poderiam incluir mais exemplos práticos de golpes reais e simulações interativas, pois isso ajuda ainda mais no aprendizado. No geral, o conteúdo foi claro, útil e bem organized os professores de terça da mais exemplos para os alunos entender melhor sobre o assunto dado aluns professores, tirando o alex e caio, precisam explicar melhor. Acho que eles nao ligam muito para oque a crianças entedem ou deixam de entender, assim fica meio complicado! "A interface do CyberLab é intuitiva e facilita a navigation pelas atividades. Engenharia_social Hacker Engenharia_social "Sombre como proteger a minhas conta e coloca senha senguda " Tudo Trava_ZAP Sobre os golpes que pode acontecer com os link estranhos "Pra fazer uma senha e a aula de aprender a proteger minhas conta " phishing De responder a questões do corso Sobre os golpes links estranho e etc "“O conceito de phishing foi o mais interessante, pois aprendi como identificar golpes e evitar clicar em links suspeitos, aumentando minha segurança no ambiente digital " SandBox praticamente tudo, achei bem legal. A regra principal é nunca confiar, sempre verificar
"""

palavras_ignoradas = set(STOPWORDS)
palavras_ignoradas.update([
    "da", "de", "e", "o", "a", "os", "as", "em", "para", "com", "foi", "mais", "uma", "ao", "na",
    "que", "está", "assim", "pra", "pelo", "pelas", "como", "pois", "ou", "deixam", "meio", "acho",
    "tudo", "sobre", "foi", "muito", "oque", "terça", "tirando", "minhas", "senguda", "sombre", "coloca",
    "bom", "precisa", "minha", "muita", "alex", "precisam", "ta", "claro", "caio", "etc", 
    "nada", "reclama", "pode", "alunos", "aluns", "fica", "ainda", "sempre", "geral", "isso", "reais", "entendem", "é", 
    "achei", "eu", "nunca", "conta", "bem", "crianças", "ligam", "corso", "não", "nao"
])

nuvem = WordCloud(width=1200, height=800, background_color='white', stopwords=palavras_ignoradas, min_font_size=10, colormap='plasma').generate(texto_respostas)

plt.figure(figsize=(12, 8))
plt.imshow(nuvem, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

# SALVANDO COM NOME EXCLUSIVO
plt.savefig("nuvem_seguranca.png", dpi=300)
print("Sucesso! A primeira nuvem foi salva como 'nuvem_seguranca.png'.")
plt.show()
