from photologue.models import Photo


def get_all_index_page_images():
    return Photo.objects.all().filter()
