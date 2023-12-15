from celery import Celery
from time import sleep


redis_url = "redis://localhost:6379"
app = Celery("tasks", backend=redis_url, broker=redis_url)

@app.task
def add(x, y):
    print(f"adding {x} and {y}")
    return x + y


@app.task
def slow_add(x, y):
    print(f"very slowly adding {x} and {y}")

    seconds = 60
    while seconds > 0:
        sleep(1)
        print("still sleeping")
        seconds -= 1

    print(f"yawnnn sorry I was sleepy, here you go")
    return x + y