# Projeto: **PyUtilBR**

Criado por: Fabiano Stussi Pereira em 01/08/2021.
Licença: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007

------------

## Clonando o repositório:
Após ter criado o seu projeto, entrar na pasta do projeto e clonar o repositório do PyUtilBR com o comando abaixo:
~~~ DOS
git clone https://github.com/fabstussi/PyUtilBR.git
~~~
Após a importação do PyUtilBR, basta entrar no projeto e fazer o import:
~~~ python
from PyUtilBR import format_num_data_br as fnd
from PyUtilBR import desenha_terminal as tela
from PyUtilBR import cpf_cnpj_phone_utilit as ccp
~~~
### O *format_num_data_br* é utilizado para manipular números e data / hora.
- Métodos:
	- ```ler_inteiro``` -> Utilizado para ler números inteiros com validação, exibindo uma mensagem de erro caso o usuário digite alguma coisa diferente, a mensagem de erro é personalizável, bem como a quantidade de tentativas para digitar um número inteiro.
		- Parâmetros:
			1. **msg:** preenchimento obrigatório, é a mensagem de interação com o usuário que será impressa no prompt, obrigatoriamente deve ser do tipo str(string).
			2. **msg_erro:** de preenchimento facultativo, serve para configurar uma mensagem de erro que será exibida para o usuário caso digite algo que não seja um inteiro.
	- ```ler_real``` -> utilizado para ler números reais com validação, aceita tanto número com separador de decimais com "," (virgula) ou "." (ponto), exibe uma mensagem de erro personalizável caso o usuário digite algo que não seja um número real, possui a quantidade de tentativas para digitar um número real.
		- Parâmetros:
			1. **msg:** preenchimento obrigatório, é a mensagem de interação com o usuário que será impressa no prompt, obrigatoriamente deve ser do tipo str(string).
			1. **msg_erro:** de preenchimento facultativo, serve para configurar uma mensagem de erro que será exibida para o usuário caso digite algo que não seja um número real.
	- ```mostrar_real``` -> retorna o número com a virgula na separação dos decimais, não possui parâmetros.
	- ```mostrar_BLR``` -> retorna o número com simbulo da moeda real e os centavos separados por virgula, não possui parâmetros.
	- ```pega_data``` -> retorna a data no formato dd/mm/aaaa, não tem parâmetros.
	- ```pega_hora``` -> retorne a hora no formato hh:mm, não tem parâmetros.

### O *desenha_terminal* contém algumas ferramentas para facilitar o processo de criação de telas no terminal.
- Métodos:
	- ```cl_scr``` -> utilizado para limpar a tela do terminal.
	- ```desenha_linha``` -> utilizado para a criação de uma linha com um símbulo qualquer:
		- Parâmetros:
			1. __simbulo:__ uma string que irá formar uma linha na tela do terminal. Obrigatório o preenchimento.
			1. __tamanho:__ indica a quantidade de vezes que o símbolo irá ser repetido na tela do terminal, formando uma linha.
	- ```titulo``` -> escreve uma frase de uma linha, entre duas linhas formadas por um símbolo personalizavel, o titulo fica centralizado.
		- Parâmetros:
			1. __texto:__ de preenchimento obrigatório, texto de linha unica, o tamanho é calculado automaticamente.
			2. __simbolo:__ símbolo que será usado para desenhar as linhas acima e abaixo do texto.
	- ```titulos_ml``` -> desenha uma caixa na tela com um símbolo definido, com texto de multiplas linhas escrito e centralizado.
		- Parâmetro:
			1. __texto:__ uma lista de frases, cada elemento da lista será inserido em uma linha diferênte.
			2. __Alinhamento:__ Opção para alinha a esquerda 'e' ou centralizar 'c' o texto
	- ```cria_menu``` -> desenha um menu unumerado em uma caixa na tela.
		- Parâmetro:
			1. __menu:__ uma lista com as opções, que irá ser enumerado e exibida na tela.

### O *cpf_cnpj_phone_utilit* contém ferramentas para gerar e validar entradas de CPF, CNPJ e de telefones.
- Métodos:
	- ```gerar_cpf``` -> Utilitário para obter números de CPF válidos aleatóriamente.
		- Parâmetro:
			1. __mascara:__ boleano onde verdadeiro gera o CPF com o formato XXX.XXX.XXX-XX e se for falso gera apenas os números sem formato.
	- ```validar_cpf``` -> Utilitário que valida a entrada de um CPF, aceita a entrada com o formato XXX.XXX.XXX-XX ou apenas número.
	- ```gerar_cnpj``` -> Utilitário para obter números de CNPJ válidos aleatóriamente.
		- Parâmetro:
			1. __mascara:__ boleano onde verdadeiro gera o CNPJ com o formato XX.XXX.XXX/XXXX-XX e se for falso gera apenas os números sem formato.
	- ```validar_cnpj``` -> Utilitário que valida a entrada de um CNPJ, aceita a entrada com o formato XX.XXX.XXX/XXXX-XX ou apenas número.
	- ```gerar_telefone``` -> Utilitário para obter números de telefones aleatóriamente.
		- Parâmetros:
			1. __celular:__ boleano onde verdadeiro acrescenta o digito 9 ao número do telefone.
			2. __ddd:__ boleano onde verdadeiro acrescenta o DDD ao número do telefone.
			3. __mascara:__ boleano onde verdadeiro gera o número do telefone com as mascaras necessárias dependendo dos outros parâmetros.
	- ```validar_telefone``` -> utilitário que valida a entrada de números de telefone, podendo entrar com os formatos com ddd, celular e com todas as mascaras.