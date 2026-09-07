# ⚔️ Treinando Python — Jogo de Batalha

Primeiro programa de um jogo de batalha simples em Python, onde o jogador enfrenta um inimigo com ataque gerado aleatoriamente.

## 🎯 Objetivo

Projeto criado como um dos primeiros exercícios de lógica de programação em Python, praticando:

- Entrada de dados (`input`)
- Geração de números aleatórios (módulo `random`)
- Estruturas condicionais (`if` / `else`)
- Comparação de valores

## ⚙️ O que o programa faz

- ✅ Pergunta o nome do jogador
- ✅ Pergunta o valor de ataque do jogador
- ✅ Pergunta o nome do inimigo
- ✅ Sorteia aleatoriamente o valor de ataque do inimigo (entre 0 e 100)
- ✅ Compara os dois valores e informa se o jogador venceu ou foi derrotado

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `random` (biblioteca padrão do Python)

## ▶️ Como rodar o projeto

1. Certifique-se de ter o Python instalado na máquina
2. No terminal, execute:
   ```
   python primeiro_programa.py
   ```
3. Digite seu nome, o valor do seu ataque e o nome do inimigo quando solicitado

## 🖥️ Exemplo de uso

```
Digite o seu nome:João
Digite o valor do seu ataque:75
digite o nome do seu inimigo:Dragão
você derrotou  seu inimigo com uma força de: 75
```

## 💡 Possíveis melhorias futuras

- Exibir também o nome do jogador e do inimigo na mensagem final (hoje eles são coletados mas não aparecem no resultado)
- Validar se o valor de ataque digitado é realmente um número
- Limitar o valor de ataque do jogador a uma faixa razoável (ex: 0 a 100), para deixar a disputa mais justa
- Adicionar múltiplos rounds/turnos em vez de uma única comparação
- Adicionar pontos de vida (HP) para cada personagem, tornando a batalha mais elaborada

## 👤 Autor

Projeto desenvolvido como exercício prático inicial de lógica de programação em Python.
