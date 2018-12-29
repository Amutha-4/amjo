def snake_to_camel(Word):
        import re
        return ''.join(x.capitalize() or '_' for x in Word.split('_'))

print(snake_to_camel('python_exercises'))

