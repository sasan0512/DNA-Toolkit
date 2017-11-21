#Calculate number of n-mers motifs in sequence
def numNmersMotifs(self):
    pattern = ''

    for i in range(len(self.fasta)):
        dna = self.fasta[i]
        my_dna = Seq(dna, generic_dna)

        countOldPattern = 0
        sum = 0
        flag = True

        for j in range(len(self.motifs)):
            pattern = self.motifs[j]

            if (len(self.motifs[j]) != len(self.motifs[j-1])):

                oldPattern = self.motifs[j-1]
                self.sumMotifs.append(sum)
                print (sum)
                sum = 0
                flag = False
                countOldPattern = my_dna.count_overlap(pattern)
                print (oldPattern)
            else:

                if (flag == True):
                    print (self.motifs[j-1])
                    sum += (my_dna.count_overlap(pattern))
                else:
                    print (self.motifs[j-1])
                    sum += (my_dna.count_overlap(pattern) + countOldPattern)
                    flag = True
print(self.sumMotifs)

