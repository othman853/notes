class Engine:

    def __init__(self):
        self.template_env = Environment(loader = FileSystemLoader('src/templates'))

    def render(self, template_name, template_data={}):
        template = self.template_env.get_template('{}.j2'.format(template_name))
        print(template.render(meta = { 'title': 'Title' }))
