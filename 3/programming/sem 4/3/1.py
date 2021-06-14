''' Автор: Гришутенко Павел
    
    Задание: Разработка классов и объектов «запись», «комментарий» для 
    приложения «Блог» (использование наследования). '''

class Note(object):

    def __init__(self, note, media=None):
        self._note = note
        self._id = 0

    def writeNote(self):
        pass

class Comment(object):
    
    def __init__(self, comment):
        self._comment = comment

    def writeComment(self):
        pass

class App(Note, Comment): 

    def __init__(self):
        self.noteDataStorage = {} # id:[запись, коментарий, коментарий ....]
        self._id = 0 

    def writeNote(self, note):
        self._id += 1
        note._id = self._id
        self.noteDataStorage[note._id] = [note._note]
    
    def writeComment(self, note, comment):
        self.noteDataStorage[note._id].append(comment._comment)
    
    def showNotesAndComments(self):
        print(self.noteDataStorage)
        
    


blog = App() 

note = Note("Hello world", media=None)
comment = Comment("WOW you wrote  \"Hello world\" ")

blog.writeNote(note)
blog.writeComment(note, comment)
blog.showNotesAndComments()

# Считаю что использовал не самый лучший объекто ориентированный дизайн,
# сдесь более уместно не наследовать коментарии и записи, а сделать
# их полями приложения и использовать их как структуры данных.