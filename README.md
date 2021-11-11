# RSA_WEB_BACKEND

or running back-end you need to follow the below steps:

1- install PyCharm
2- clone the project form Github
3- create your virtual enviroment to run the project
4- after cloning, create new Repository folder in RSA_BACKEND repository as ' media'
5- install all the packages which PyCharm show as redlines in import part
6- run command ' python manage.py runserver'
7- for using Google Drive, go to Google Cloud Platform then try to make new project, then Enable Google Drive API, then click on ' CREATE CRENDENTIALS' click on 'Auth Client ID ' then follow the steps which Google will mention and in redirect link, put ' http://localhost/ '. It is because in your machine the localhost of Django is available and TLS connection is not possible cause Google Driver uploading is in test STATUS, so registered users can upload files and for PUBLISH STATUS, you have to pay and verify your app. Then download JSON file of Google and paste it as same name as exist In project repository. Then run ' run server '  command and the backend is ready for receive and response requests from front-end. 
