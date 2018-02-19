API REST
-------- 


### Aplicação feita em Django 2.0, rest_framework e django-rest-swagger


#### Usando o cURL teremos resultados de estudantes e universidades.


> Segue alguns exemplos de uso:
> - Para trocar entre ambiente de teste e produção basta mudar no começo da url "prod" por "dev".



* Para retornar todos os estudantes:
``` ruby
curl -X GET --header 'Accept: application/json' 'http://prod-letrus.us-east-1.elasticbeanstalk.com/api/students/’
``` 


* Para retornar todas as universidades: 
``` ruby
curl -X GET --header 'Accept: application/json' 'http://prod-letrus.us-east-1.elasticbeanstalk.com/api/universities/'
```


* Para retornar por ID, basta adiciona lo no fim das requisições:
``` ruby
curl -X GET --header 'Accept: application/json' 'http://prod-letrus.us-east-1.elasticbeanstalk.com/api/students/1/’
```


* Usando POST para adicionar elementos:
``` ruby
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'X-CSRFToken: YY94xAzkqNH0l98VL18sLgvBlLiwlLqOjjrocNYftgUkG1IruiHpVw1RJqGjpfbN' -d '{ \ 
   "first_name": "Marcos", \ 
   "last_name": "Maya", \ 
   "university": "1" \ 
 }' 'http://prod-letrus.us-east-1.elasticbeanstalk.com/api/students/’
``` 