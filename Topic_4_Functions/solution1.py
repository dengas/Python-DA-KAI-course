# Реализуйте функцию, которая в качестве аргумента получает строку и возвращает список слов этой строки. В качестве примера можно взять вот такой текст:
# text = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
# Aenean commodo ligula eget dolor. Aenean massa. 
# Cum sociis natoque penatibus et"""


text = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. 
Cum sociis natoque penatibus et"""

def text_to_list(text: str) -> list:
    my_list = text.split(" ")
    print(my_list)
    
text_to_list(text=text)