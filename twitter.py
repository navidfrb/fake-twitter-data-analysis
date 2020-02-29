punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):

    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word

def get_neg(str1):

    wrd_lst = str1.split(" ")
    c = 0

    for word in wrd_lst:
        fixed_word = strip_punctuation(word)
        if fixed_word in negative_words:
            c = c + 1
    return c

def get_pos(str1):

    wrd_lst = str1.split(" ")
    c = 0
    for word in wrd_lst:
        fixed_word = strip_punctuation(word)
        if fixed_word in positive_words:
            c = c+1
    return c

myFile = open ("project_twitter_data.csv", "r")
lines= myFile.readlines()

header = lines[0]
print(header)
field_names = header.strip().split(',')

total_pos = 0
total_neg = 0
total_retweet =0
total_rep = 0
tweets_no = len(lines) -1

   # print("Number of tweets: ", tweets_no)
    #print("Number of retweet: ", retweet_no)
    #print("Number of replies:", rep_no)
    #print("Number of positive words: ",pos_wrd_no)
    #print("Number of negative words: ",neg_wrd_no)

result = open ("resulting_data.csv","w")
result.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
result.write('\n')

for row in lines[1:]:
    values = row.strip().split(",")
    print(values[1])
    #pos_wrd_no = get_pos(values[0])
    #total_pos = total_pos + pos_wrd_no
    #neg_wrd_no = get_neg(values[0])
    #total_neg = total_neg + neg_wrd_no
    #net_score = pos_wrd_no - neg_wrd_no
    #retweet_no= int(values[1])
    #rep_no = int(values[2])
    #row_line = '{},{},{},{},{}'.format(retweet_no,rep_no,pos_wrd_no,neg_wrd_no,net_score)
    #result.write(row_line)
    #result.write('\n')
