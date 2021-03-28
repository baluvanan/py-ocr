import pdfplumber
import os
import re

mode = 0o666
flags = os.O_RDWR
file_path = 'input.pdf'
elections = [
                {'2011':{'start_page':''}},
                {'2006':{'start_page':''}},
                {'2001':{'start_page':''}},
                {'1996':{'start_page':''}},
                {'1991':{'start_page':''}},
                {'1989':{'start_page':''}},
                {'1984':{'start_page':''}},
                {'1980':{'start_page':''}},
                {'1977':{'start_page':''}},
                {'1971':{'start_page':''}},
                {'1967':{'start_page':''}},

            ]
tables = []
table_settings = {
    "vertical_strategy": "text",
    "horizontal_strategy": "text",
    "intersection_x_tolerance": 15
}
listToStr = ''
# with open(file_path, "r") as file:
def process_2006():
    with open('table_2006_output.txt', 'a+') as output:
        with pdfplumber.open('./input_data/2006.pdf') as pdf:
            pages = pdf.pages
            print(len(pages))
            for i, page in enumerate(pages, start=263):
                if i < len(pages):
                    constitution_crop = pages[i].crop((200, 80, 400, 120))
                    constitution_name = constitution_crop.extract_text()
                    # m = re.search('([^\d .])', constitution_name)
                    # constitution_name = m.group
                    tbl = pages[i].extract_tables(table_settings={
                        "vertical_strategy": "text",
                        "horizontal_strategy": "lines",
                        "min_words_horizontal": 1,
                        "keep_blank_chars": True,
                        "text_x_tolerance": 10
                    })
                    #print(f'{i} --- {tbl}')
                    constituency = {constitution_name:tbl[0], 'year':2006}
                    output.write(str(constituency))
        pdf.close()
    output.close()

def process_2001():
    with open('table_output.txt', 'a+') as output:
            with pdfplumber.open('./input_data/2001.pdf') as pdf:
                pages = pdf.pages
                for i, page in enumerate(pages, start=257):
                    if i < len(pages):
                        constitution_crop = pages[i].crop((200, 80, 400, 120))
                        constitution_name = constitution_crop.extract_text()
                        # m = re.search('([^\d .])', constitution_name)
                        # constitution_name = m.group
                        tbl = pages[i].extract_tables(table_settings={
                            "vertical_strategy": "text",
                            "horizontal_strategy": "lines",
                            "min_words_horizontal": 1,
                            "keep_blank_chars": True,
                            "text_x_tolerance": 10
                        })
                        #print(f'{i} --- {tbl}')
                        constituency = {constitution_name:tbl[0], 'year':2006}
                        output.write(str(constituency))
process_2006()