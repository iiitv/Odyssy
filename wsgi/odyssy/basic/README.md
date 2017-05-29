# Basic

Contains carousel upload portal. 

Make sure that you have installed django-photologue.

After installing django-photologue, run **python manage.py migrate photologue**

Since, django-photologue has some bugs, so for proper uploading of images,
follow the steps mentioned below.
 
1. In admin panel, don't click on "Gallaries", because it shows some strange error. 
Many others are facing same problem. An issue is opened in django-photologue 
repository, as soon as that issue is resolved there, I will fix it here.

2. For uploading, click on Photos. If you want to add single photo, click on "ADD PHOTO" 
option on top right of the page. If you want to upload multiple images, store your images 
in a zip file and click "UPLOAD A ZIP ARCHIVE".

3. While uploading a zip archive or an image, if you want to display those images on carousel,
then make sure that "is_public" check_box on bottom of page is checked. If you don't want
to display those images in carousel, simply uncheck the box.

4. If you wish to add some images to set of images which are being displayed on carousel, 
then go to admin panel and select "Photos". List of images will be displayed in front 
of you. Select new set of images by simply selecting the checkboxes on left side of the 
page, then go to "actions" and select "Show them on carousel". Similarly, if you wish to 
remove some images from carousel, then follow above steps and select "Remove them from carousel".
