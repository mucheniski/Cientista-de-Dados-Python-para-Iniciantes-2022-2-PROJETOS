Instalar o pacote anaconda  
https://www.anaconda.com/products/individual  

comando para listar o que está instalado 
~~~
pip list
~~~  

Principais libs  
    pandas - trabalhar com os dados, como importar de planilhas por exemplo.
    numpy - trabalhar com arrays, tanto em 2D, 3D, etc...  
    matplotlib - Graficos.  

Recurso gratuito para download de dados para testes  
https://www.kaggle.com/  

Dataset - Planilhas om dados para serem trabalhados.  

Condicionais  
~~~
& e  
| ou 
~~~  

O Numpy é a lib usada para trabalhar com arrays.  
Os arrays podem ser em 1D 2D e 3D como no exemplo abaixo, sempre começando pelo eixo 0  
![](/images/ArraysExamples.png)   

Objetivo projeto1  
Na coluna Survived 0 é não e 1 é sim
Chegar ao resultato igual o arquivo titanic_results.csv
~~~
    mostrar o index iniciando por um na contagem de linhas  
    Colunas - Name | Age | Sex | Pclass | Survived  
    Filtrando somente por mulheres (female)
    Filtrando por classe, somente a primeira classe
    Filtrando apenas por sobrevientes, mostrar os sobreviventes com SIM no lugar de 1
    Orndenar os nomes em ordem alfabética
    exportar em csv
~~~

