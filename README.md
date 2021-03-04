# Foodanic Recipes 🥘 

A Django CRUD app tutorial published on [Dev.to](https://dev.to/vladyslavnua/how-to-build-a-django-web-app-from-scratch-tutorial-5bp0), [Hackernoon](), and [Medium](). Features include User Authentication, CRUD operations, Markdown Field support, Live deployment to Heroku.

[Preview Live](https://foodanic.herokuapp.com/)

## Local Installation

Follow these instructions to run the project locally.

```bash
git clone https://github.com/vladyslavnUA/foodanic && cd foodanic/

# create and activate virtual environment 
virtualenv env
source env/bin/activate

# install requirements
pip install -r requirements.txt

# run migrations to create db
python manage.py migrate

# run the app
python manage.py runserver
```

## Troubleshooting 🐞


If you come across any bugs/issues with the code, feel free to open a [new issue](https://github.com/vladyslavnUA/foodanic/issues) in the repo. If you experience technical issues, you can always do a quick Google search to see if someone has encountered a similar Django-related issue before.


## Contributing 💻
[Pull requests](https://github.com/vladyslavnUA/foodanic/pulls) are welcome. For major changes, please open an issue first to discuss what you would like to change. Make sure to run tests and migrations as appropriate.

## License 📜
[MIT](https://github.com/vladyslavnUA/foodanic/blob/main/LICENSE)
