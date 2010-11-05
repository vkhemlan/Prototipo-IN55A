class RoleList:
    def __init__(self, user):
        self.roles = list()
        self.roles.extend(user.courseinstance_set.all())
        self.roles.extend(user.auxiliary_set.all())
        self.roles.extend(user.assistant_set.all())
        self.roles.extend(user.student_set.all())
        
        self.roles.sort(key = lambda x: x.course_instance.get_value(), reverse = True)
                
    def set_default(self, selected_class, selected_id):
        selected_id = int(selected_id)
        
        for role in self.roles:
            if role.__class__ == selected_class and role.id == selected_id:
                role.selected = True
                
    def is_empty(self):
        return len(self.roles) == 0
                
    def get(self, index):
        return self.roles[index]
        
    def __iter__(self):
        self.current = 0
        return self
        
    def next(self):
        if self.current == len(self.roles):
            raise StopIteration
        else:
            self.current += 1
            return self.roles[self.current - 1]
