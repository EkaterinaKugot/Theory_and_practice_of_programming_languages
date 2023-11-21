from enum import Enum
import json


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.add_child(self)

    def add_child(self, child: "Widget"):
        self.children.append(child)

    def __str__(self):
        return f"{self.__class__.__name__}{self.children}"

    def __repr__(self):
        return str(self)
    
    def to_binary(self):
        res = {}
        c = 0
        for child in self.children:
            key, value, ch = child.to_binary() 
            if key in res.keys():
                key += str(c) 
            if len(ch) == 0: #нет детей
                res[key] = value
            else:
                res[key] = [value, ch]
            c += 1
        result = {}
        if (self.__class__.__name__ == 'MainWindow'):
            result[self.title] = res
        elif (self.__class__.__name__ == 'Layout'):
            a = 1
            if self.alignment == Alignment.VERTICAL:
                a = 2
            return 'lt', a, res
        elif (self.__class__.__name__ == 'LineEdit'):
            return 'le', self.max_length, res
        elif (self.__class__.__name__ == 'ComboBox'):
            return 'cb', self.items, res
         
        return json.dumps(result)
    
    @classmethod
    def watching_children(self, rt, data):
        for key in data.keys():
            root = rt
            if 'lt' in key:
                a = Alignment.HORIZONTAL
                if data[key][0] == 2:
                    a = Alignment.VERTICAL
                root = Layout(root, a)
                Widget.watching_children(root, data[key][1])
            elif 'le' in key:
                LineEdit(root, data[key])
            elif 'cb' in key:
                ComboBox(root, data[key])
        return rt      

    @classmethod
    def from_binary(self, data):
        data = json.loads(data)
        root = MainWindow(list(data.keys())[0])
        if isinstance(data[root.title], dict):
            root = Widget.watching_children(root, data[root.title])
        return root


class MainWindow(Widget):

    def __init__(self, title: str):
        super().__init__(None)
        self.title = title


class Layout(Widget):

    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment


class LineEdit(Widget):

    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length

class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items


app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(app)

bts = app.to_binary()
print(f"Binary data length {len(bts)}")
print(bts)

new_app = MainWindow.from_binary(bts)
print(new_app)

print(new_app.children[1].children[1].items)