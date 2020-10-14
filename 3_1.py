def one_list(text_list):
    text_result = []
    for text_number in text_list:
        if ' ' in text_number:
            for i in text_number.split():
                text_result.append(i)
        else:
            text_result.append(text_number)
    print(text_result)

one_list(['jjg','ytyut gffg','ytuyt fgf fgf','hjgjhg'])
