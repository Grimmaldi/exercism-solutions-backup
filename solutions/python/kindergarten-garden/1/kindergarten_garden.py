class Garden(object):

    children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, plant_string, students=children):
        self.plant_string = plant_string
        self.students = students

        self.students = sorted(self.students)
        self.plant_rows = str(plant_string).split()

    def plants(self, child):
        plant_list = ''
        child_index = self.students.index(child)
        plant_index = {'V': 'Violets ', 'R': 'Radishes ', 'G': 'Grass ', 'C': 'Clover '}
        for row in self.plant_rows:
            for letter in row[(child_index * 2):((child_index * 2) + 2)]:
                plant_list += plant_index.get(letter)
        return plant_list.split()