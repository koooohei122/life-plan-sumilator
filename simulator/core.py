class LifeSimulator:
    def __init__(self, profile):
        self.profile = profile

    def simulate(self, years=30):
        results = []
        assets = self.profile["assets"]

        for year in range(years):
            income = self.profile["income"] * ((1 + self.profile["income_growth"]) ** year)
            expenses = self.profile["expenses"]
            savings = income - expenses
            assets += savings

            results.append({
                "year": year,
                "income": income,
                "expenses": expenses,
                "assets": assets
            })

        return results
