def delete_duplicates(list):
    unique = []  # answer list
    for element in list:
        if not (element in unique):  # if element not in unique add it to unique
            unique.append(element)
    return unique


# returns list with all duplicate elements removed

def score_probablity(statement):
    key_words = ['age', 'year', 'born', 'date of birth']
    words_total = 0
    occurrences = 0
    for word in statement:
        words_total += 1  # counts total number of words in statement
        if (word in key_words):  # if word is in keywords increment occurrences
            occurrences += 1
    return (
                       occurrences / words_total) > 0.7  # if keywords are more than 70% of the total sentence return true else false


def is_orderedone(list):
    return list == sorted(list)


def is_orderedtwo(list):
    copylist = list.copy()
    for x in range(len(copylist) - 1):
        if copylist.pop(0) > min(copylist):
            return False
    return True


def is_orderedthree(list):
    for x in range(len(list) - 1):
        y = x + 1
        if list[x] > list[y]:
            return False
    return True


# assume there is a new line table in between every answer and question
def parseFile(name):
    question, answer, question_number, answer_number = [], [], [], []
    current = True
    numList, anslist = [], []
    with open(name) as file:
        for line in file:
            if line == '\n':

                if not current:
                    answer_number.append(numList)
                    answer.append(anslist)
                    numList, anslist = [], []

                current = not current
            elif current:
                current_question = line.split(".")
                question_number.append(current_question[0])
                question.append(current_question[1][1:-1])
            else:
                current_answer = line.split(".")
                numList.append(current_answer[0])
                anslist.append(current_answer[1][1:-1])

    print(question)
    print(answer_number)
    print(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(is_orderedone([1, 1, 1, 1, 1]))
    print(is_orderedone([1, 2, 3]))
    print(is_orderedone([7, -4, 8, 12, 0]))
    print(is_orderedtwo([1, 1, 1, 1, 1]))
    print(is_orderedtwo([1, 2, 3]))
    print(is_orderedtwo([7, -4, 8, 12, 0]))
    print(is_orderedthree([1, 1, 1, 1, 1]))
    print(is_orderedthree([1, 2, 3]))
    print(is_orderedthree([7, -4, 8, 12, 0]))
    parseFile("test.txt")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
