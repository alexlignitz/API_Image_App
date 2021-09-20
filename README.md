My first project written completely in Django Rest Framework.

It is an API allowing to upload images and use it depending on the user account type.
There are three user account types and views connected with them:
- Basic account user: can access a thumbnail of the uploaded picture (200px height)
- Premium account user: can access two thumbnails of the uploaded picture (200px and 400px height) as well as the original picture
- Enterprise account user: can access the Premium user features plus a view where he can fetch an expiring link to the uploaded picture (expiration time can be set by user between 300 and 3000 sec)

Admin has superuser features and can access all the pictures/thumbnails and also create expiring links through admin panel.
