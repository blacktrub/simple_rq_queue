import time

from redis import Redis
from rq import Queue, decorators

from utils import func, async_func


def main() -> None:
    q = Queue(connection=Redis())

    for n in range(10):
        job = q.enqueue(func, n)
        time.sleep(1)
        print(job.result)


if __name__ == '__main__':
    main()
    async_func.delay(10)
