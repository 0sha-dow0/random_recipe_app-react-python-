import requests

def generateData():
    resp = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    resp = resp.json()
    data = resp['meals'][0]
    dish = data['strMeal']
    youtubeLink = data['strYoutube']
    category = data['strArea']
    thumbNail = data['strMealThumb']
    ingredients = []
    instruction = data['strInstructions']
    print(dish)
    for x in range(1, 10):
        ingredients.append(data['strIngredient' + str(x)])
    print(ingredients)
    images = []
    for x in ingredients:
        resp = "https://www.themealdb.com/images/ingredients/" + x + ".png"
        images.append(resp)

    polishedData = {
        'dish_Name': dish,
        'youtube_link': youtubeLink,
        'category': category,
        'thumbNail': thumbNail,
        'ingredients': ingredients,
        'overview':instruction,
        'images': images
    }
    return polishedData











