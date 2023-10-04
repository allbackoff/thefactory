## Функционал
* Регистрация: **POST**  `/register/`
   
  _Request Body_:
  ```css
   {
      "username": string,
      "password": string,
      "first_name": string
   }
  ```
  _Response Body_:
  ```css
   {
      "username": string,
      "first_name": string
   }
  ```
* Авторизация: **POST**  `/api-token-auth/`
   
  _Request Body_:
  ```css
   {
      "username": string,
      "password": string
   }
  ```
  _Response Body_:
  ```css
   {
    "token": string
   }
  ```
* Генерация токена для телеграм бота: **POST**  `/generate-token/`
  
  _Headers_:
  `Authorization : Token {токен авторизации}`  
  _Request Body_: `None`   
  _Response Body_: 
  ```css
  {
    "token": string
  }
  ```
* Отправка сообщений боту: **POST**  `/messages/`
  
   _Headers_:
  `Authorization : Token {токен авторизации}`   
  _Request Body_:
  ```css
   {
      "text": string
   }
  ```
  _Response Body_:
  ```css
   {
      "text": string,
      "date": string
   }
  ```
* Получение списка своих сообщений: **GET**  `/messages/`
  
   _Headers_:
  `Authorization : Token {токен авторизации}`   
  _Response Body_:
  ```css
   [{
      "text": string,
      "date": string
   }]
  ```
