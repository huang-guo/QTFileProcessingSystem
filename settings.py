import json

with open('config.json', encoding='utf-8')as f:
    contents = f.read()
if contents.startswith(u'\ufeff'):
    contents = contents.encode('utf8')[3:].decode('utf8')
config = json.loads(contents)
TITLE = config['title']
FORM_SIZE = config['form_size']
COMMODITY_CODE_JS = config['commodity_code_js']
LINK_JS = config["link_js"]

SAMPLE_INVOICE = config['sample_invoice']

FIELD_LINK = config['field_link']
FIELD_COMMODITY = config["field_commodity"]
FIELD_PRICE = config["field_price"]
FIELD_UNIT = config["field_unit"]
FIELD_NUM = config["field_num"]
FIELD_MONEY = config["field_money"]
FIELD_NUMBER = config["field_number"]

EXCEL_SUFFIX = config["excel_suffix"]