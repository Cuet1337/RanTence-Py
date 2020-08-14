# Dev Dependency
import random

# Determiners
determiners = ["the", "a", "an"]

# Conjunctions
conjunctions = ["and", "or", "but", "if", "until", "nor", "so", "yet", "although", "though", "while", "after", "before", "because", "since"]

#Describing

adjectives = ["sad", "good", "nice", "perfect", "enjoyable", "awesome", "fantastic", "flexible", "loving", "caring", "insane", "funny", "glum", "gay", "homosexual", "sexual", "beautiful", "obedient", "accurate", "optimistic", "great", "polite", "imperfect", "careful", "brave", "idiotic", "dumb", "stupid", "kind", "large", "tiny",  "small",  "enormous",  "short",  "big",  "annoying",  "idiotic",  "different", "ugly", "triangle-sized", "red", "magenta",  "simple",  "square-sized",  "dark blue",  "yellow",  "purple",  "blue", "green", "orange",  "black",  "white",  "red",  "blurple",  "pink",  "lime",  "turqouise",  "dark",  "dark purple",  "indigo",  "violet",  "unknown",  "demonic",  "evil",  "violent", "hot", "cold", "loose", "soft", "icy", "hard", "sticky", "solid", "dirty", "warm", "wet", "silent", "noisy", "loud", "silver", "gold", "dark", "crimson", "light", "fat", "skinny", "deep", "oval", "early", "speedy", "old", "young", "quick", "future", "heavy", "limited", "few", "each", "full", "poor", "real", "glossy", "greatfull", "cloudy", "clear", "cracked", "wild", "cute", "poisoned", "electric", "electrical"
] 

# Words from the Dictionary

words = ["table", "cat", "dog", "baby", "chicken", "laptop", "computer", "kid", "door", "school", "cloud", "profile", "human", "lamp", "tree", "clock", "portal", "bench", "charger", "poop", "apple", "phone", "app", "brush", "pencil", "knife", "dagger", "scythe", "mace", "keyboard", "mouse", "mice", "letter", "space", "jungle", "spaceship", "button", "jacket", "staff", "pokemon", "ambulance", "planet", "plastic", "ice", "bed", "beard", "barn", "rainbow", "raincoat", "jewellery", "kitchen", "carpet", "carrot", "caravan", "jelly", "car", "candle", "camera", "breakfast", "banana", "kiwi", "beef", "pork", "machine", "magazine", "motorcycle", "dream", "dress", "disease", "file", "fan", "blazer", "coat", "pants", "trousers", "tracksuit", "eggplant", "microphone", "hinge", "sky", "sun", "moon", "engine", "magician", "eye", "whale", "window", "roof", "football", "forest", "ocean", "ghost", "oil", "glass", "orange", "oxygen", "blood", "furniture", "garage", "oyster", "gas", "garden", "zoo", "night", "notebook", "plants", "photo", "image", "chat", "map", "enemey", "stopwatch", "watch", "vehicle", "motorbike", "bike", "scooter", "basket", "ball", "basketball", "stove", "cooker", "credit", "card", "credit card", "juice", "controller", "xbox", "playstation", "hub", "pub", "office", "room", "frost", "snowflake", "money", "cash", "score", "game", "water", "mop", "gun", "pistol", "bullets", "sniper", "scope", "robot", "client", "blade", "ninja star", "book", "pages", "rocks", "branch", "beer", "radio"]

verbs = ["ran", "slept", "ate", "sat", "spoke to", "filtered", "walked", "watched", "pat", "moved", "pushed", "chocked", "felt", "cried"]


rconjs = random.choice((conjunctions))
radjs = random.choice((adjectives))
rwords = random.choice((words))
rdets = random.choice((determiners))
rverbs = random.choice((verbs))

rconjs2 = random.choice((conjunctions))
radjs2 = random.choice((adjectives))
rwords2 = random.choice((words))
rdets2 = random.choice((determiners))

rdets3 = random.choice((determiners))
rwords3 = random.choice((words))

#rantence()

if rdets == "a":
  if radjs.startswith("a" or "e" or "i" or "o" or "u"):
    rdets == "an"
  else:
    pass 

aftercompound = f'{rdets} {radjs} {rwords} {rconjs}, {rdets2} {radjs2} {rwords2} {rverbs} {rdets3} {rwords3}'
beforecompound = f'{rconjs} {rdets} {radjs} {rwords} {rverbs} {rdets2} {rwords3}, {rdets3} {radjs2} {rwords2}'
nocompound = f'{rdets} {radjs} {rwords}'

a = ["1", "2", "3"]
randoma = random.choice((a))
#1 = beforecompound
#2 = aftercompound
#3 = nocompound

def rt():
  if randoma == "1":
    print(beforecompound)
  elif randoma == "2":
    print(aftercompound)
  elif randoma == "3":
    print(nocompound)
