library(jsonlite)
library(tibble)

f <- stream_in(file("C:/Users/Ethan/Downloads/business.json"))
ff <- flatten(f)
df <- as_data_frame(ff)
df <- df[,c('business_id','name','categories')]
write.csv(df, file='E:/parsed_business.csv')

f <- stream_in(file("C:/Users/Ethan/Downloads/checkin.json"))
ff <- flatten(f)
df <- as_data_frame(ff)
write.csv(df, file='E:/parsed_checkin.csv')

f <- stream_in(file("C:/Users/Ethan/Downloads/review.json"))
ff <- flatten(f)
df <- as_data_frame(ff)
df <- df[df$stars==1,]
df <- df[,c('user_id','business_id','useful','text')]
write.csv(df, file='E:/parsed_review.csv')

f <- stream_in(file("C:/Users/Ethan/Downloads/user.json"))
ff <- flatten(f)
df <- as_data_frame(ff)
df <- df[df$review_count==1,]
df <- df[df$average_stars==1,]
df <- df[,c('user_id')]
write.csv(df, file='E:/parsed_user.csv')
