import flet as ft 

class ToDo(object):
	
	def __init__(self, page: ft.Page):
		super(ToDo, self).__init__()
		self.page = page
		self.page.bgcolor = ft.colors.WHITE
		self.page.window_width = 350
		self.page.window_height = 450
		self.page.window_resizable = True
		self.page.window_always_on_top = True
		self.page.title = "Tarefas"
		self.main_page()

	def main_page(self):
		input_task = ft.TextField(hint_text = "Adicione uma tarefa", expand = True)

		input_bar = ft.Row(
			controls = [
				input_task,
				ft.FloatingActionButton(icon = ft.icons.ADD)
			]
		)

		self.page.add(input_bar)
