class Logger:

    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        should_print = True
        if message in self.log and timestamp < self.log[message]:
            should_print = False
        else:
            self.log[message] = timestamp + 10
        return should_print

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
