# Huffman-Compression
This project represents understanding and implementation of a Compression Engine based on compressing textual data using the Huffman algorithm

# What it does?
This program can compress text files on your device to enable easier storage and transmission of the file

# How to use it
The process has a driver program inbuilt, and executing the core.py module should start it
There are two operations to choose from:
				a) Compression [To compress a given file]
				b) Decompression [To decompress a compressed file]
				
# Size reduction benchmarks:
1) Bible.txt [3.98kB] to Bible.bin [2.17kB]  (45.72% reduction in size)
2) SCC_DATA.txt [70.95MB] to SCC_DATA.bin [31.79MB] (55.19% reduction in size)

[The test data will be uploaded to this repository soon] 

# Note:
The program produces a copy of the compressed file. ie. The original file remains untouched.
Hence, to truly free up space, a user must delete the original file.

# Upcoming Features/Improvements:
1) Improvement to the Huffman Tree datastructure will speed up the process slightly [Already timed to be decent despite the messy-looking code]
2) Better decoding algorithm required
3) Addition of media compression using the same engine [Experimental and Unorthodox]
