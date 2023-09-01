from debug_toolbar.toolbar import DebugToolbar

class CustomDebugToolbar(DebugToolbar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_toolbar(self):
        # Override the rendering of the toolbar
        # Customize URL generation logic here
        self.css_url = self.css_url.replace('/debug_toolbar/', '/staticfiles/debug_toolbar/')
        return super().render_toolbar()
