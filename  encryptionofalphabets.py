alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
S = raw_input("enput your sentence")
a=(S.lower())
b = list(a)
i=0
sum_of_sentence=0
string = ' '
sentence = ' '
sentence_num = {}
num=[]
while i<len(b):
    if b[i]==" ":

        sentence_num[sum_of_sentence]=string
        num.append(sum_of_sentence)
        string=' '
        sum_of_sentence = 0
    else:
        sum_of_sentence = sum_of_sentence + (alpha[a[i]])
        string+=b[i]

    i+=1
num.append(sum_of_sentence)
# print num
p=0
while p<len(num):
    k=0
    while k<len(num)-1:
        if num[k]>num[k+1]:
            num[k],num[k+1]=num[k+1],num[k]
        k+=1
    p+=1
# print num
sentence_num[sum_of_sentence]=string
j=0
while j<len(num):
    print(sentence_num[num[j]]),
    j+=1
























# j=0
# string = ' '
# sentence = ' '

# while j<len(b):
#     if b[j]==" ":
#         sentence+=(string)
#         string=' '
#         print "hfkjdshfjk"
#     else:
#         string+=b[j]
#     j+=1
# sentence+=(string)
# print sentence

