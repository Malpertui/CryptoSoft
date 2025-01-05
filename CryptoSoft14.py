import time
import random
import re
date = time.strftime("%Y-%m-%d %H:%M")
global x
global textFile
global coinName
x=-1
def main():
    global x
    x = -1
    # print(x)
    
    global textFile
    global coinName
    while x<0:
        coinName = input("Введите название монеты: ")
        if len(coinName)<1:
            print("Название должно состоять хотя бы из одной буквы :)")
            continue

        coinName = coinName.upper()
        textFile = input("Введите название файла, куда нужно сохранять данные. Нажмите Enter, чтобы сохранять данные в файл по умолчанию: ")
        if len(textFile)<1:
            textFile = "Crypto.txt"
        if ".txt" not in textFile:
          textFile= textFile + ".txt" 
        
        while x<0:

            priceCoin = input("Цена монеты в USDT: ")
            if "," in priceCoin:
                priceCoin=priceCoin.replace(",", ".")
            try:
                priceCoin = float(priceCoin)
            except:
                print("Неправильные данные. Введите число больше нуля.")
                continue

            if priceCoin > 0:
                # print("Ok")

                
                while x<0:
                    sumMoney = input("На какую сумму вы покупаете монету (в USDT): ")
                    if "," in sumMoney:
                        sumMoney=sumMoney.replace(",", ".")
                    try:
                        sumMoney = float(sumMoney)
                    except:
                        print("Неправильные данные. Введите сумму больше нуля, которая состоит из цифр.")
                        continue
                    if sumMoney > 0:
                        # print("ok")

                        while x<0:
                            priceCoinSell = input("По какой цене думаете продавать монету: ")
                            if "," in priceCoinSell:
                                priceCoinSell=priceCoinSell.replace(",", ".")
                            try:
                                priceCoinSell = float(priceCoinSell)

                            except:
                                print("Неправильные данные. Введите цену продажи, которая состоит из цифр.")
                                continue
                            
                            if priceCoinSell > 0:
                                                 

                                yesOrNo = input("Учитывать комиссию Binance (вводите ДА или НЕТ)? ")
                                yesOrNo = yesOrNo.upper()


                                if yesOrNo == 'ДА':
                                    gain = sumMoney/priceCoin*priceCoinSell - sumMoney - sumMoney/100*0.1 - sumMoney/priceCoin*priceCoinSell/100*0.1
                                    quant_coin = (sumMoney - sumMoney/100*0.1) /priceCoin
                                    gain = round(gain, 3)
                                    quant_coin = round(quant_coin, 3)
                                    sumMoney = round(sumMoney, 3)
                                    priceCoin = round(priceCoin, 3)
                                    print("Вы заработаете ", gain, " USDT (с учетом комиссии). || Количество приобретенных монет: ", quant_coin, "Вложенная сумма: ", sumMoney, "Цена монеты: ", priceCoin)
                                    write_or_no = input("Нажмите Enter, чтобы сохранить данные в текстовый файл. Нажмите 1, если сохранять данные не нужно: ")
                                    if len(write_or_no) < 1:
                                        gain = repr(gain)
                                        coinName = repr(coinName)
                                        
                                        quant_coin = repr(quant_coin)
                                        
                                        sumMoney = repr(sumMoney)
                                        
                                        priceCoin = repr(priceCoin)
                                        with open(textFile, "a", encoding="utf-8") as f:
                                            f.write("Заработок на " + coinName + ": " + gain + " USDT (с учетом комиссии). || Количество приобретенных монет: " + quant_coin + " Вложенная сумма: " + sumMoney + " Цена монеты: " + priceCoin + " Дата записи: " + date + " |||")
                                            f.close()

                                        with open(textFile, 'r', encoding="utf-8") as v:
                                            text_3 = v.read()
                                        if  coinName in text_3:                        # count = 0
                                            # print(text)
                                            totalCoin = 0
                                            totalSumMoney = 0
                                            s = text_3.split('|||')
                                            # print(s)
                                            
                                            for i in range(len(s)):
                                                if coinName in s[i]:
                                                    # print(type(s[i]))
                                                    sumMoneyOne = re.findall(r'сумма: (.*) Цен', s[i])
                                                    floatSumMoneyOne = float(sumMoneyOne[0])
                                                    # print(type(floatSumMoneyOne))
                                                    totalSumMoney = floatSumMoneyOne + totalSumMoney
                                            # print(totalSumMoney)
                                                    coinOne = re.findall(r'монет: (.*) Вло', s[i])    
                                                    floatCoinOne = float(coinOne[0])
                                                    totalCoin = totalCoin + floatCoinOne
                                                    average_entry_point = totalSumMoney/totalCoin
                                        average_entry_point = round(average_entry_point, 3)
                                        average_entry_point = repr(average_entry_point)
                                        with open(textFile, 'a', encoding="utf-8") as v:
                                            v.write(" Cредняя точка входа: " + average_entry_point + "\n")
                                            v.close()            
                                    
                                    
                                    x=x+2
                                    # print(x)

                                else:
                                    gain2 = sumMoney/priceCoin*priceCoinSell - sumMoney
                                    quant_coin2 = sumMoney / priceCoin
                                    sumMoney = round(sumMoney, 3)
                                    priceCoin = round(priceCoin, 3)
                                    quant_coin2 = round(quant_coin2, 3)
                                    gain2 = round(gain2, 3)
                                    print("Вы заработаете ", gain2, " USDT (без учета комиссии). || Количество приобретенных монет: ", quant_coin2, "Вложенная сумма: ", sumMoney, "Цена монеты: ", priceCoin)
                                    write_or_no = input("\nНажмите Enter, чтобы сохранить данные в текстовый файл. Нажмите 1, если сохранять данные не нужно: \n")
                                    if len(write_or_no) < 1:

                                        gain2 = repr(gain2)
                                        coinName = repr(coinName)
                                        quant_coin2 = repr(quant_coin2)
                                        sumMoney = repr(sumMoney)
                                        priceCoin = repr(priceCoin)
                                        with open(textFile, "a", encoding="utf-8") as f:
                                            f.write("Заработок на " + coinName + ": " + gain2 + " USDT (без учета комисси).|| Количество приобретенных монет: " + quant_coin2 + " Вложенная сумма: " + sumMoney + " Цена монеты: " + priceCoin + " Дата записи: " + date + " |||")
                                            f.close()

                                        with open(textFile, 'r', encoding="utf-8") as v:
                                            text_3 = v.read()
                                        if  coinName in text_3:                        # count = 0
                                            # print(text)
                                            totalCoin = 0
                                            totalSumMoney = 0
                                            s = text_3.split('|||')
                                            # print(s)
                                            
                                            for i in range(len(s)):
                                                if coinName in s[i]:
                                                    # print(type(s[i]))
                                                    sumMoneyOne = re.findall(r'сумма: (.*) Цен', s[i])
                                                    floatSumMoneyOne = float(sumMoneyOne[0])
                                                    # print(type(floatSumMoneyOne))
                                                    totalSumMoney = floatSumMoneyOne + totalSumMoney
                                            # print(totalSumMoney)
                                                    coinOne = re.findall(r'монет: (.*) Вло', s[i])    
                                                    floatCoinOne = float(coinOne[0])
                                                    totalCoin = totalCoin + floatCoinOne
                                                    average_entry_point = totalSumMoney/totalCoin
                                        average_entry_point = round(average_entry_point, 3)
                                        average_entry_point = repr(average_entry_point)
                                        with open(textFile, 'a', encoding="utf-8") as v:
                                            v.write(" Cредняя точка входа: " + average_entry_point + "\n")
                                            v.close()            
                                    

                                    x=x+2
                                    # print(f"x = {x}")

                                    
                            else:
                                print("Неправильные данные. Введите цену продажи больше нуля.")
                    else:
                        print("Неправильные данные. Введите сумму покупки больше нуля.")
                        continue
                            
                            
            else:
                print("Неправильные данные. Введите число больше нуля.")
                continue

