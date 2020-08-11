# MonitorAmazon

## O que é 
A ideia é fazer um script que será colocado para rodar periódicamente (provávelmente no [IBM Cloud Functions](https://cloud.ibm.com/functions/)), pegará as informações dos produtos na sua lista da Amazon e salvará os dados em um [MongoDB](https://www.mongodb.com/).

Além de treinar minhas skills em Python, comecei esse projeto para facilitar uma coisa que faço quase que diariamente: verificar se os livros que eu quero na Amazon estão disponíveis ou se o preço de algum deles abaixou. Mas às vezes não consigo notar as diferenças ou simplesmente fico observando atoa por uma diferença que não existe.

## Como funciona

Está sendo feito um webscrapper no arquivo [listProducts.py](https://github.com/Nattel/MonitorAmazon/blob/master/listProducts.py), enquanto que o restante está sendo trabalhado no arquivo [main.py](https://github.com/Nattel/MonitorAmazon/blob/master/main.py).

No momento está sendo feito o upload de apenas os 10 primeiros livros, por uma limitação de carregamento na página da Amazon. 

### Arquivo <i>.env</i>

Para o funcionamento do script deve haver um arquivo <i>.env</i>, onde devem estar as informações da lista e do MongoDB utilizado. Ele deve ter a seguinte forma:
```
url = 

user = 
password = 
cluster = 
```
Que fique claro que arquivos <i>.env</i> não necessitam de aspas nas definições das variáveis.

## Projeto

O plano depois de otimizar o que existe é criar um modo de vizualizar os dados facilmente, algo que inicialmente deve ser feito com um Jupyter Notebook, mas a dificuldade para algo tão simples não parece valer a pena no imediatismo, um app deve ser a melhor opção a longo prazo.
