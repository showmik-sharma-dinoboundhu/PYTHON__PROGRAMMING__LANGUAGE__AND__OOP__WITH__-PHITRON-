class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,capacity) -> None:
        self.capacity = capacity

class HardDrive:
    def __init__(self,storage) -> None:
        self.storage = storage

class SSD:
    def __init__(self,memory) -> None:
        self.memory = memory

class Processor:
    def __init__(self,intel,amd) -> None:
        self.intel = intel
        self.amd = amd


class Computer:
    def __init__(self,cores,capacity,storage,memory,intel,amd) -> None:
        self.cores = CPU(cores)
        self.capacity = RAM(capacity)
        self.harddisk = HardDrive(storage)
        self.ssd = SSD(memory)
        self.processor = Processor(intel,amd)

    def __str__(self) -> str:
        return f"My Laptop is Lenevo Ideapad S145. My CPU has {self.cores.cores} cores. Capacity, HardDisk and SSD is {self.capacity.capacity}, {self.harddisk.storage}, {self.ssd.memory}. It's processor {self.processor.intel}"


Lenevo = Computer(16,512,256,"2TB","Core i3 Gen-10","NOT AMD")
print(Lenevo)