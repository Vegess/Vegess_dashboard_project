import time
now = time.ctime()
qna = {
    "hi":"hey",
    "how are you":"i am fine",
    "what is your name":"i am jarvis",
    "where are you from?":"i am from vision techno Ai",
    "what is the time now":now,
    "what is a human being?":"A human being is a member of the species Homo sapiens, which is the only extant species of the genus Homo",
    
}

while True:
    qs=input()

    if (qs == "quit"):
        break

    else:
        print(qna[qs])
