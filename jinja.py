from jinja2 import Environment, FileSystemLoader

# Set up the environment with the folder containing the templates
env = Environment(loader=FileSystemLoader('templates'))

# Load the template
template = env.get_template('template.jinja2')

# Render the template with the variable
output = template.render(name=input("Bitte gib deinen Namen ein:"))


print("Grüße aus Kurs:AWS 23/07")