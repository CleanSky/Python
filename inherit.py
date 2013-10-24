#!/usr/bin/python
#面向对象的编程带来的好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
#继承完全可以理解成类之间的类型和子类型关系。



#Filename: inherit.py
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        print("(Initialized School Member:%s)" %self.name);

    def tell(self):
        '''Tell my details.'''
        print('Name:%s, Age:%s' %(self.name, self.age));

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age);
        self.salary = salary;
        print('(Initialized Teacher:%s)' %self.name);

    def tell(self):
        SchoolMember.tell(self);
        print('Salary:%d' %self.salary);

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age);
        self.marks = marks;
        print("(Initialized Student:%s)" %self.name);

    def tell(self):
        SchoolMember.tell(self);
        print("Marks:%d" %self.marks);

t = Teacher('Mrs. Shrividya', 40, 30000);
s = Student('Swaroop', 22, 75);

print#prints a blank line

members = [t, s];
for member in members:
    member.tell();#works for both Teachers and Students
