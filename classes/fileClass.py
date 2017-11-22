from __future__ import division
from Bio.Seq import Seq #Import Sequence BioPython
from Bio.Alphabet import generic_dna

class file:
    
    fasta=[]
    motifs=[]
    sumMotifs=[]
    numNmersMotifsDic = {}

    
    #Open files
    def openFile(self, fileAddress):
        self.fileAddress = fileAddress #File address
        self.file = open(self.fileAddress, 'r') #Open file

    #Print files
    def printFile(self):
        print (self.file.read())

    #Get sequence
    def sequence(self):
        line = ''
        meta = ''
        sequence = ''
        self.line = self.file.readline()
        while self.line:
            self.line = self.line.rstrip('\n')
            if '>' in self.line:
                meta = self.line
            else:
                sequence = self.line
                self.fasta.append(sequence) #Append sequence to list
            self.line=self.file.readline()

    #Print fasta list
    def printFasta(self):
        print (self.fasta)

    #Print length of fasta
    def getLenFasta(self):
        print (len(self.fasta))
    
    #Save motifs in list
    def motifList(self):
        for line in self.file:
            for motif in line.strip().split(','):
                self.motifs.append(motif)

    #Print motifs list
    def printMotif(self):
        print (self.motifs)

    #Print length of motifs
    def getLenMotif(self):
        print (len(self.motifs))
    
    #Calculate count of motifs in sequence
    def countMotif(self):
        pattern = ''
        countMotifs={}

        for i in range(len(self.fasta)):
            dna = self.fasta[i]
            my_dna = Seq(dna, generic_dna)

            for j in range(len(self.motifs)):

                pattern = self.motifs[j]
                #Number of repeat pattern
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))
            print (countMotifs)

    #Calculate number of n-mers motifs in sequence
    def numNmersMotifs(self):
        pattern = ''
        countMotifs={}

        for i in range(len(self.fasta)):
            dna = self.fasta[i]
            my_dna = Seq(dna, generic_dna)
           
            sum1ch = 0 #Number of 1-mers motifs
            sum2ch = 0 #Number of 2-mers motifs
            sum3ch = 0 #Number of 3-mers motifs
            sum4ch = 0 #Number of 4-mers motifs
            sum5ch = 0 #Number of 5-mers motifs

            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

            for value in countMotifs.keys():
                if (len(value) == 1):
                    temp = countMotifs[value] #This is a list
                    sum1ch += temp[0]
                elif (len(value) == 2):
                    temp = countMotifs[value]
                    sum2ch += temp[0]
                elif (len(value) == 3):
                    temp = countMotifs[value]
                    sum3ch += temp[0]
                elif (len(value) == 4):
                    temp = countMotifs[value]
                    sum4ch += temp[0]
                elif (len(value) == 5):
                    temp = countMotifs[value]
                    sum5ch += temp[0]

            self.numNmersMotifsDic[i] = []
            self.numNmersMotifsDic[i].append(sum1ch)
            self.numNmersMotifsDic[i].append(sum2ch)
            self.numNmersMotifsDic[i].append(sum3ch)
            self.numNmersMotifsDic[i].append(sum4ch)
            self.numNmersMotifsDic[i].append(sum5ch)
        

    #Calculate Frequency of motifs in sequence
    def frequencyMotifs(self):
        pattern = ''
        countMotifs={}

        for i in range(len(self.fasta)):
            dna = self.fasta[i]
            my_dna = Seq(dna, generic_dna)
            print ('Sequence', i+1)
           
            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

            for key, value in countMotifs.items():
                if (len(key) == 1):
                    temp = value[0] #This is a list
                    print ('Frequency of', key, '==>', (temp/self.numNmersMotifsDic[i][0])*100, '%')
                elif (len(key) == 2):
                    temp = value[0]
                    print ('Frequency of', key, '==>', (temp/self.numNmersMotifsDic[i][1])*100, '%')
                elif (len(key) == 3):
                    temp = value[0]
                    print ('Frequency of', key, '==>', (temp/self.numNmersMotifsDic[i][2])*100, '%')
                elif (len(key) == 4):
                    temp = value[0]
                    print ('Frequency of', key, '==>', (temp/self.numNmersMotifsDic[i][3])*100, '%')
                elif (len(key) == 5):
                    temp = value[0]
                    print ('Frequency of', key, '==>', (temp/self.numNmersMotifsDic[i][4])*100, '%')
