pets = {'Everest': '29032', 'k2': '28251', 'KangchenJjnga': '28169', 'Lhotse': '27940', 'makalu': '27825', }
for mountain in pets.keys():
    print(mountain)
for height in pets.values():
    print(height)
for mountain, height in pets.items():
    print(mountain, " with an elevatioon of ", height)