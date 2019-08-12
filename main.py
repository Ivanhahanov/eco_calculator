from PyPDF2 import PdfFileReader

# help(PdfFileReader)

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(info)
    print(number_of_pages)

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # get the first page
        page = pdf.getPage(1)
        print(page)
        # print('Page type: {}'.format(str(type(page))))

        text = page.extractText()
        print(text)


if __name__ == '__main__':
    path = 'Fkko2019.pdf'
    get_info(path)
    text_extractor(path)
