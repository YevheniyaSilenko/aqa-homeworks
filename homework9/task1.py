class KoboCompany:
    def __init__(self, name, industry, location, founded_year):
        self.name = name
        self.industry = industry
        self.location = location
        self.founded_year = founded_year

    def __str__(self):
        return f"Company: {self.name}\nIndustry: {self.industry}\nLocation: {self.location}\nFounded Year: {self.founded_year}"

# Usage:
kobo = KoboCompany("Kobo Inc.", "Technology", "San Francisco, CA", 2009)
print(kobo)
