import sys
from random import *
import math
import de_bruijn

#Given a file in the FASTA format, returns the the sequence as a string. 
def read_single_fasta(filename):
    f = open(filename, "r")  # Open file
    f.readline()  # Skip first line
    lines = f.readlines()
    seq = ""
    for line in lines:
        seq += line.strip()
    return seq.upper()


# Given a FASTA file, returns a bunch of reads. 
def create_reads(filename, coverage, length):
    genome = read_single_fasta(filename)

    # Math stuff
    G = len(genome)
    N = math.floor((coverage * G) / length)

    reads = []
    for i in range(N):
        # This ensures we don't get a read not long enough
        index = randrange(0, G - length)
        reads.append(genome[index:index + length])

    #Return a list of all our reads
    return reads




# # With these reads, we add error to them

def add_error(read, error):
    # We take one read at a time, and return a string
    new_str = ""
    # Go through every character in the read
    for i in range(len(read)):
        letters = ['A', 'T', 'C', 'G']
        # Math to check if we add error
        if uniform(0, 1) < error:
            letters.pop(letters.index(read[i]))
            new_str += choice(letters)
        else:
            new_str += read[i]

    return new_str





# This brings it all together!
def simulate(genome_file, C, L, E):
    # We get a sample without error
    correct_sample = create_reads(genome_file, C, L)
    return_reads = []
    # We add error and get a fresh list
    for str_reads in correct_sample:
        return_reads.append(add_error(str_reads, E))
    print(len(set(return_reads)))
    # We create our reads file for our graph!
    file_str = "\n".join(return_reads)
    with open("sample_c12_r_50_e0.01.txt", "w") as f:   #change reads.txt to the desired file name
        f.write(file_str)


if __name__ == "__main__":
    if sys.argv[5] == 'simulate':
        genome = sys.argv[1]
        C = int(sys.argv[2])
        L = int(sys.argv[3])
        E = float(sys.argv[4])
        simulate(genome, C, L, E)
    elif sys.argv[5] == 'assemble':
        read_file = sys.argv[1]
        kmer = int(sys.argv[2])
        bruijn = de_bruijn.Bruijn(read_file, kmer)
        bruijn.make_graph()