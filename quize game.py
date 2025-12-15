questions1=[
    {
        "question":"what is the capital city of ethiopia?",
        "options":[
            "A.paris","B.london","C.Addis ababa","D.Madrid"
        ],"answer":"c"
    },
    {
        "question":"which language is used for web development?",
        "options":[
            "A.css","B.html","C.python","D.A&B"
        ]
        ,"answer":"D"
    },
    {
        "question":"which one is mark up language?","options":[
            "A.html","B.css","C.javascript","D.django"
        ]
        ,"answer":"A"
    }
]
score=0
for mule in questions1:
    print(mule["question"])
    for option in mule["options"]:
        print(option)
    user_answer=input("enter your answer (A/B/C/D):").upper()
    if user_answer==mule["answer"]:
        print("correct!\n")
        score=+1
    else:
        print("wrong! The correct answer is {mule['answer']}\n")
print(f"you scored {score} out of {len(questions1)}")            