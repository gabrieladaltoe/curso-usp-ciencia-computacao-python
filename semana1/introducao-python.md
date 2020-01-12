### Introdução ao Python

Abrindo o IDLE no sistema windows, ou o terminal no sistema MacOS, podemos começar a rodar algumas operações matemáticas com python, como soma (+), subtração (-), divisão (/) e multiplicação (*). 

É possível agrupar operações mais complexas usando (), ou comparações (>, <, <=, >=, ==, !=) que retornam *true* ou *false*. 

A seguir, alguns exemplos que foram rodados no IDLE:

        Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license()" for more information.
        >>> help
        Type help() for interactive help, or help(object) for help about object.
        >>> 1 +1
        2
        >>> 123954 + 6564
        130518
        >>> 5 > 3
        True
        >>> 3*8
        24
        >>> 2 + 5 * 2
        12
        >>> (2+5)*2
        14
        >>> 2 **8
        256
        >>> 2** 3
        8
        >>> 1**120
        1
        >>> 20 != 30
        True
        >>> 1 **20 > 20** 1
        False
        >>> 

#### Variáveis

        x = 5 
        // A variável x tem o valor 5.

Uma variável pode mudar ao longo do código, pode mudar o seu valor. Para que o IDLE imprima o valor de uma variável, usa-se também *print(nomeDaVariavel)*.

        >>> x =5
        >>> y=10
        >>> soma = x+y
        >>> print(soma)
        15
        >>> 

        >>> peso = 78
        >>> altura = 183
        >>> peso
        78
        >>> altura
        183
        >>> 

O comando print() pode imprimir várias coisas, separado apenas por vígula. 

        a = 10
        b = 30

        soma = a + b 

        print('O valor total é', soma)

Para que o arquivo .py rode no terminal, basta apenas digitar no terminal do Windows *py nome-do-arquivo*, ou no MacOS  *python3 nome-do-arquivo*, já dentro da pasta desejada:

        C:\Users\> py somador.py
        Resultado do que foi digitado em print().

