n = int(input())
scores_dataset = []
for students in range(n):
    name = input()
    city = input()
    SeqNo = int(input())
    Mm = int(input())
    Pm = int(input())
    Cm = int(input())

    details = {"Name": name, "City": city, "SeqNo": SeqNo, "Mathematics": Mm, "Physics": Pm, "Chemistry": Cm}
    scores_dataset.append(details)