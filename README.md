# StackOverflow Parser
This is a simple site that enables you to find answers on your questions using StackOverflow

## How to install it locally
Setup process on Linux:
```bash
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```
It's similar on other operating systems.

## How to use it locally
Before you start activate the virtual environment
```bash
source venv/bin/activate
```

Then you can use the site:
```bash
python manage.py runserver
```

## How to deploy it
The project supports Heroku Cloud Application Platform. If you want to use Heroku service, you may create the 
application and deploy your code using the following commands:
```bash
heroku create
git push heroku master 
```
To learn more visit [Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app)
