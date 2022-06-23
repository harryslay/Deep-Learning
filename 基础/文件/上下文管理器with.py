'''
不需要手动关闭，离开with的时候会自动释放资源
'''
with open('a.txt','r') as file:
    print(file.read())

print(type(open('a.txt','r'))) #<class '_io.TextIOWrapper'>

'''
MyContentMgr实现了特殊方法__enter__()和__exit__() 称为该类对象遵守了上下文管理协议
该类对象的实例对象，称为上下文管理器
MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print("enter方法被调用执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了') # 不管有没有异常都自动退出

    def show(self):
        print("show方法被调用执行了")

with MyContentMgr() as file:
    file.show()


print("----------------------使用with实现一个图片复制")

with open('图片.png','rb') as src_file:
    with open("cp_img.png",'wb') as target_file:
        target_file.write(src_file.read())