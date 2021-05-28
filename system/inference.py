import os

from utils.utilities import sortDictionary
from components.knowledge import Knowledge

MIN_PERCENT = 50

class inference:

    def __init__(self):
        self.questions = None
        self.currentQuestion = None
        self.__knowledgeBase = None
        self.__clauseBase = None
        self.currentQuestionIndex = 0

    def startGUI(self, knowledge, clauses):
        print('\n --- Sistema Especialista em diagnose de doenças respiratórias --- \n \n ---------------- Descubra qual doença você tem ------------------ \n                          Vamos começar.               \n')

        self.questions = len(clauses)
        self.currentQuestion = clauses[0].getClause()
        self.__knowledgeBase = knowledge
        self.__clauseBase = clauses

        options = list()
        userBaseOfKnowledge = Knowledge()
        
        return self.receivingInput(options, userBaseOfKnowledge)
    
    def receivingInput(self, options, userBaseOfKnowledge):

        for knowledge_item in self.__knowledgeBase:
                for rule in knowledge_item.getRules():
                    if options.count(rule.getRule()) == 0:
                        options.append(rule.getRule())
    
        while True:
            print('\n' + self.__clauseBase[0].getClause() + '\n')
            for j in range(len(options)):
                print("[" + str(j) + "] " + str(options[j]))
            
            print("\n[-1] Sem mais sintomas")

            try:
                userInput = int(input("\nDigite aqui o número do seu sintoma: "))
            except ValueError:
                continue
            if userInput == -1:
                break

            userBaseOfKnowledge.addRule("User", options[userInput])
            
        return self.forwardChain(userBaseOfKnowledge)
    
    def forwardChain(self, userBase):
        matchesRules = dict()

        for knowledge in self.__knowledgeBase:
            match = 0
            for rule in knowledge.getRules():
                for userRule in userBase.getRules():
                    if rule.getRule() == userRule.getRule() and userBase.getRules().count(userRule) == 1:
                        match = match + 1
        
            matchesRules[knowledge.getTarget()] = (match / len(knowledge.getRules())) * 100

        matchesRules = sortDictionary(matchesRules)

        for target, percent in matchesRules.items():
            if percent >= MIN_PERCENT:
                return True, target, percent
            else:
                return False, target, percent
