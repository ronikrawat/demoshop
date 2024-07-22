from xlrd import open_workbook


def set_locator(worksheet):
    def _read_locator(cls):
        book = open_workbook(r"C:\Users\ronik\Desktop\demoshop\pythonProject2\utilites\objects.xls")
        sheet = book.sheet_by_name(worksheet)
        used_rows = sheet.nrows
        for i in range(1, used_rows):
            row = sheet.row_values(i)
            setattr(cls, row[0], (row[1], row[2]))
        return cls

    return _read_locator


def get_header(worksheet, test_function):
    book = open_workbook(r"C:\Users\ronik\Desktop\demoshop\pythonProject2\utilites\testdata.xls")
    sheet = book.sheet_by_name(worksheet)
    used_lines = sheet.nrows
    for i in range(used_lines):
        row = sheet.row_values(i)
        if row[0] == test_function:
            row = [i.strip() for i in sheet.row_values(i - 1)[2:] if i.strip()]
            return ",".join(row)


def get_data(worksheet, testcase):
    book = open_workbook(r"C:\Users\ronik\Desktop\demoshop\pythonProject2\utilites\testdata.xls")
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    data = []
    for i in range(0, used_rows):
        row = sheet.row_values(i)
        if row[0] == testcase and row[1].upper() == "YES":
            row = [line.strip() for line in row if line.strip()]
            data.append(tuple(row[2:]))
    return data
