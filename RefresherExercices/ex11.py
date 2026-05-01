# Exercise 11: Advanced String Manipulation
# Task: Create a program that:
# 1. Asks the user to input a text paragraph
# 2. Counts the occurrence of each word (case-insensitive)
# 3. Prints the top 5 most frequent words
# 4. Finds all email addresses in the text (using string methods, not regex)
# 5. Replaces all numbers with their spelled-out form (e.g., 1 becomes "one")
# 6. Formats the text so that each sentence starts on a new line


def count_word_occurence(text):
    #count occurence of each word
    word_count ={}
    words = text.lower().split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        #or 
        # word_count[word] = word_count[word] + 1 if word in word_count else 1 

    return word_count


def find_top_words(word_count:dict, n:int=5):
    #get the top 5 
    sorted_dict = sorted(word_count.items(), key=lambda x : x[1], reverse=True)[:n]
    return sorted_dict


#find all the email addresses
def find_emails(text):
    emails = []
    words = text.split()
    #base@something.something
    for word in words:
        if not "@" in word:
            continue

        splited_word = word.split('@')
        if len(splited_word) != 2:
            continue
        localPart, domainPart = splited_word
        #local part cant be empty
        if not localPart :
            continue

        if not "." in domainPart:
            continue 
        #domain part cant start with dot or finish with dot
        if domainPart.startswith('.') or domainPart.endswith('.'):
                continue
        
        splited_domain = domainPart.split('.')
        #can be many dots but make sure the last dot have a word after
        if not splited_domain[-1] :
            continue 

        emails.append(word)
    
    return emails

def replaceNumbersWithWord(text):

    numbers = {
        "0":'zero',
        "1":"one",
        "2":"two",
        "3":'three',
        "4":"four",
        "5":"five",
        "6":'six',
        "7":"seven",
        "8":"eight",
        "9":"nine"
    }

    ''' another approach
    
    for digit,word in numbers.items():
        text.replace(digit, word)
    return text
    '''
    result = ""
    for char in text:
        if char in numbers:
            result += numbers[char]
        else:
            result += char
    
    return result

def sentenceInNewLine(text):
    '''
    #sentence should end with .
    sentences = text.split('. ')
    newText = "\n".join(sentences)
    #this doesnt workd correctly because emails will be splt
    return newText
    '''
    text = text.replace(". ", ".\n")
    text = text.replace("? ", "?\n")
    text = text.replace("! ", "!\n")

    if text.endswith('.') or text.endswith('?') or text.endswith('!'):
        result += '\n'

    return text 
    

if __name__ == "__main__":
    
    #text = input("enter a paragprah")
    text = "Python is a powerful programming language. Python is widely used in web development," \
    "data science, and artificial intelligence. Learning Python can be fun and rewarding. Python's simplicity."\
    "This is an email rahim@asselah.com , ah@. , washid@subdomain.domain.com local@.domain.com. "\
    "This is number 0 , and thi is number 3 , 4, ,5 6, ,7 ,8 9, 123"
    
    word_count = count_word_occurence(text)
    top5 = find_top_words(word_count)
    emails = find_emails(text)
    switched_text = replaceNumbersWithWord(text)
    newLineText = sentenceInNewLine(text)

    print(text)
    print(word_count)
    print(top5)
    print(emails)
    print(switched_text)
    print(newLineText)

    print(text)
