import sys
import argparse
from zaliczenie_psy_io import get_list_of_breeds, get_photo


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("--list_all", action='store_true')
    parser.add_argument("--list_by_breed")
    parser.add_argument("--get_random_photo", action="store_true")
    parser.add_argument("--get_breed_photo")
    args = parser.parse_args(arguments[1:])
    if args.list_all or args.list_by_breed:
        breeds = get_list_of_breeds(args)
        for each_breed in breeds:
            print(str(each_breed))
    if args.get_random_photo:
        photo = get_photo(None)
        photo.save('dog.jpg')
    if args.get_breed_photo:
        photo = get_photo(args.get_breed_photo)
        photo.save(f'{args.get_breed_photo}.jpg')


if __name__ == "__main__":
    main(sys.argv)
