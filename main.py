from classes.fileClass import file #Import fileClass

#Create objects

fasta = file()
fasta.openFile("/home/parham/Documents/Python/DNA_Motif_PKG/importFiles/ebola.fasta")
fasta.sequence()
#fasta.printFasta()
#fasta.getLenFasta()


motif = file()
motif.openFile("/home/parham/Documents/Python/DNA_Motif_PKG/importFiles/motifs.txt")
motif.motifList()
#motif.printMotif()
#motif.getLenMotif()
#motif.countMotif()

motif.numNmersMotifs()
#print (motif.numNmersMotifsDic)

motif.frequencyMotifs()
