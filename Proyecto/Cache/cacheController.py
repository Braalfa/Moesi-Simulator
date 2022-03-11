from Enums.cpuActionEnum import CPUAction
from Enums.stateEnum import State
from Cache.cacheL1 import CacheLine
from Cache.cacheL1 import Cache
from Communication.messaging import Message
from Communication.messaging import MessageType
import time


# TODO: Include eviction
# TODO: protect shared resources

class CacheController:
    def __init__(self, cache: Cache):
        self.cache = cache
        self.received_messages_queue = []
        self.send_messages_queue = []

    def write_request(self, address: int, new_value: str):
        state = self.cache.obtain_address_state(address)
        self.transition_by_cpu(state, CPUAction.WRITE, address, new_value)

    def read_request(self, address):
        state = self.cache.obtain_address_state(address)
        data = self.transition_by_cpu(state, CPUAction.READ, address)
        return data

    def receive_message_from_bus(self, message: Message):
        if message.message_type == MessageType.READ_MISS \
                or message.message_type == MessageType.WRITE_MISS:
            self.transition_by_bus(message)
        else:
            self.received_messages_queue.append(message)

    def transition_by_cpu(self, current_state: State,
                          action: CPUAction, address: int, new_value: str = None):
        if current_state == State.I:
            return self.transition_by_cpu_from_I(action, address, new_value)
        elif current_state == State.S:
            return self.transition_by_cpu_from_S(action, address, new_value)
        elif current_state == State.E:
            return self.transition_by_cpu_from_E(action, address, new_value)
        elif current_state == State.O:
            return self.transition_by_cpu_from_O(action, address, new_value)
        elif current_state == State.M:
            return self.transition_by_cpu_from_M(action, address, new_value)

    def transition_by_cpu_from_I(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            block = self.cache.select_block_to_overwrite(address)
            self.broadcast_read_miss(address)
            sharers_found = self.are_there_sharers(address)
            if not sharers_found:
                self.ask_data_from_memory(address)
                self.obtain_data_and_overwrite_existing_block(block, address)
                block.state = State.E
            else:
                self.obtain_data_and_overwrite_existing_block(block, address)
                block.state = State.S
            return block.data
        elif action == CPUAction.WRITE:
            self.broadcast_write_miss(address)
            next_state = State.M
            self.cache.write(address, new_value, next_state)

    def transition_by_cpu_from_S(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.S
            return self.cache.read_and_update_state(address, next_state)
        elif action == CPUAction.WRITE:
            self.broadcast_write_miss_2(address)
            next_state = State.M
            self.cache.write(address, new_value, next_state)

    def transition_by_cpu_from_E(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.E
            return self.cache.read_and_update_state(address, next_state)
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.cache.write(address, new_value, next_state)

    def transition_by_cpu_from_O(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.O
            return self.cache.read_and_update_state(address, next_state)
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.broadcast_write_miss_2(address)
            self.cache.write(address, new_value, next_state)

    def transition_by_cpu_from_M(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.M
            return self.cache.read_and_update_state(address, next_state)
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.cache.write(address, new_value, next_state)

    def transition_by_bus(self, message: Message):
        current_state = self.cache.obtain_address_state(message.address)
        if current_state == State.I:
            pass
        elif current_state == State.S:
            return self.transition_by_bus_from_S(message)
        elif current_state == State.E:
            return self.transition_by_bus_from_E(message)
        elif current_state == State.O:
            return self.transition_by_bus_from_O_and_M(message)
        elif current_state == State.M:
            return self.transition_by_bus_from_O_and_M(message)

    def transition_by_bus_from_S(self, message: Message):
        if message.message_type == MessageType.READ_MISS:
            next_state = State.S
            self.cache.update_state(message.address, next_state)
            self.return_shared_to_bus(message.address)
        elif message.message_type == MessageType.WRITE_MISS or \
                MessageType.WRITE_MISS_2:
            next_state = State.I
            self.cache.update_state(message.address, next_state)

    def transition_by_bus_from_E(self, message: Message):
        if message.message_type == MessageType.READ_MISS:
            next_state = State.S
            self.cache.update_state(message.address, next_state)
            self.return_shared_to_bus(message.address)
            self.supply_data_to_bus(message.address, self.cache.read(message.address))
        elif message.message_type == MessageType.WRITE_MISS:
            next_state = State.I
            self.cache.update_state(message.address, next_state)

    def transition_by_bus_from_O_and_M(self, message: Message):
        if message.message_type == MessageType.READ_MISS:
            next_state = State.O
            self.cache.update_state(message.address, next_state)
            self.return_shared_to_bus(message.address)
            self.supply_data_to_bus(message.address, self.cache.read(message.address))
        elif message.message_type == MessageType.WRITE_MISS:
            next_state = State.I
            self.cache.update_state(message.address, next_state)

    def broadcast_read_miss(self, address: int):
        self.send_message_to_bus(MessageType.READ_MISS, address)

    def broadcast_write_miss(self, address: int):
        self.send_message_to_bus(MessageType.WRITE_MISS, address)

    def broadcast_write_miss_2(self, address: int):
        self.send_message_to_bus(MessageType.WRITE_MISS_2, address)

    def ask_data_from_memory(self, address: int):
        self.send_message_to_bus(MessageType.REQUEST_FROM_MEMORY, address)

    def are_there_sharers(self, address: int):
        message = self.await_message_from_bus(MessageType.SHARED_RESPONSE, address)
        if message is not None:
            return True
        else:
            return False

    def return_shared_to_bus(self, address: int):
        self.send_message_to_bus(MessageType.SHARED_RESPONSE, address)

    def supply_data_to_bus(self, address: int, data: str):
        self.send_message_to_bus(MessageType.DATA_RESPONSE, address, data=data)

    def obtain_data_and_overwrite_existing_block(self, block: CacheLine, address: int):
        data = self.read_data_from_bus(address)
        self.cache.overwrite_block(data, address, block)

    def read_data_from_bus(self, address: int):
        message = self.await_message_from_bus(MessageType.DATA_RESPONSE, address)
        return message.data

    # TODO: Adjust time
    def await_message_from_bus(self, message_type: MessageType,
                               address: int, max_time: int = 10000) -> Message | None:
        start = time.time()
        while time.time() - start < max_time:
            for i in range(len(self.received_messages_queue)):
                message = self.received_messages_queue[i]
                if message.message_type == message_type and message.address == address:
                    self.received_messages_queue.pop(i)
                    return message
        return None

    def send_message_to_bus(self, message_type: MessageType, address: int, destinations=None, data=None):
        message = Message(message_type, self.cache.cache_number, destinations, address, data)
        self.send_messages_queue.append(message)
