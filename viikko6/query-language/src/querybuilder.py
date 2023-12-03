from matchers import All, PlaysIn, And, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_olio = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher_olio,PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher_olio, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher_olio, HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._matcher_olio
