# Author  : Bhishan Poudel
# Program : writehere.r
# Source  : Rscript example.r

# set working directory here
set_wd <- function() {
  library(rstudioapi) # make sure you have it installed
  current_path <- getActiveDocumentContext()$path 
  setwd(dirname(current_path ))
  print( getwd() )
}

print( getwd() )
set_wd()
print( getwd() )