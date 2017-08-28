import time
from redis import Redis
from rq.decorators import job


class async(job):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.queue = 'default'
        self.connection = Redis()


def func(n: int) -> None:
    print('n:', n)
    return n ** 2


@async()
def async_func(n: int) -> int:
    print('call async_fun:', n)
    return (n ** 2) * 2
