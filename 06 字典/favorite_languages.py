favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('point','No point value assigned.')
print(point_value)
