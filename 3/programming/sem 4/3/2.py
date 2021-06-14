''' Автор: Гришутенко Павел
    
    Задание: Создание геттеров и сеттеров для классов «запись», «комментарий»
    приложения «Гостевая книга». Создание функций для вывода на печать
    информации, хранящийся в объектах.

'''

class Note(object):

    def __init__(self, note, media=None):
        self._note = note
        self._id = 0
    
    @property
    def note(self):
        return self._note
    
    @note.setter
    def note(self, note):
        self._note = note
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, noteID):
        self._id = noteID

    def writeNote(self):
        pass

class Comment(object):
    
    def __init__(self, comment):
        self._comment = comment

    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, comment):
        self._comment = comment

    def writeComment(self):
        pass

class App(Note, Comment): 

    def __init__(self):
        self.noteDataStorage = {} # id:[запись, коментарий, коментарий ....]
        self._id = 0
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, noteID):
        self._id = noteID
    
    def writeNote(self, note):
        self._id += 1
        note._id = self._id
        self.noteDataStorage[note._id] = [note._note]
    
    def writeComment(self, note, comment):
        self.noteDataStorage[note._id].append(comment._comment)
    
    def showNotesAndComments(self):
        print(self.noteDataStorage)
        
    

guestbook = App() 

note = Note("Thank you for your good service.", media=None)
comment = Comment("We are glad that you liked it.")

note2 = Note("Thank you for your good service.", media=None)
comment2 = Comment("We are glad that you liked it.")

guestbook.writeNote(note)
guestbook.writeComment(note, comment)

guestbook.writeNote(note2)
guestbook.writeComment(note2, comment2)

guestbook.showNotesAndComments()
