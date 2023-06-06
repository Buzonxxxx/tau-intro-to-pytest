class Accumulator:
    def __init__(self):
        #private
        self._count = 0
    
    # property decorator 將 class (類) 的方法轉換為 只能讀取的 屬性
    @property
    def count(self):
        return self._count
    
    def add(self, more=1):
        self._count += more
