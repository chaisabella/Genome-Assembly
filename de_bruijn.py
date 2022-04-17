''' Takes in as input a .txt file containing the reads, and outputs the reads as a list.'''
def read_txt_file(f):
    with open(f) as file:
        lines = file.readlines()
        reads = []
        for line in lines:
            reads += [line.rstrip()]
    return reads


'''Constructs a de Bruijn graph as an adjacency list, from a set of reads with k length word.'''
class Bruijn:

    def __init__(self, reads, kmer):
        self.reads = read_txt_file(reads) #get reads as a list
        self.kmer = kmer
        self.adjacency_list = {}
        self.edges = 0
        self.vertices = 0

    def get_kmers(self, read):
        kmers = []
        for i in range(len(read) - self.kmer + 1):
            kmers.append([read[i:(i + self.kmer - 1)], read[(i + 1):(i + self.kmer)]])
        return kmers

    def make_graph(self):
        # go through all the reads
        for read in self.reads:
            # for a read, get a list of kmers (see get_kmers)
            kmers = self.get_kmers(read)

            # iterate through all the k-1mer pairs (left and right)
            for pair in kmers:
                # if the left thing is not already a node, we make a node of it
                if not pair[0] in self.adjacency_list.keys():

                    # the value is the node it goes to and the edge
                    self.adjacency_list[pair[0]] = [pair[1], pair[0] + pair[1][-1:]]
                    self.vertices += 1
                    self.edges += 1

                # otherwise, the node already exists!
                else:
                    #check if the corresponding edge-node value pair doesn't exist
                    does_not_exist = True 
                    if pair[1] in self.adjacency_list[pair[0]] and pair[0] + pair[1][-1:] in self.adjacency_list[pair[0]]:
                        x = self.adjacency_list[pair[0]].index(pair[1])
                        if pair[0] + pair[1][-1:] == self.adjacency_list[pair[0]][x + 1]:
                            does_not_exist = False
                    if does_not_exist:
                        if self.adjacency_list[pair[0]] == ['', '']:
                            self.adjacency_list[pair[0]] = [pair[1], pair[0] + pair[1][-1:]]

                        # otherwise, we just add the new node-edge pair
                        else:
                            self.adjacency_list[pair[0]] += [pair[1], pair[0] + pair[1][-1:]]
                        self.edges += 1
                # if the node we are going to is not already in our adjacency list, we make it!
                if not pair[1] in self.adjacency_list.keys():
                    self.adjacency_list[pair[1]] = ['', '']
                    self.vertices += 1
        print("Number of vertices in graph:", self.vertices)
        print("Number of edges in graph:", self.edges)



        if self.vertices < 30: 
            for key in self.adjacency_list:
                print(self.adjacency_list[key])

    
    def make_dot_content(self):
        '''Method to write the .dot file. '''

        lines = []
        lines.append("digraph mygraph{")
        for key in self.adjacency_list:
            i = 0
            while i < len(self.adjacency_list[key]):
                lines.append('\t"'+key+'"->"'+self.adjacency_list[key][i]+'"')
                i += 2
        lines.append("}")

        with open("graph.dot", "w") as f:
            f.write('\n'.join(lines))

