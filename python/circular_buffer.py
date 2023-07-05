class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_read = 0
        self.buffer = [[] for i in range(self.capacity)]
        

    def read(self):
        if not any(self.buffer):
            raise BufferEmptyException('Circular buffer is empty')
        if self.last_read > len(self.buffer)-1:
            self.last_read = 0
        for slot in self.buffer[self.last_read]:
            if slot:
                self.last_read += 1
                self.buffer[self.last_read - 1] = []
                return slot
        for slot in self.buffer[:self.last_read]:
            if slot:
                self.last_read = self.buffer.index(slot)
                self.buffer[self.last_read] = []
                return slot
            

    def write(self, data):
        if all(self.buffer):
            raise BufferFullException("Circular buffer is full")
        for slot in self.buffer:
            if not slot:
                self.buffer[self.buffer.index(slot)] = data
                break
            
            
    def clear(self):
        self.buffer = [[] for i in range(self.capacity)]
        
        
    def overwrite(self, data):
        if all(self.buffer):
            self.last_read += 1
            self.buffer[self.last_read - 1] = data
        else:
            self.write(data)
