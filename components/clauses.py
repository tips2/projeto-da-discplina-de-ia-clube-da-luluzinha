class Clauses:

    def __init__(self):
        self.__clause = None
        self.__positive = None
        self.__negative = None
    
    def addClause(self, clause, positive, negative):
        self.__clause = clause
        self.__positive = positive
        self.__negative = negative
    
    def getClause(self):
        return self.__clause

    def getPositive(self):
        return self.__positive

    def getNegative(self):
        return self.__negative
    