def do_anything(*args):
    count = len(args)
    print("受け取った値：{}".format(args))
    if count == 0:
        print("やることが無いので暇です")
    elif count == 1:
        if type(args[0]) is str:
            print("{}{}".format(args[0],args[0]))
        elif type(args[0]) is int:
            print(args[0]*2)
        else:
            print("難しくて無理です")
    elif count == 2:
        if type(args[0]) is int and type(args[1]) is int:
            print(args[0]+args[1])
        elif type(args[0]) is str and type(args[1]) is str:
            print("{}{}".format(args[0],args[1]))
        elif type(args[0]) != type(args[1]):
            print("できません～")
        else:
            print("無茶言わないで！")
    else :
        print("無理です…")




# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1,2,3])
do_anything(10,20)
do_anything(10,'abc')
do_anything('x','yz')
do_anything([1,2,3],[4,5,6])
do_anything(1,2,3)