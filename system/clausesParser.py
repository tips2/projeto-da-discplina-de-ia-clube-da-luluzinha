from components.clauses import Clauses
import json
import os

from components.clauses import Clauses

class clausesParser:

    def __init__(self):
        self.__clauses = list()

    def _parsingJsonClause(self, jsonFile):

        if os.path.isfile(jsonFile) is False:
            print(f"Clause file {jsonFile} does not exists")
            return
        
        with open(jsonFile, 'r') as file:
            file = json.load(file)

            for clause in file:
                _c_ = Clauses()
                _c_.addClause(
                    clause=file[clause]['question'],
                    negative=file[clause]['answer']['negative'],
                    positive=file[clause]['answer']['positive']
                )
                self.__clauses.append(_c_)

        return self.__clauses
    
    def getClausesBase(self, jsonFile):
        return self._parsingJsonClause(jsonFile)