import random
correct_num = random.randint(1,100)
guess_count = 1
player_guess = int(input("小朋友，猜猜看，我心裡想的數字是多少?: "))
while player_guess != correct_num:
  if player_guess < correct_num:  
    print("猜錯啦! 猜高一點!")
  elif player_guess > correct_num:
    print("不對! 猜低一點")
  guess_count += 1 
  player_guess = int(input("小朋友，猜猜看，我心裡想的數字是多少?: "))
else:
  print("恭喜你，猜對了！")
  print(f"你總共猜了{guess_count}次!")
