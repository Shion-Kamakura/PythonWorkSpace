import time
def run_time(func):
    def funcname(*args,**kwargs):
        # このstarttrimはこの処理までにかかった時間
        starttrim = time.time()
        result = func(*args,**kwargs)
        # このstarttrimをひくことで関数の処理にかかった時間だけを計算する
        # func.__name__は関数の名前を表示してくれる
        print(f'実行関数:{func.__name__} 実行時間:{time.time() - starttrim}')
        return result
    return funcname

# main
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)
test(3)
test(5)
