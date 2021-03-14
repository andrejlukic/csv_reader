import sys # For printing exception stack trace

ROW_LIMIT = 100000000
DEFAULT_DELIMITER = ','
DEFAULT_QUOTATION = '"'
DEFAULT_ESCAPE = '\\'
DEFAULT_COMMENT = '#'

def read_csv(fname, header = True):
    """ Read a comma-separated CSV document

    :param fname: path to a CSV file
    :param header: interpret first line as header
    :return: CSV represented as list of dictionaries
    """

    count_total = 0
    count_parsed = 0
    count_failed = 0
    document = list()
    documentHeader = None
    with open(fname, 'r+', encoding='utf-8-sig') as csvfile:
        for line in csvfile:
            stripped_line = line.strip()

            if not stripped_line:
                continue

            count_total += 1
            if (count_total > ROW_LIMIT):
                print("The file limit has been reached. Exiting ... ")
                break;

            try:
                record = parseline(stripped_line)
                if header and count_total==1:
                    documentHeader = list(record.values())
                else:
                    document.append(record)
                count_parsed += 1
            except:
                # log error
                print("Ignoring line {0}. Error parsing: {1} Error: {2}".format(count_total, line, sys.exc_info()[0]))
                count_failed += 1
        else:
            #no more lines to read
            pass

    print("CSV reader summary: {0} lines read. {1} parsed. {2} failed".format(count_total, count_parsed, count_failed))
    return merge_header(document, documentHeader)

def parseline(line):
    state = LineState(line)
    #startindex = 0
    #if header:
    #    startindex = 1

    for char in line:
        while True:
            process_next = state.next_step(char)
            if process_next:
                break
    state.collect_field()
    return state.get_record()

def merge_header(records, header):

    if not header:
        if records:
            columns = len(records[0])
            return [d for d in records if len(d) == columns]
        else:
            return []
    elif not records:
        return {h:None for h in header}
    else:
        columns = len(header)
        cleaned_records = [d for d in records if len(d) == columns]
        document = [{a:b for a,b in zip(header, rec.values())} for rec in cleaned_records]
        return document

class LineState:
    def __init__(self, line, header = None):
        self.line = line
        self.header = header
        self.state = StartLineState()
        self.current_char = line[0]
        self.current_field = ''
        self.record = list()

    def collect_field(self):
        if self.current_field:
            self.record.append(self.current_field)
        self.current_field = ''

    def get_record(self):
        if self.header and len(self.record) != len(self.header):
            raise Exception('Header length does not match column length')
        elif self.header:
            return {a:b for a,b in zip(self.header, self.record)}
        else:
            return {a: b for a, b in zip(range(len(self.record)), self.record)}

    def is_end_of_line(self):
        return self.current_char == len(self.line)-1

    def is_comment(self):
        return self.current_char == DEFAULT_COMMENT

    def is_quote(self):
        return self.current_char == DEFAULT_QUOTATION

    def is_delimiter(self):
        return self.current_char == DEFAULT_DELIMITER

    def next_step(self, char):
        self.current_char = char
        return self.state.next_step(self)

class CommentState:
    def next_step(self, linestate):
        if linestate.is_end_of_line():
            linestate.state = EndLineState()
            return False
        return True

class StartFieldState:
    def next_step(self, linestate):
        if linestate.is_end_of_line():
            linestate.state = EndLineState()
            return False
        elif linestate.is_quote():
            linestate.state = QuotedFieldState()
            return True
        else:
            linestate.state = RegularFieldState()
            return False

class StartLineState:
    def next_step(self, linestate):
        if linestate.is_end_of_line():
            linestate.state = EndLineState()
            return False
        elif linestate.is_comment():
            linestate.state = CommentState()
            return False
        else:
            linestate.state = StartFieldState()
            return False



class QuotedFieldState:
    def next_step(self, linestate):
        if linestate.is_end_of_line():
            linestate.state = EndLineState()
            return False
        elif linestate.is_quote():
            linestate.state = DoubleQuoteState()
            return True
        else:
            linestate.current_field += linestate.current_char
            return True

class RegularFieldState:
    def next_step(self, linestate):
        if linestate.is_end_of_line():
            linestate.state = EndLineState()
            return False
        elif linestate.is_delimiter():
            linestate.state = StartFieldState()
            linestate.collect_field()
            return True
        else:
            linestate.current_field += linestate.current_char
            return True

class DoubleQuoteState:
    def next_step(self, linestate):
        if linestate.is_end_of_line():
            linestate.state = EndLineState()
            return False
        elif linestate.is_delimiter():
            linestate.state = StartFieldState()
            linestate.collect_field()
            return True
        elif linestate.is_quote():
            linestate.current_field += linestate.current_char
            linestate.state = QuotedFieldState()
            return True
        else:
            raise Exception('Unexpected character following the second quote')

class EndLineState:
    def next_step(self, linestate):
        linestate.collect_field()
        return True






