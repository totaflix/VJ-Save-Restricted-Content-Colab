import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7742134572:AAEpoiyNWZQYlt53a2HuEQuA3WQakd23CEg")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24172301"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ca79a5425fa6dbe58853ab66cc7bb168")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://heroku:heroku@cluster0.wamwxpr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
