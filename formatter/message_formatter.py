def fluffy_border(func):
    def wrapper(message):
        border = "🌸" * 33
        cute_face = "(｡♥‿♥｡)"
        result = func(message)
        return(f"{border}\n{cute_face} {result} {cute_face}\n{border}")
    return wrapper    

def emoji_faces(func):
    def wrapper(message):
        emojis = "🐤✨🌸✨🐤"
        result = func(message)
        return(f"{emojis} {result} {emojis}")
    return wrapper

@fluffy_border
@emoji_faces
def message_display(message):
    return message
 
