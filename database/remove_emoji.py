import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def demoji(text): ## 한글, 숫자, 특수문자 전체 제거
    pattern = re.compile("["
            u"\U00000000-\U0000001F"
            u"\U00000028-\U0000002D"
            u"\U0000003A-\U0000ABFF"
            u"\U0000D7B0-\U0010FFFF"
#            u"\U000025A0-\U000027FF"
#            u"\U00002B00-\U00002BFF"
#            u"\U0001F600-\U0001F64F"  # emoticons
#            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#            u"\U0001F680-\U0001F6FF"  # transport & map symbols
#            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#            u"\U0001F900-\U0001F9FF"
#            u"\U0001FA70-\U0001FAFF"
                            "]+", flags=re.UNICODE)
    repl = ''
    return re.sub(pattern = pattern, repl = repl, string = text)
