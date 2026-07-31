# ☁️ Nuvens de Palavras Automatizadas (Google Forms)

Este repositório contém os scripts em Python desenvolvidos para automatizar a extração de dados e a geração visual de **Nuvens de Palavras** com base nos feedbacks coletados via Google Forms. O projeto foi estruturado utilizando boas práticas de desenvolvimento no ambiente **VS Code** e versionado via **Git/GitHub**.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.11+**: Linguagem de programação principal.
* **uv**: Gerenciador de pacotes ultrarrápido para instalação de ambientes isolados.
* **WordCloud**: Biblioteca utilizada para o processamento de texto e geração das nuvens.
* **Matplotlib**: Biblioteca para renderização gráfica e exportação de arquivos de imagem (.png).
* **VS Code**: Ambiente de desenvolvimento integrado (IDE).

---

## 📂 Estrutura do Repositório

* `nuvem_seguranca.py` - Script de extração e tratamento para as respostas de segurança digital.
* `nuvem_seguranca.png` - Imagem gerada da primeira nuvem (Foco: Conscientização).
* `nuvem_tecnica.py` - Script de extração para as respostas do treinamento avançado.
* `nuvem_tecnica.png` - Imagem gerada da segunda nuvem (Foco: Redes/Fortinet).
* `README.md` - Documentação e análise dos resultados do projeto.

---

## 📊 Análise de Sentimentos e Resultados

### 1. Módulo de Conscientização (Segurança Geral)
* **Sentimento Predominante:** Altamente Positivo (~85%).
* **Destaques:** Os alunos demonstraram forte engajamento no aprendizado prático e memorizaram conceitos críticos como **Phishing**, **Engenharia Social**, **Trava ZAP** e **SandBox**, que ganharam grande peso visual na nuvem.
* **Oportunidades de Melhoria:** Feedbacks sugerem a padronização na didática de alguns docentes e a inclusão de ainda mais simulações de golpes reais.

### 2. Módulo Técnico (Redes & Fortinet)
* **Sentimento Predominante:** Neutro-Desafiador (~60% Crítico/Neutro).
* **Destaques:** O corpo docente recebeu ótimas avaliações pela prontidão em sanar dúvidas de alto nível. Os conceitos da arquitetura **Fortinet**, **FortiGate**, **IPS** e **SD-WAN** foram o centro das atenções.
* **Oportunidades de Melhoria:** Os alunos relataram uma curva de aprendizado íngreme (com termos como "difícil" e "confusão" ganhando destaque) e solicitaram a expansão de laboratórios práticos com Máquinas Virtuais para fixar os modos de **VLAN** de forma interativa.

---

## 🛠️ Como Executar este Projeto Localmente

Certifique-se de ter o [Git](https://git-scm.com) e o [uv](https://github.com) instalados no seu computador.

1. **Clone este repositório:**
   ```bash
   git clone https://github.com
   cd nuvem-de-palavras
   ```

2. **Execute as Nuvens usando o `uv`:**
   O `uv` gerenciará as dependências (`wordcloud` e `matplotlib`) de forma isolada automaticamente:
   
   * Para rodar a primeira nuvem (Segurança):
     ```powershell
     uv run --with wordcloud --with matplotlib nuvem_seguranca.py
     ```
   * Para rodar a segunda nuvem (Técnica):
     ```powershell
     uv run --with wordcloud --with matplotlib nuvem_tecnica.py
     ```

---
*Nota: Em conformidade com as diretrizes de privacidade e LGPD, a planilha bruta com as respostas individuais e dados sensíveis dos participantes foi devidamente anonimizada e armazenada em um ambiente de repositório 100% privado e restrito.*
