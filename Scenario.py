from Config import Config

class hScenario:
    CURRENT_SCENARIO = 0

    def __init__(self, scenario):
        self.CURRENT_SCENARIO = scenario
        pass

    def getScenario(self):
        return self.CURRENT_SCENARIO

    def setScenario(self, scenario):
        self.CURRENT_SCENARIO = scenario
