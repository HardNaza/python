# Gerador de Senhas

O **Gerador de Senhas** é uma ferramenta simples e eficiente para criar senhas seguras e aleatórias. Ele gera senhas que combinam letras maiúsculas e minúsculas, dígitos e caracteres especiais, tornando-as robustas contra ataques de força bruta e outros métodos de invasão.

## Como funciona

O programa é escrito em Python e utiliza a biblioteca `secrets` para garantir que as senhas geradas sejam verdadeiramente aleatórias e seguras. A senha é criada a partir de uma combinação de letras maiúsculas e minúsculas, dígitos e caracteres especiais, resultando em senhas altamente resistentes a tentativas de adivinhação.

## Requisitos

- Python 3.x

## Como usar

1. Certifique-se de que você tenha o Python 3.x instalado em seu sistema.
2. Faça o download ou clone este repositório em seu computador.
3. Abra um terminal ou prompt de comando na pasta onde você salvou o arquivo `gerador_de_senhas.py`.
4. Execute o seguinte comando para gerar uma senha:

```bash
python gerador_de_senhas.py
```

5. O programa irá gerar uma senha aleatória com 12 caracteres e exibi-la no terminal.

Você pode modificar o valor `k=12` na linha `print(''.join(config(caracters, k=12)))` para gerar senhas com um número diferente de caracteres.

## Aviso de responsabilidade

Embora as senhas geradas por este programa sejam altamente seguras, é importante lembrar que nenhuma senha é 100% inviolável. É sempre recomendável adotar boas práticas de segurança, como não compartilhar senhas, usar autenticação de dois fatores sempre que possível e atualizar regularmente suas senhas.