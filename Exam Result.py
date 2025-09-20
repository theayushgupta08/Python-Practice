print("Section wise weightage:"
      "\n1- Activities: 30%"
      "\n2- Sports: 20%"
      "\n3- Examination: 50%")
sportsw=20.0
activityw=30.0
examw=50.0
print("Enter the score of the Examinations (Out of 100): ")
e1=float(input("Examination 1: "))
e2=float(input("Examination 2: "))
texamscore=(e1+e2)/200*100
print("Enter the score of the Sports (Out of 100): ")
s1=float(input("Sports: "))
tsportsscore=s1/100*100
print("Enter the score of the Activities (Out of 100): ")
a1=float(input("Activity 1: "))
a2=float(input("Activity 2: "))
a3=float(input("Activity 3: "))
tactscore=(a1+a2+a3)/300*100
result=(texamscore/100*50)+(tsportsscore/100*20)+(tactscore/100*30)
print("******************RESULT******************"
      f"\nExamination: {texamscore} %"
      f"\nSports: {tsportsscore} %"
      f"\nActivities: {tactscore} %"
      f"\n******************************************"
      f"\nOverall Result: {result} %"
      f"\n******************************************")



