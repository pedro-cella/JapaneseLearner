# JapaneseLearner

# Introdução

O aprendizado do japonês pode ser desafiador, especialmente quando se trata dos sistemas de escrita hiragana e katakana. Para facilitar esse processo, este projeto desenvolve uma ferramenta interativa que ajuda os usuários a aprimorar suas habilidades com os kanas do japonês. O objetivo principal é oferecer uma plataforma prática para que os usuários possam melhorar sua escrita, leitura e pronúncia dos kanas.

O projeto oferece duas funcionalidades principais:

**Prática de Escrita:** Os usuários têm a opção de praticar a escrita dos kanas em diferentes formatos, como ler um kana e escrevê-lo em romaji ou vice-versa. Isso promove um entendimento mais profundo e a memorização dos caracteres japoneses.

**Prática de Leitura e Pronúncia:** O programa exibirá um kana e o usuário deverá pronunciá-lo corretamente. Esta funcionalidade é projetada para ajudar os usuários a desenvolver a precisão na pronúncia e a fluência na leitura dos kanas.

## Implementações desenvolvidas

- [x] Criação dos bancos de dados de hiragana e katakana.

- [x] Criação da prática através da escrita, escrita dos kanas e reconhecimento do romaji e escrita do romaji e reconhecimento do kana.

## Implementações a ser desenvolvida

- [ ] Criação da prática de fala. O programa mostra um símbolo (kana) e é exigido que a pessoa fale qual kana foi mostrado, o programa deve reconhecer o que foi falado e estabelecer um acerto ou erro (em desenvolvimento)

- [ ] Criar a escolha da coluna dos kanas em Hiragana e Katakana para prática da escrita

- [ ] Criar a escolha da coluna dos kanas em Hiragana e Katakana para prática da fala

- [ ] Melhora na organização do código, implementação de classes

- [ ] Criação de uma interface simples, melhora visual

- [ ] Criação de uma interface Web disponível no Github Pages

## Como rodar

### Criar um ambiente virtual

```
python -m venv nome_ambiente_virtual
```

### Ativar ambiente virtual

```
source nome_ambiente_virtual/bin/activate
```

### Baixar requiremens.txt

```
pip install -r requirements.txt
```

### Executar programa

```
python src/main.py
```

## Observações

Caso receba o seguinte erro:

```
ERROR: Could not build wheels for pyaudio, which is required to install pyproject.toml-based projects
```

use o comando

```
sudo apt install portaudio19-dev
```
