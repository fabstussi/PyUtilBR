# Projeto: **PyUtilBR**

Priado por: Fabiano Stussi Pereira em 01/08/2021.
Licença: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007

------------

## Clonando o repositório:
Após ter criado o seu projeto, entrar na pasta do projeto e clonar o repositório do PyUtilBR com o comando abaixo:
~~~ DOS
git clone https://github.com/fabstussi/PyUtilBR.git
~~~
Após a importação do PyUtilBR, basta entrar no projeto e fazer o import:
~~~ python
from PyUtilBR import PyNumBR as pnb
from PyUtilBR import PyUtilTerminal as put
~~~
O **PyNumBR** é utilizado para manipular números e data / hora.
- Métodos:
	- ```ler_inteiro``` -> Utilizado para ler números inteiros com validação, exibindo uma mensagem de erro caso o usuário digite alguma coisa diferente, a mensagem de erro é personalizável, bem como a quantidade de tentativas para digitar um número inteiro.
		- Parâmetros:
			1. **msg:** preenchimento obrigatório, é a mensagem de interação com o usuário que será impressa no prompt, obrigatoriamente deve ser do tipo str(string).
			2. **msg_erro:** de preenchimento facultativo, serve para configurar uma mensagem de erro que será exibida para o usuário caso digite algo que não seja um inteiro.
			3. **tentativas:** por padrão o método está configurado para 3 tentativas, podendo ser configurado para quantas tentativas o usuário terá para digitar um número inteiro, caso falhe o método retorna 0 (zero).
	- ```ler_real``` -> utilizado para ler números reais com validação, aceita tanto número com separador de decimais com "," (virgula) ou "." (ponto), exibe uma mensagem de erro personalizável caso o usuário digite algo que não seja um número real, possui a quantidade de tentativas para digitar um número real.
		- Parâmetros:
			1. **msg:** preenchimento obrigatório, é a mensagem de interação com o usuário que será impressa no prompt, obrigatoriamente deve ser do tipo str(string).
			1. **msg_erro:** de preenchimento facultativo, serve para configurar uma mensagem de erro que será exibida para o usuário caso digite algo que não seja um número real.
			1. **tentativas:** por padrão o método está configurado para 3 tentativas, podendo ser configurado para quantas tentativas o usuário terá para digitar um número inteiro, caso falhe o método retorna 0 (zero).
	- ```mostrar_real``` -> retorna o número com a virgula na separação dos decimais, não possui parâmetros.
	- ```pega_data``` -> retorna a data no formato dd/mm/aaaa, não tem parâmetros.
	- ```pega_hora``` -> retorne a hora no formato hh:mm, não tem parâmetros.
