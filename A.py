#coding:utf-8

''' 自定义类Member '''


class Member:
    __metaclass__ = type
    member_id = 0

    def __init__(self, name='song', tel=None, sex=None, age=None):
        self.name = name
        self.tel = tel
        self.sex = sex
        self.age = age

    def __iter__(self):
        return self

    def next(self):
        self.member_id = self.member_id+1
        if self.member_id > 10:
            raise StopAsyncIteration
        return self.member_id

    def getname(self):
        say = 'I am a baby.'
        print(say)
        return self.name


if __name__ == '__main__':
    m = Member()
    print('打印测结果', m.__iter__())
    get = m.getname()
    print(get)
    next1 = m.next()
    print('next', next1)



