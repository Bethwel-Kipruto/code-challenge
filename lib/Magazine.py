class Magazine:
    def __init__(self, category, name, articles, authors):
        self.name = name
        self.articles = articles
        self.authors = authors
        self.category = category

    def display(self):
        print("Category:", self.category)
        print("Magazine:", self.name)
        print("Articles:")
        for article in self.articles:
            article.display()
        print("Authors:")
        for author in self.authors:
            author.display()
        
