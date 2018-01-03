# standard agent initialization
import time
import newrelic.agent
newrelic.agent.initialize()

# register application since this is a background task
newrelic.agent.register_application(timeout=3.0)

@newrelic.agent.background_task()
def hello_world():
    for x in range(0, 5):
        print("Hello World")
        time.sleep(1)

if __name__ == '__main__':
    hello_world()

