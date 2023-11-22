import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])
        return programs_list

# Create an instance of the GetPrograms class
programs_instance = GetPrograms()

# Call the get_programs method
programs_data = programs_instance.get_programs()
print(programs_data)

# Call the program_school method
programs_schools = programs_instance.program_school()

# Print unique schools
for school in set(programs_schools):
    print(school)
