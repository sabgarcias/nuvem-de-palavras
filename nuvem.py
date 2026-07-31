import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# O seu novo texto de respostas com termos compostos ajustados
texto_respostas = """
Entender agentes coletores. Tópicos sobre IPS e SD-WAN Nenhum Ha O mais difícil foi entender os tipos de modos do VLAN_modos, acredito que pela falta de prática e por ser abordado bem cedo na jornada do curso, tive que reler várias vezes os conceitos pra fixar. Muito bom todo o material. Maquina_virtual Entender a diferença profunda de como o FortiGate processa os pacotes gera muita confusão. Disponibilizar laboratórios da fortinet, e garantir que os alunos façam. Criação de mais laboratórios práticos e ambientes aonde os alunos podem testar seus conhecimentos Sim Acredito que inserir mais laboratórios e aulas práticas seria melhor pra ver mais na prática os conceitos abordados, preparar os notebooks antes das aulas para os alunos conseguirem “brincar” e testar as coisas seria interessante. Também acho que a forma como o curso foi apresentado aos interessados inicialmente não foi muito precisa, visto que a expectativa era entender os conceitos básicos de cybersec, mas chegando la foram abordados conceitos bem mais técnicos e complexos focados praticamente 100% na arquitetura da Fortinet. No geral gostei muito da dinâmica dos professores, sempre se colocaram a disposição pra tirar todas as dúvidas e nos incentivaram muito a continuar estudando e tirar as outras certificações. Acredito que só agradecemos. Mais aulas práticas! No período que eu estava no curso sinto que os professores são excelentes para ensinar e consegui entender muito bem as coisa, sinto que não precisa melhorar nada por enquanto
"""

# Lista expandida com palavras e conectivos para ignorar nesta nuvem
palavras_ignoradas = set(STOPWORDS)
palavras_ignoradas.update([
    # Conectivos e pronomes comuns
    "da", "de", "e", "o", "a", "os", "as", "em", "para", "com", "foi", "mais", "uma", "ao", "na",
    "que", "está", "assim", "pra", "pelo", "pelas", "como", "pois", "ou", "do", "dos", "no", "nos",
    "por", "aos", "la", "mas", "que", "todo", "toda", "tudo", "seu", "seus", "suas", "pela", "antes",
    
    # Palavras organizacionais e de opinião para limpar a nuvem
    "eu", "Também", "seria", "sobre", "tipos", "pacotes", "muita", "façam", "das", "podem", "era", "ser",
    "cedo", "se", "gera", "são", "ver", "chegando", "não", "criação", "foram",
    "entender", "curso", "professores", "alunos", "aulas", "aluno", "muito", "bom", "melhor", 
    "excelentes", "coisas", "coisa", "nada", "enquanto", "sinto", "acredito", "acho", "visto", 
    "ter", "tive", "reler", "várias", "vezes", "geral", "gostei", "dinâmica", "sempre", "colocaram", 
    "disposição", "tirar", "todas", "dúvidas", "incentivaram", "continuar", "outras", "só", 
    "agradecemos", "período", "estava", "ensinar", "consegui", "precisa", "melhorar", "nenhum", "ha", "sim"
])

# Gerando a nuvem de palavras técnica
nuvem = WordCloud(
    width=1200, 
    height=800, 
    background_color='white',
    stopwords=palavras_ignoradas, 
    min_font_size=10,
    colormap='cool'  # Nova paleta de cores (tons frios de azul, ciano e roxo), bem estilo TI
).generate(texto_respostas)

# Configurando a exibição visual
plt.figure(figsize=(12, 8))
plt.imshow(nuvem, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

# Salva por cima da imagem anterior na pasta Documents
plt.savefig("nuvem_de_palavras.png", dpi=300)
print("Sucesso! A nova nuvem técnica foi salva em 'nuvem_de_palavras.png'.")
plt.show()
