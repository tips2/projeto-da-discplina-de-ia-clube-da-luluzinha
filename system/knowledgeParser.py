import json
import os

from components.knowledge import Knowledge

class knowledgeParser:

    def __init__(self):
        self.__knowledgeBase = list()
    
    def _parsingJsonKnowledge(self, jsonFile):
        
        if os.path.isfile(jsonFile) is False:
            print(f"Este arquivo {jsonFile} não existe.")
            return

        with open(jsonFile, 'r') as file:
            file = json.load(file)

            for knowledge in file['target']:
                knowledgeBase = Knowledge()
                for rule in knowledge['rules']:
                    knowledgeBase.addRule(target=knowledge['name'], rule=knowledge['rules'][rule])

                self.__knowledgeBase.append(knowledgeBase)
        
        return self.__knowledgeBase
    
    def getKnowledgeBase(self, jsonFile):
        return self._parsingJsonKnowledge(jsonFile)


