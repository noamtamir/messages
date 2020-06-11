# Messaging System
Backend for messaging system using Django.

## Base Url in production
[https://noams-messaging-app.herokuapp.com/](https://noams-messaging-app.herokuapp.com/)
Optional to use UI via broswer.

## Messages Endpoint
[https://noams-messaging-app.herokuapp.com/messages/](https://noams-messaging-app.herokuapp.com/messages/)

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
> POST https://noams-messaging-app.herokuapp.com/messages/
with json of a message. example:
{"receiver": 2, "subject": "a subject", "message": "a message"}
("sender" is the logged in sender, and "read" is defaulted to false)

- ### Get all messages for a specific user
> GET https://noams-messaging-app.herokuapp.com/messages?user=:id
also possible to use query params: user__username=:string, receiver=:id, receiver__username=:string, sender=:id, sender__username=:string

- ### Get all messages for logged in user
> GET https://noams-messaging-app.herokuapp.com/messages
(all messages for admin user)

- ### Get all unread messages for a specific user
> GET https://noams-messaging-app.herokuapp.com/messages?read=false

- ### Read message (return one message)
> GET https://noams-messaging-app.herokuapp.com/messages/:id/

- ### Mark message as read
> PATCH https://noams-messaging-app.herokuapp.com/messages/:id/
with json body {"read": true}

- ### Delete message (as owner or as receiver)
> DELETE https://noams-messaging-app.herokuapp.com/messages/:id/


## Link to Postman Collection with examples
[https://www.getpostman.com/collections/473e735ab2efb73fab37](https://www.getpostman.com/collections/473e735ab2efb73fab37)

## Link to Swagger File for documentation to extended API
[https://noam-messaging-app.herokuapp.com/swagger/](https://noams-messaging-app.herokuapp.com/swagger/)


## Running localy
When running localy, be sure to add dev.env file (no need for anything in it) to root directory. Runs with sqlite localy instead of postgres for quick and easy setup.