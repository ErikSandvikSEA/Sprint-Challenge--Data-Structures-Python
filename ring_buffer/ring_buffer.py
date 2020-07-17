class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupants = []
        self.current_oldest_occupant_idx = 0

    def append(self, item):
        if len(self.occupants) < self.capacity:
            self.occupants.append(item)
        else:
            self.occupants[self.current_oldest_occupant_idx] = item
            if self.current_oldest_occupant_idx < len(self.occupants) - 1:
                self.current_oldest_occupant_idx += 1
            else:
                self.current_oldest_occupant_idx = 0

    def get(self):
        return self.occupants
