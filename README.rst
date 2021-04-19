Egyption Nationa ID

A Django project template for a RESTful Application using Docker

Docker commands used :

    sudo make build
    sudo make up

testable cases :

    national id should be 14 digits , not containing chars
    national id conisit of 14 digits
    national = x-gggggg-ll-oooo-r
    national[0[ = centery
    national[1:7] = birthday
    national[7:9] = country code

this api is deployed in heroku , https://nationaid.herokuapp.com/users/nationalids/id/

thanks .
