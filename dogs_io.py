import requests
from io import BytesIO
from PIL import Image
from random import choice


url = "https://dog.ceo/api/breed{pattern}"


class InvalidBreed(Exception):
    pass


def get_list_of_breeds(args):
    final_list = []
    if args.list_by_breed:
        breed = args.list_by_breed
        breeds_json = requests.get(url.format(pattern=f'/{breed}/list')).json() # noqa 551
    else:
        breeds_json = requests.get(url.format(pattern="s/list/all")).json()
    for each_breed in breeds_json["message"].keys():
        dog = Dog(each_breed, breeds_json["message"][each_breed])
        final_list.append(dog)
    if not final_list:
        raise InvalidBreed("Given breed does not exists!")
    return final_list


def get_photo(breed):
    if not breed:
        response_json = requests.get(url.format(pattern="s/image/random")).json() # noqa 551
        image_link = requests.get(response_json['message'])
    else:
        response_json = requests.get(url.format(pattern=f'/{breed}/images')).json() # noqa 551
        try:
            image_link = requests.get(choice(response_json['message']))
        except IndexError:
            raise InvalidBreed("Given breed does not exists!")
    return Image.open(BytesIO(image_link.content))


class Dog:
    def __init__(self, breed, subbreeds):
        self.breed = breed
        self.subbreeds = subbreeds

    def __str__(self) -> str:
        if not self.subbreeds:
            return f'Breed: {self.breed.title()}. No subbreeds.'
        else:
            return f'Breed: {self.breed.title()}. Subbreeds: {self.subbreeds}'
