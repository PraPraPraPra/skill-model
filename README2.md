# Intro

Este é um projecto exploratório que procura criar um motor de busca de curriculos. Ao fornecer pelo menos um skill e uma data, deve devolver a lista de curriculos que melhor se aproximam dessa(s) skill(s) e que estejam disponíveis o mais perto possível da data escolhida.

Ex.: Precisando de competências em Django e não tendo ninguem com essa skill explicitamente escrita no curriculo, o programa deve ser capaz de encontrar os top matches de curriculos que melhor se adequaram (isto é, mais semelhantes) - por exemplo - Python.

# Caminhos Percorridos

Existem vários possíveis caminhos para resolver este problema. Cada um com as suas vantagens e dificuldades. Esta secção procura percorrer um pouco os vários caminhos disponíveis para que se perceba as razões que nos levaram à solução atual.

Começando com os ingredientes essenciais, será sempre preciso:
 - Uma base de dados que guarde as skills de cada pessoa (Guarda os currículos completos? Só as skills numa lista?);
 - Uma forma de calcular semelhanças entre várias skills para que as possamos relacionar (usar listas feitas à mão? Natural Language Processing? Neural Networks?);


## Base de Dados
A base de dados é a questão mais pragmática - de acordo com as condicionantes, escolhe-se a que se enquadrar melhor.
Neste caso, optámos pela Elasticsearch já que se enquadra bem com as restantes condicionantes.

## Semelhanças entre Skills
O método para descobrir as semelhanças entre as skills será o mais complicado. Na prática, não precisamos de ter um grau de semelhança hiper-preciso entre todos os skills existentes - será de muito pouco valor determinar se Python se encontra mais perto de React ou de Angular. Apenas importa perceber que tanto o React como o Angular estão muito mais perto um do outro do que de Python.

Tento isto em conta, existirão várias classes de soluções:
  -  Soluções compiladas à mão (ter uma lista de skills semelhantes);
  -  Modelos de NLP (Word2Vec)
  -  Neural Networks
  -  Knowledge Graph (Um grafo dirigido, que mostra as relações entre as várias skills: https://www.baeldung.com/cs/ml-knowledge-graphs)

Optámos por treinar o nosso próprio modelo de NLP, utilizando como base Word2Vec e alguns outros projectos que já caminharam neste sentido (bibliografia no fim).

No futuro, um Knowledge Graph poderá fazer mais sentido e talvez seja a melhor opção. No entanto, não é uma solução trivial...

A lista feita à mão, seria demasiado complicado de criar, manter, actualizar e teriam que se tomar muitas decisões não assim tão triviais (ex.: como é que definimos o que está mais perto de Java?). 

Uma neural network precisa de datasets muito maiores que as opções e não traz nenhuma vantagem ao problema.

# Tecnologias
Para isto, vamos utilizar o Elasticsearch juntamente com um modelo de Natural Language Processing (NLP).

O Elasticsearch tem uma funcionalidade que nos permite utilizar um modelo pré-treinado de NLP para calcular um score de próximidade entre um critério de pesquisa e os dados em base de dados (criando assim uma lista ordenada por critérios de maior semelhança) : https://www.elastic.co/blog/text-similarity-search-with-vectors-in-elasticsearch

O Elasticsearch oferece vários modelos já treinados que podem ser usados para calcular este grau de próximidade. No entanto, como procuram ser modelos generalizados não conseguem capturar as diferenças várias tecnologias diferentes (conseguem perceber que "C++" está mais perto de "Java" do que de "lavatório" mas não têm noção das relações entre as várias tecnologias onde, por exemplo, "Python" e "Flask" teriam de estar sempre mais próximos do que "Python" e "PowerPoint").



Python --version:
python 3.8.10


Bibliografia de vários outros projectos:

    https://github.com/ggeop/Job-Recommendation-Engine.git
    https://github.com/vgangaprasad/ML_Skills_Match.git
    https://github.com/Jwata/job-word-embeddings.git
    https://github.com/duyet/skill2vec.git
    https://github.com/duyet/skill2vec-dataset.git
    https://github.com/duyet/related-skills.git


###     https://github.com/ggeop/Job-Recommendation-Engine.git

-> Utiliza a descrição de um trabalho para tentar prever o seu título.
Obtém os dados (10K) do indeed.com.
Partilhar o código do crawler.
Testam vários modelos para perceber qual o mais eficiente a fazer o mapeamento "Descrição" -> "Título";
Têm um número limitado de "Títulos" (a que eles chamam de Queries);
Os modelos testados (ex.: CNN) não são fáceis de aplicar a este problema: seria preciso criar uma lista de todas as tecnologias existentes para calcular as distâncias entre estas e cada descrição fornecida.
No que toca ao modelo de Word2Vec, ainda não testei a eficácia... 10K é um bom dataset, mas é preciso filtrar tudo o que não sejam tecnologias...

-> É preciso correr:
import nltk
nltk.download()

--- OU ENTÃO ---
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')


###     https://github.com/vgangaprasad/ML_Skills_Match.git

###    https://github.com/Jwata/job-word-embeddings.git



###    https://github.com/duyet/skill2vec-dataset.git
-> Has a 50K token "skills" dataset. The dataset is not perfect and the "skills" aren't allways perfect, and you don't have access to the raw data.

Word2Vec with this dataset alone prodeces no usefull results.
-------- INSERT EXAMPLE ---------

###    https://github.com/duyet/related-skills.git
-> Has a 1k raw Dataset and nothing else of use;

###    https://github.com/duyet/skill2vec.git