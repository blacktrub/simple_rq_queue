import time

from redis import Redis
from rq import Queue

from utils import func


def main() -> None:
    q = Queue(connection=Redis())

    for n in range(10):
        job = q.enqueue(func, n)
        time.sleep(1)
        print(job.result)


if __name__ == '__main__':
    main()