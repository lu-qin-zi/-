import random
with open("D:\\python\\单词本-物联网30词.txt","r+",encoding="utf-8") as f:
    #把读取到的内容搞到words哪里
    #需要把那一大串字符串分开才对
    #还需要把单词与汉语分开，赋值
    wrong_words_list=[]
    for i in f:
        i=i.strip()
        if i:
            word,china=i.split(",")
            wrong_words_list.append((word,china))

while True:
    guess_word,chin = random.choice(wrong_words_list)
    print(guess_word)  # 把单词展示给用户看一看，（还需要搞一个循坏）
    user_word=input("请输入单词的意思(按下q就是结束)")
    #用户输入的单词汉语意思
    if user_word=='q':
        print("我们下次再见")
        break

    # 这里的word应该是单词，那么汉语意思就使用china吧

    if user_word == chin:  #比较错误，还需要拆包，即把单词和汉语意思分开
        print("恭喜你答对了")


    else:

        print("很遗憾，你答错了")

        while True:

            print(guess_word)
            user_answer=input("你可以继续猜，输入不要就给你答案")
            if user_answer=="不要":
                print(chin)
                break
            else:
                if user_answer==chin:
                    print("恭喜你答对了")
                    break



        #再补一个判断，让对方选择看答案还是继续写