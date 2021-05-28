class Rule:

    def __init__(self, rule: str):
        self.__rule = rule
    
    def getRule(self):
        return self.__rule

class Knowledge:
    
    def __init__(self):
        self.__target = None
        self.__rules = list()
    
    def addRule(self, target, rule):
        self.__target = target
        self.__rules.append(Rule(rule))
    
    def getTarget(self):
        return self.__target

    def getRules(self):
        return self.__rules

    
