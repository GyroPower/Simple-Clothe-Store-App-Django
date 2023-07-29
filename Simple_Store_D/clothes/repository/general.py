from .. import models 


def get_clothe(id):
    return models.Clothes.objects.get(id=id)
