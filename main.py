import fitz


def parse_doc(doc_path):
    return fitz.Document(doc_path)


def count_page(doc):
    return doc.pageCount


def convert_pdf_to_image(doc_path):
    doc = parse_doc(doc_path=doc_path)
    page = count_page(doc)

    for pg in range(page):
        page = doc[pg]
        rotate = int(0)
        zoom_x = 1.0
        zoom_y = 1.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        return pg, pm


def output_image(doc_path, output_path):
    if doc_path:
        pg, im = convert_pdf_to_image(doc_path=doc_path)
        pic_path = output_path
        pic_name = '{}.png'.format(pg)
        pic = '{}{}'.format(pic_path,pic_name)
        im.writePng(pic)


if __name__ == '__main__':
    output_image('/users/apple/desktop/Cplus2.pdf', '/users/apple/desktop/convert')
