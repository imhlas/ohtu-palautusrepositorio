from matchers import All

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_olio = matcher

    def build(self):
        return self._matcher_olio
