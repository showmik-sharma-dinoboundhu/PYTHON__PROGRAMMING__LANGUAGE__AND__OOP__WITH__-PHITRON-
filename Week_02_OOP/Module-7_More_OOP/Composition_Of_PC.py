class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size

class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity = capacity


class Computer:
    def __init__(self,cores,ram_size,hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hardDisc = HardDrive(hd_capacity)

    def __str__(self) -> str:
        return f"{self.cpu.cores} {self.ram.size} {self.hardDisc.capacity}"

Lenevo = Computer(8,16,512)
print(Lenevo)