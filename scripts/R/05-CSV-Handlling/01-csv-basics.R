setwd("~/")
getwd()
set_wd()
getwd()
students <- read.csv(file="users-data.csv", head=TRUE, sep=",")
print (students)
summary(students)

print (students$name)
students$name
print (students$fullname)
names(students)

