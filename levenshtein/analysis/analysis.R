
rm(list=ls())
frame <- read.delim("../results/results1.dat")

morr <- frame[frame$word=="morrissey", ]
counter <- frame[frame$word=="counterrevolutionaries", ]

barplot(t(as.matrix(morr[morr$sample==20, c(4, 5)])), 
        beside=TRUE, 
        col=c("pink", "lightblue"),
        names.arg=c("99%", "98%", "95%", "90%", "85%", 
                    "80%", "75%", "70%"),
        xlab="OCR character accuracy",
        ylab="P(success)",
        main=paste0("COMPARISON OF SPELLING CORRECTION ACCURACY",
                    "\nword: 'morrissey' & # of occurences: 20"))
lgd.text <- c("chance", "levenshtein")
# due to a bug in R 3.0, the location must be hardcoded
legend(18, 1,
       lgd.text,
       fill=c("pink", "lightblue"),
       cex=0.8,
       bty="n")


rm(list=ls())

frame <- read.delim("../results/results2.dat")

plot(frame$exp, type="l", col="blue", lwd=5,
     ylab="P(success)",
     xlab="number of occurences in document",
     main=paste0("Identification accuracy as a function of",
                 "\nnumber of occurences of word in document"))
lines(frame$chance, type="l", col="red", lwd=5)
lgd.text <- c("chance", "levenshtein")
# due to a bug in R 3.0, the location must be hardcoded
legend(35, .8,
       lgd.text,
       fill=c("red", "blue"),
       cex=0.8,
       bty="n")




