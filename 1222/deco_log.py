import datetime
def log_file(func):
    def funcname(*args, **kwargs):
        LOG_FILENAME = 'python.log'
        dt_now = datetime.datetime.now()
        with open(LOG_FILENAME, 'a')as f:
            f.write(f'{dt_now}function:{func.__name__}args:{args} kwargs:{kwargs}\n')
        result = func(*args,**kwargs)
        return result
    return funcname
# main
# 呼び出した関数の情報をファイルに出力する log_file( )デコレータを作成する。
# テスト用の関数を定義し、正しく実行しているかを確認する main 部分は以下の通り
@log_file
def test(n):
    print('test->{}'.format(n))
# 呼出
test(100)
# 呼出
for i in range(5):
    test(i)
