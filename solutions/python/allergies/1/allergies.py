class Allergies:

    def __init__(self, score):
        self.score = score
        self.list_of_items = [('cats', 128),
                              ('pollen', 64),
                              ('chocolate', 32),
                              ('tomatoes', 16),
                              ('strawberries', 8),
                              ('shellfish', 4),
                              ('peanuts', 2),
                              ('eggs', 1)]
        self.allergy_list = []
        self.allergens = []
        self.lst = self.make_lst(self.score)

    def make_lst(self, score):
        for item in self.list_of_items:
            if item[1] <= self.score:
                self.allergy_list.append(item[0])
                self.score -= item[1]
            else:
                pass
        return self.allergy_list

    def is_allergic_to(self, allergen):
        self.allergen = allergen
        self.allergy_list = self.lst
        for x in allergen:
            if str(self.allergen) in self.allergy_list:
                return True
            else:
                return False