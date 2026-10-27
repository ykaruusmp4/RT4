class RichCPU:
    def __init__(self):
        self.reg_A = 0x0
        self.reg_B = 0x0
        self.pc = 0x0
        self.flag_Z = 0
        self.flag_O = 0
        self.ram = [0x0] * 16
        self.OP_MOVE = 0b00
        self.OP_EXCOR = 0b01
        self.OP_JUMP = 0b10
        self.OP_LOADB = 0b11

    def write_ram(self, endereco, valor):
        if 0 <= endereco < 16:
            self.ram[endereco] = valor & 0x0F

    def ciclo_clock(self):
        if self.pc >= 16:
            self.pc = 0x0

        instrucao = self.ram[self.pc]

        opcode = (instrucao & 0b1100) >> 2
        dado = instrucao & 0b0011

        proximo_pc = (self.pc + 1) & 0x0F

        if opcode == self.OP_MOVE:
            self.reg_A = dado & 0x0F
        elif opcode == self.OP_EXCOR:
            self.reg_A = (self.reg_A ^ self.reg_B) & 0x0F
            self.flag_Z = 1 if self.reg_A == 0 else 0
        elif opcode == self.OP_JUMP:
            if self.reg_A != 0:
                proximo_pc = dado & 0x0F
        elif opcode == self.OP_LOADB:
            self.reg_B = dado & 0x0F

        self.pc = proximo_pc

    def obter_status_str(self):
        bin_A = f"{self.reg_A:04b}"
        bin_B = f"{self.reg_B:04b}"
        bin_PC = f"{self.pc:04b}"
        return {
            "A": f"REG A: 0x{self.reg_A:X} ({bin_A})",
            "B": f"REG B: 0x{self.reg_B:X} ({bin_B})",
            "PC": f"PC: 0x{self.pc:X} ({bin_PC})",
            "FLAGS": f"FLAGS: Z={self.flag_Z} O={self.flag_O}",
        }
