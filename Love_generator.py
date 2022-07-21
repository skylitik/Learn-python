
from distutils.command.check import check
from collections import defaultdict
from functools import total_ordering

print('''
        hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&
        &            hugs&kisses&hugs&kisses&hu         &hugs&kisses
        s&h        es&hugs&kisses&hugs&kiss                 gs&kisse
        es&h      sses&hugs&kisses&hugs&k                     s&kiss
        ses&      isses&hugs&kisses&hugs            &kiss      s&kis
        sses      kisses&hugs&kisses&hu           ugs&kiss      s&ki
        isse      &kisses&hugs&kisses&h          &hugs&kiss     gs&k
        kiss      s&kisses&hugs&kisses&         es&hugs&kis     ugs&
        &kis      gs&kisses&hugs&kisses        sses&hugs&k      hugs
        s&ki      ugs&kisses&hugs&kisse       kisses&hugs       &hug
        gs&k      hugs&kisses&hugs&kiss      s&kisses&hu        s&hu
        ugs&      &hugs&kisses&hugs&kis     ugs&kisses&         es&h
        hugs      s&hugs&kisses&hugs& i     hugs&kisse          ses&
        &hug      es&hugs&kisses&hug  k      hugs&kis           sses
        s&hu      ses&hugs&kisses&h   &       hugs&             isse
        es&h      sses&hugs&kisse     s&                       &kiss
        s                             gs&ki                 hugs&kis
        s                             ugs&kisse         sses&hugs&ki
        i             ses&h                                        k
        k             sses&                                        &
        &kis      gs&kisses&hug   isses&hugs      s&hugs&kisse     s
        s&kis      gs&kisses&h   &kisses&hug      es&hugs&kisses   g
        gs&ki      ugs&kisses&   s&kisses&hu      ses&hugs&kisses  u
        ugs&ki      ugs&kisse   ugs&kisses&h      sses&hugs&kisses h
        hugs&k      hugs&kiss   hugs&kisses&      isses&h gs&kisses&
        &hugs&k      hugs&ki   s&hugs&kisses      kisses  ugs&kisses
        s&hugs&      &hugs&k   es&hugs&kisse              hugs&kisse
        es&hugs&      &hugs   sses&hugs&kiss      s&kiss  &hugs&kiss
        ses&hugs      s&hug   isses&hugs&kis      gs&kiss s&hugs&kis
        sses&hugs      s&h   &kisses&hugs&ki      ugs&kisses&hugs& i
        isses&hug      es&   s&kisses&hugs&k      hugs&kisses&hug  k
        kisses&hug      e   ugs&kisses&hugs&      &hugs&kisses&h   &
        &kisses&hu          hugs&kisses&hugs      s&hugs&kisse     s
        s&kisses&hu        s&hugs&kisses                           g
        gs&kisses&h        es&hugs&kisse                           u
        ugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&h ''')

print("Welcome to the Love Calculator!")


name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name_sum = name1.lower() + name2.lower()
c = ['t','r','u','e']
d = ['l','o','v','e']
count1 = 0
count2 = 0
for key1 in name_sum:
    if str(key1) in c:
        count1 +=1
for key2 in name_sum:
    if str(key2) in d:
        count2 +=1

total = int(str(count1) + str(count2))  


if total < 10 or total > 90:
    print(f"Your score is %{total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is %{total}, you are alright together.")
else:
    print(f"Your score is %{total}")
    


