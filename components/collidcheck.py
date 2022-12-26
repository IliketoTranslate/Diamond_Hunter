
# Uwaga: CollidChecker wola na kazdym posiadanym obiekcie getRect() do sprawdzania kolizji
# getRect musi zwrocic obiekt Rect zawierający jego ID, aby kolizje nie byly wykrywane z tym samym obiektem
class CollidChecker():
    def __init__(self, collection):
        self.collection = collection
        self.left_y_boundary = 10
        self.right_y_boundary = 850
        self.left_x_boundary = 10
        self.right_x_boundary = 1770
    def checkCollision(self, object, update):
        new_x, new_y = update
        _, updated_coord = object.getRect()
        #hint: this below moves object itself:)
        #updated_coord.move_ip(new_x, new_y)
        #x, y, w, h = updated_coord
        #print("before x:"+str(x)+" y:"+str(y))
        updated_coord = updated_coord.move(new_x, new_y)
        x, y, w, h = updated_coord
        #print("after x:"+str(x)+" y:"+str(y))
        if x < self.left_x_boundary or x > self.right_x_boundary or y < self.left_y_boundary or y > self.right_y_boundary:
            return False
        for el in self.collection:
            if object.getId() == el.getId(): continue
            _, coord_1 = el.getRect()
            if updated_coord.colliderect(coord_1):
                return True
        return False
