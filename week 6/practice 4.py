class TextEditor:
    def __init__(self):
        self.content = ''
        self.undo_stack = []
        
    def write(self, teks):
        self.undo_stack.append(self.content)
        self.content += teks
        print (f'Tulis: {self.content}')
        
    def undo(self):
        if self.undo_stack:
            self.content = self.undo_stack.pop()
            print(f'UNDO → {self.content}')
        else:
            print('Tidak bisa undo lagi!')
        
editor = TextEditor()
editor.write('Halo')
editor.write(' Dunia')
editor.write('!')
editor.undo()
editor.undo()