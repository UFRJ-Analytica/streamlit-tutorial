# Tutorial de Streamlit

## Preparação

Para esse dashboard utilizaremos dados de Bicicletas Compartilhadas de Nova Iorque, que podem ser encontrados em:

https://drive.google.com/uc?id=10NQ5QdMQKBWw5-PpnCsjkmijXLYFFblb

Será necessário baixar os dados "citibike2019_sample.parquet" e colocar na pasta "/Data/".

Também deverá instalar todos os requirements do arquivo ```requirements.txt```. Para isso, se utilizar o pip, basta abrir o terminal de comando na raíz do projeto e rodar ```pip install -r requirements.txt```.

## Execução do Dashboard

Basta se posicionar na raíz do projeto e executar ```streamlit run dashboard.py```.

O arquivo base do projeto é o ```dashboard.py```, que importa todas as componentes necessárias.

## Boas Práticas

Para simplificar o uso do streamlit, a organização das componentes ajuda muito, bastando invocar as componentes nos momentos adequados.

Outro ponto que pode ser de grande utilidade quando o dashboard aumenta em complexidade é determinar um componente responsável por agregar todos os estados globais, como filtros e dados. Assim todas as componentes poderão ter acesso sem necessidade de passar por parâmetro.