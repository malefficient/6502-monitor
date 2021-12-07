#Generate a 32Kb NOPSled of ROM
# to program: minipro -p AT28C256 -w rom.bin 
rom = bytearray( [0xea] * 32768)

rom[0x7ffc] = 0x00 #Little endian: 0x8000 -> 0x10000000
rom[0x7ffd] = 0x80 #                 A15   ----^
with open("rom.bin", "wb") as out_file:
    out_file.write(rom)
