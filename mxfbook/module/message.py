def noExistBook(book_nm):
    return 'book : ' + book_nm + ' does not exist'


def noExistInst(inst_nm):
    return 'instrument : ' + inst_nm + ' does not exist'


def noInstrumentExistInBook(inst_nm, book_nm):
    return inst_nm + ' does not exist in book : ' + book_nm

def instrumentExistInBook(inst_nm, book_nm):
    return inst_nm + ' exist in book : ' + book_nm