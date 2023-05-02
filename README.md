

# Mokko

Mokko is a web application built with Django that allows workers of the coffeehouse administrate their data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

## Installation

To install and run Mokko, follow these steps:

1. Clone the repository to your local machine:

```
https://github.com/VsevolodSheyko/Mokko.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up the database:

```
python manage.py migrate
```

4. Create a superuser account:

```
python manage.py createsuperuser
```

5. Run the development server:

```
python manage.py runserver
```

The application should now be running at http://localhost:8000/ in your web browser.

## Usage

To use Mokko, follow these steps:

1. Open your web browser and navigate to http://localhost:8000/.

2. Navigate to the one of defined URL's.

## Contributing

If you would like to contribute to Mokko, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix:

```
git checkout -b my-feature-branch
```

2. Make your changes and commit them with a descriptive commit message:

```
git commit -m "Add feature X"
```

3. Push your changes to your fork:

```
git push origin my-feature-branch
```

4. Create a pull request on the main repository with a detailed description of your changes.

## License

This project is licensed under the Vsevolod Sheiko License

## Author

Mokko was created by Vsevolod Sheiko. You can contact me at vsevolodsheyko@gmail.com

## Acknowledgements

- Django
- REST API
- HTTP Methods

## Testing

To run the test suite for Mokko, use the following command:

```
python manage.py test
```

This will run all of the tests for the application and provide feedback on any failures or errors.

## Deployment

To deploy Mokko to a production server, follow these steps:

1. Configure the production server with the necessary environment variables, including the `SECRET_KEY` and database settings.

2. Install the required dependencies on the server:

```
pip install -r requirements.txt
```

3. Start the production server:

```
gunicorn Mokko.wsgi:application --bind 0.0.0.0:8000
```

This will start a Gunicorn server that listens on port 8000 and serves the Coffeehouse application.

## Support

If you encounter any issues with Mokko or have any questions, please contact us at vsevolodsheyko@gmail.com

Thank you for using Mokko!