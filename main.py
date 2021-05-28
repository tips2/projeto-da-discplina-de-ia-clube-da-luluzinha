from system.knowledgeParser import knowledgeParser
from system.clausesParser import clausesParser
from system.inference import inference

class engine():
    
    def _startSystem_(self):

        _k = knowledgeParser().getKnowledgeBase('./data/knowledge.json')
        _c = clausesParser().getClausesBase('./data/clauses.json')

        return _k, _c

    def _endSystem_(self, output):
        
        _c = clausesParser().getClausesBase('./data/clauses.json')

        if output[0]:
            self.clause = _c[0].getPositive() + output[1]
            self.percent = output[2]
            print("\n" + self.clause + " com uma chance de " + str(int(self.percent)) + "%.")
        else:
            self.clause = _c[0].getNegative() + output[1]
            self.percent = output[2]
            print("\n" + self.clause + " com uma chance de " + str(int(self.percent)) + "%.")

        print("\nProcure a ajuda de um profissional da saúde para um diagnóstico mais preciso.")

if __name__ == "__main__":

    _knowledge, _clauses = engine()._startSystem_()

    engine()._endSystem_(inference().startGUI(_knowledge, _clauses))



    
