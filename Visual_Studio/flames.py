# function for removing common characters  
def eliminateCommonChars(listOne, listTwo) :  
    for i in range(len(listOne)) :  
        for j in range(len(listTwo)) :  
            if listOne[i] == listTwo[j] :  
                c = listOne[i]  
                listOne.remove(c)  
                listTwo.remove(c)  
                listThree = listOne + ["*"] + listTwo  
                return [listThree, True]  
  
    listThree = listOne + ["*"] + listTwo  
    return [listThree, False]  
  
# Driver code  
if __name__ == "__main__" :  
    playerOne = input("Enter Your Name : ")  
    playerOne = playerOne.lower()  
    playerOne.replace(" ", "")  
    playerOneList = list(playerOne)  
  
    playerTwo = input("Enter Your Crush Name : ")  
    playerTwo = playerTwo.lower()  
    playerTwo.replace(" ", "")  
    playerTwoList = list(playerTwo)  
  
    proceed = True  
      
    while proceed :  
        retList = eliminateCommonChars(playerOneList, playerTwoList)  
        conList = retList[0]  
        proceed = retList[1]  
        starIndex = conList.index("*")  
  
        playerOneList = conList[ : starIndex]  
        playerTwoList = conList[starIndex + 1 : ]  
  
    theCount = len(playerOneList) + len(playerTwoList)  
  
    # list of FLAMES acronym  
    res = ["Friends", "Sister", "Marriage", "Enemies", "Lovers", "Affectionate"]  
  
    while len(res) > 1 :  
        splitIndex = (theCount % len(res) - 1)  
        if splitIndex >= 0 :  
            right = res[splitIndex + 1 : ]  
            left = res[ : splitIndex]  
            res = right + left  
        else :  
            res = res[ : len(res) - 1]  
  
    # print final result  
    print("Relationship Status :", res[0])