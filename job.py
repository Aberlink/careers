class Job():
    def __init__(self, id, title, location, salary, currency, responsibilities=None, requirements=None) -> None:
        self.id = id
        self.title = title
        self.location = location
        self.salary = salary
        self.currency = currency
        self.responsibilities = responsibilities
        self.requirements = requirements
        