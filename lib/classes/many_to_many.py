class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        author.articles_list.append(self)
        magazine.articles_list.append(self)
        
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        pass
    
    
class Author:
    def __init__(self, name):
        self._name = name
        self.articles_list = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return self.articles_list

    def magazines(self):
        return list(set(article.magazine for article in self.articles_list))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles_list:
            return None
        return list(set(article.magazine.category for article in self.articles_list))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.articles_list = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self.articles_list

    def contributors(self):
        return list(set(article.author for article in self.articles_list))

    def article_titles(self):
        if not self.articles_list:
            return None
        return [article.title for article in self.articles_list]

    def contributing_authors(self):
        author_counts = {}

        for article in self.articles_list:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1

        contributing = []
        for author, count in author_counts.items():
            if count >= 3:
                contributing.append(author)

                return contributing
