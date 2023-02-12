Dog API Wrapper:
This is a Python script that wraps the Dog API which provides information about dog breeds and pictures of dogs.

Usage:
The script provides several options for using the Dog API:

- List all breeds and subbreeds
- List information about a specific breed
- Get a random picture of a dog
- Get a picture of a specific breed

To use the script, you need to run the following command in your terminal:
python script_file.py [options]

Options:
--list_all: List all breeds and subbreeds
--list_by_breed: List information about a specific breed. To use this option, you need to specify the breed name after the option, e.g., --list_by_breed husky.
--get_random_photo: Get a random picture of a dog and save it as dog.jpg.
--get_breed_photo: Get a picture of a specific breed and save it as breed_name.jpg. To use this option, you need to specify the breed name after the option, e.g., --get_breed_photo husky.

Error Handling:
If the breed specified with --list_by_breed or --get_breed_photo options does not exist, the script will raise an InvalidBreed exception with the message "Given breed does not exists!".

License:
This script is open source and available under the MIT License.
