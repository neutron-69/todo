import django_tables2 as tables



class TodoTable(tables.Table):
    title = tables.Column(empty_values={},orderable = False)
    description = tables.Column(empty_values={},orderable = False)
    duedate = tables.DateColumn(empty_values={},format="d-m-Y")
    is_completed = tables.BooleanColumn(visible=False)
    mark_complete = tables.TemplateColumn(template_name="mark_complete_button.html",orderable = False)
    delete = tables.TemplateColumn(template_name="delete_todo.html",orderable=False)
    edit = tables.TemplateColumn(template_name="edit_button.html",orderable=False)


    def render_title(self, value, record):
        return record.title

    def render_description(self, value, record):
        return record.description

    def render_due_date(self, value, record):
        return record.duedate
    def render_completed(self, value, record):
        return record.is_completed