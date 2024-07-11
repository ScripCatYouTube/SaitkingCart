import flet as ft
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin
)

class KingCart:
	def __init__(self, page: Page):
		self.page = page
		self.page.add(Text("Hi"))
		self.page.update()