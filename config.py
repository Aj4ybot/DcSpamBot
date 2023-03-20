import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# FOR CODES

API_ID = int(getenv("API_ID", "25785806")) 
API_HASH = getenv("API_HASH", "aa055afea5f5a4b653d430a91cc1a5ca") 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6171038521").split()))
LOGGER = int(getenv("LOGGER", None)) 
OWNER = int(getenv("OWNER_ID", "5731466060")) 
NAME = getenv("ALIVE_NAME", "Sahu name")
OWN_USERNAME= getenv("OWN_USERNAME")
ALIVE_PIC = getenv("ALIVE_PIC") 

# FOR SPAMBOT

TOKEN1 = getenv("TOKEN1", "5961954568:AAFuCPLKxJWQ2vtIz6XN8DRGS2regPq58dk") 
TOKEN2 = getenv("TOKEN2", "6131029283:AAFMIG2Lk-GZ3Iaxn0Oay8njhRwrNy8Bz4M") 
TOKEN3 = getenv("TOKEN3", "6159483566:AAHD4bAkGbCri49IuLQtTp1epkrOCx9Y1z8") 
TOKEN4 = getenv("TOKEN4", "6096114322:AAENkLrIyvYWwyPW882VdA__KyYOTur5mgM") 
TOKEN5 = getenv("TOKEN5", "6010849767:AAE8NJ9f7COzxk0c95nImEIxGkLruxf_r6M") 
TOKEN6 = getenv("TOKEN6", "6292527891:AAHavo718YQ9g55kDcTpeSI7IagHzPmjRzc") 
TOKEN7 = getenv("TOKEN7", "6157122621:AAGqD_gjwZX99xkqbOMvh2Ap5WiLE6_bi14") 
TOKEN8 = getenv("TOKEN8", "6260677943:AAHejWaTxUX_L4XF5Y34v8kvivm9FwWATck") 
TOKEN9 = getenv("TOKEN9", "5618242617:AAFv0qiYyzIiwPtkTR-XLZg-I0TobBj5hWw") 
TOKEN10 = getenv("TOKEN10", "6171761671:AAGj_sHIZPij0rBrfo1oFOtmPhQT4S2QjiA") 
