import os
import pytesseract
import re
import cv2
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import MWETokenizer
import spacy

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
path = "C:\\Users\\HweeNamYeonRok\\Documents\\카카오톡 받은 파일"

file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".jpg")]


for name in file_list_py:
    abpath = path + "\\"
    image = cv2.imread(name)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    image_gray = cv2.medianBlur(image_gray, 9)
    
    txt = pytesseract.image_to_string(image, lang='eng')
    #temp = re.sub('[=+#/\?:^$.@*\"※~&%!\\\'\"/\[\]_{}<>£§»®|\n-]','',txt)
    temp = txt.lower()
    print(name)
    tokenizer = MWETokenizer()
    tokenizer.add_mwe(('nestle',',','koko'))
    print(tokenizer.tokenize(temp.split()))
    
    print('========================================nltk========================================\n')
    print(word_tokenize(temp))
    print('\n========================================Spacy========================================')
    nlp = spacy.load('en_core_web_sm')
    print(list(nlp(temp)))
    print('====================================================================================')

    #rep = name.replace(".jpg", ".txt")
    #print(rep + "=========================================")
    #print(pos_tag(word_tokenize(temp)))
    #print(re.split(',|\(|\)|\n', temp))
    #print("=========================================")
    '''file = open(abpath + rep, 'w',-1, "utf-8")
    file.write(txt)
    file.close()'''

#a = pos_tag(["hot","pepper","dried", "fruits","green","tea"])

#for i in range(len(a)) :
    #if ('JJ' in a[i][1] or 'VBD' in a[i][1]) and 'NN' in a[i + 1][1] : print(a[i][0] + ' ' + a[i+1][0])


