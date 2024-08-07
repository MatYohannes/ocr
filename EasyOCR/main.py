import easyocr

def is_text_present(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    return len(result) > 0


def text_and_prob(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    # bbox is the coordinates
    # text is text
    # prob is the confidence score
    for (bbox, text, prob) in result:
        return text, prob

'''
Ouput:
[([[184, 133], [765, 133], [765, 318], [184, 318]], '619121', 0.6949927338421048)]
1. List containing four pairs of coordinates
    top-left, top-right, bottom-right, bottom-left
2. Detected Text
3. Confidence Score of 69.5%
'''

text1, prob1 = text_and_prob('../Images/619121.jpg')
print(text1, prob1)

