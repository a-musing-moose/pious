class Logger():
    
    template = "Watch item encountered:\n\tBefore: %s\n\tAfter: %s"
    
    def log_transform(self, data_in, data_out):
        self._emit(self._get_message(data_in, data_out))
    
    def _get_message(self, data_in, data_out):
        return self.template % (data_in, data_out)
    
    def _emit(self, msg):
        pass
    
class ConsoleLogger(Logger):
    
    def _emit(self, msg):
        print(msg)