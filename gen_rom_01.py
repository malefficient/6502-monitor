#Generate a 32Kb NOPSled of ROM
# to program: minipro -p AT28C256 -w rom.bin 
rom = bytearray( [0xea] * 32768)

with open("rom.bin", "wb") as out_file:
    out_file.write(rom)
