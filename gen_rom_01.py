# Generate a 32Kb NOPSled of ROM
# to program: minipro -p AT28C256 -w rom.bin 
# Ben-Eater follow a long offset link: https://www.youtube.com/watch?v=yl8vPW5hydQ&t=1140s
rom = bytearray( [0xea] * 32768)

#Fill A register with immediate 0x42
rom[0] = 0xa9   #; LDA 0x42
rom[1] = 0x42   #; 

# Store the contents of A register at address 0x6000
rom[2] = 0x8d   #; OUT 0x6000, 0x42
rom[3] = 0x00   #; at  
rom[4] = 0x60   #;

# What happens on next CLK cycle? 

rom[0x7ffc] = 0x00 #Little endian: 0x8000 -> 0x10000000
rom[0x7ffd] = 0x80 #                 A15   ----^
with open("rom.bin", "wb") as out_file:
    out_file.write(rom)
