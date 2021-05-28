def sortDictionary(dictionary):
    return {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}