class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print("Title:", self.title)
        print("Content:", self.content)
