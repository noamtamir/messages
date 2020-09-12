# Messaging System

Backend for messaging system using Django.

## Base Url in production

[https://messages-app.noamtamir.com/](https://messages-app.noamtamir.com/)  
Optional to use UI via broswer.

## Messages Endpoint

[https://messages-app.noamtamir.com/messages/](https://messages-app.noamtamir.com/messages/)

## Authentication

Use Basic Authentication (username, password).  
Logged in user will only be able to view, create, edit and delete messages which user is related to (sender/receiver).  
Admin user can view, create, edit and delete all messages.

## User Credentials (username: password)

- admin: chocolateisawsome123
- bobmarley: iambob123
- louisarmstrong: iamlouis123
- prince: iamprince123

## How to use the API

- ### Write message

  > POST https://messages-app.noamtamir.com/messages/  
  > with json of a message. example:  
  > {"receiver": 2, "subject": "a subject", "message": "a message"}  
  > ("sender" is the logged in sender, and "read" is defaulted to false)

- ### Get all messages for a specific user

  > GET https://messages-app.noamtamir.com/messages?user=:id  
  > also possible to use query params: user\_\_username=:string, receiver=:id, receiver\_\_username=:string, sender=:id, sender\_\_username=:string

- ### Get all messages for logged in user

  > GET https://messages-app.noamtamir.com/messages  
  > (all messages for admin user)

- ### Get all unread messages for a specific user

  > GET https://messages-app.noamtamir.com/messages?read=false

- ### Read message (return one message)

  > GET https://messages-app.noamtamir.com/messages/:id/

- ### Mark message as read

  > PATCH https://messages-app.noamtamir.com/messages/:id/  
  > with json body {"read": true}

- ### Delete message (as owner or as receiver)
  > DELETE https://messages-app.noamtamir.com/messages/:id/

## Link to Postman Collection with examples

[https://www.getpostman.com/collections/473e735ab2efb73fab37](https://www.getpostman.com/collections/473e735ab2efb73fab37)

## Link to Swagger File for documentation to extended API

[https://messages-app.noamtamir.com/swagger/](https://messages-app.noamtamir.com/swagger/)

## Running localy

When running localy, be sure to add dev.env file (no need for anything in it) to root directory. Runs with sqlite localy instead of postgres for quick and easy setup.