def afterMain():
    global x
    global textFile
    global coinName
    x = x-2
    # print(x)
    while True:
        waiting = input(f"\nОтлично! Нажмите Enter, чтобы закрыть программу. Нажмите 1 если хотите внести данные еще об одной монете. Нажмите 2 если хотите узнать сумму всех вложений за все время. \nНажмите 3 чтобы посчитать среднюю точку входа в монету {coinName} с учетом последних сохраненных данных. Нажмите 4 чтобы получить порцию криптомотивиции.  \n")
        # print(f"x = {x}")
        if len(waiting) < 1:
            quit()
        elif (waiting == '1'):
            main()
        elif (waiting == '2'):
            
            with open(textFile, 'r', encoding="utf-8") as v:
                text = v.read()
            sumMoneyOne = re.findall(r'сумма: (.*) Цен', text)
            # print(sumMoneyOne)
            totalSumMoney = 0
            for i in range(len(sumMoneyOne)):
                # print(i)
                item_sumMoney=float(sumMoneyOne[i])
                # print(type(coinOne[i]))
                # print(type(item_sumMoney))
                # i = i+1
                # print(sumMoneyOne[i])
                totalSumMoney = totalSumMoney + item_sumMoney
            print(f"Сумма всех вложений (которые занесены в файл {textFile}): {totalSumMoney}")
            continue
        elif (waiting == '3'):
            with open(textFile, 'r', encoding="utf-8") as v:
                text_3 = v.read()
            if  coinName in text_3:                        # count = 0
                # print(text)
                totalCoin = 0
                totalSumMoney = 0
                s = text_3.split('\n')
                # print(s)
                
                for i in range(len(s)):
                    if coinName in s[i]:
                        # print(type(s[i]))
                        sumMoneyOne = re.findall(r'сумма: (.*) Цен', s[i])
                        floatSumMoneyOne = float(sumMoneyOne[0])
                        # print(type(floatSumMoneyOne))
                        totalSumMoney = floatSumMoneyOne + totalSumMoney
                # print(totalSumMoney)
                        coinOne = re.findall(r'монет: (.*) Вло', s[i])    
                        floatCoinOne = float(coinOne[0])
                        totalCoin = totalCoin + floatCoinOne
                        average_entry_point = totalSumMoney/totalCoin
                print(f"Количество всех монет: {totalCoin}. Сумма всех вложений в монету {coinName}: {totalSumMoney}. Средняя точка входа: {average_entry_point}")
                continue
            else:
                print(f"Данных о монете {coinName} нет в файле {textFile}.")
                continue
        else:
            r_number = random.randrange(1, 11)
            if (r_number==1):
                print("\n***Вы молоды, вы красивы, вы успешны. Скоро еще и разбогаете!***\n")
                continue
            elif(r_number==2):
                print("\n***Все идет прекрасно! Еще чуть-чуть, и вы миллионер. Разве что SEC подаст в суд на Binance. Или на Ripple. Или еще одна крупная криптобиржа рухнет из-за незаконных делишек. Или Илон Маск напишет очередную глупость в Твиттере (простите: в Иксе).***\n")    
                continue
            elif(r_number==3):
                print("\n***Криптовалюты – это удел умных. Хорошо, что вы решили в этом всем разобраться.***\n")
                continue
            elif(r_number==4):
                print("\n***Раз вы торгуете криптовалютами, и у вас все еще остались деньги на электричество, которое питает этот компьютер, вы большой молодец!***\n")
                continue
            elif(r_number==5):
                print("\n***Немного терпения и аналитики – и ваш депозит увеличится в несколько раз.***\n")
                continue
            elif(r_number==6):
                print("\n***Чтобы начать торговать «криптой» нужно обладать твердым характером. Когда все вокруг кричали про мошенничество и обман в этой сфере, вы смогли собраться с силами и начать новое очень рискованное, но и не менее прибыльное дело. Так держать!***\n")
                continue
            elif(r_number==7):
                print("\n***Криптомиллионер – это пока не про вас. Но скоро будет про вас. Не спешите, и всё получится!***\n")
                continue
            elif(r_number==8):
                print("\n***Еще немного и можно купить ту мазду, о которой вы мечтали. С подогревом сидений и стереосистемой на 11 динамиков.***\n")
                continue
            elif(r_number==9):
                print("\n***Кто у нас перспективный инвестор? Вы – перспективный инвестор! Не спешите, диверсифицируйте вложения, и инвестиции принесут хорошую прибыль.***\n")
                continue
            elif(r_number==10):
                print("\n***А вы знали, что в 2031 году размер эмиссии при создании блока биткойна составит менее одного биткойна и продолжит стремиться к нулю? Вряд ли. Поэтому вы молодец! Решили не забивать голову глупостями, которые никак не влияют на ваш доход.***\n")
                continue
            continue

        
while True:
    main()
    afterMain()
