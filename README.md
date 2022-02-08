Dos vários projectos:
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