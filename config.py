from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "8e409e260f1d80f0ead65da912ee07bb")
      API_ID = int(getenv("API_ID", "11671320"))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "5813212548:AAG1503Ilf2se-uiHkWwNSxPSr20v0yL6Oo")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001747273968:-1001629175532").replace("\n", " ").split(' '))
