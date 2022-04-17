Last run on: Python 3.9.7. 

Genome assembly of real DNA sequencing data is still a challenging area where many researchers are currently working. This project focuses on a simplified version of the problem using simulated data. The simulation emulates the process of sampling reads from a longer piece of DNA (similar to the output of a DNA sequencing experiment). The program can also construct a De Bruijn graph from a set of reads, and output a visualization of the graph as a .DOT file.

de_bruijn.py contains the class and methods for making the De Bruijn graph. Run everything in main.py, including the simulation and the graph construction. Depending on the user input, the program will know whether to run the simulation or assemble the graph. 


How to compile: 

1. To simulate the data:\
Go to main.py. On line 66, change "reads.txt" to the desired output file name for the reads file. 

simulate.sh will take in the following parameters (in this order):\
  • FASTA sequence file (string) - File containing a DNA sequence.\
  • Coverage (integer) - The coverage of the simulated sequencing experiment.\
  • Read length (integer) - The length of reads to simulate.\
  • Error rate (float) - The sequencing error rate (between 0 and 1).\

An example is ./simulate.sh sample_c12_r_50_e0.00.txt 12 50 0.00. 


2. To create the de Bruijn Graph\
assemble.sh will take in the following parameters (in this order):\
  • Reads file (string) - A file of reads, as output by simulate.sh.\
  • k (int) - the size of k-mer to use when building a De Bruijn graph.\

An example is ./assemble.sh sample_c12_r_50_e0.00.txt 13. 








