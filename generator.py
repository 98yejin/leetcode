import os
from collections import defaultdict
from urllib.parse import quote

MD_EXTENSION = '.md'

readme_content = "# leetcode\n\n## Algorithms\n\n"

current_directory = os.getcwd()
algorithms_directory = os.path.join(current_directory, "Algorithms")
readme_path = os.path.join(current_directory, "README.md")

current_directory_length = len(current_directory)
problems_by_category = defaultdict(list)

for root, dirs, files in os.walk(algorithms_directory):
    for file in files:
        if file.endswith(MD_EXTENSION):
            file_path = os.path.join(root, file)

            directory_structure = root[current_directory_length:].split('/')
            category = directory_structure[2].strip()
            problem = directory_structure[3]

            problem_path = quote(file_path[current_directory_length:])
            problem_link = f'[{problem}]({problem_path})'
            
            problems_by_category[category].append(problem_link)

for category, problems in problems_by_category.items():
    readme_content += f"### {category}\n\n"
    readme_content += '\n'.join([f"- {problem_link}" for problem_link in problems]) + '\n\n'

with open(readme_path, 'w') as file:
    file.write(readme_content)
