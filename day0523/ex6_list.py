#list 자료형
list1=["hello"]
print(list1)
list1.append("orange")
list1.append("apple")
print(list1)

#선언만
list2=[]
list2.append("red")
list2.append("yello")
list2.append("pink")
list2.append("blue")
list2.append("black")

print(list2)

#일부만 출력
print("list1의 첫 데이터",list1[0])
print("list2의 1~3 데이타",list2[1:4])

#리스트안에 또 리스트를 담을 수 있따
list3 = ["모닝","그랜저",["벤츠","미니"]]
print(list3)
print(list3[1])
print(list3[2][0])