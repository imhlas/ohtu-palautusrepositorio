from matchers import All, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_olio = matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def build(self):
        return self._matcher_olio
