import pyperclip as clip


# markdown 标准表格格式
# |  表头   | 表头  |
# |  ----  | ----  |
# | 单元格  | 单元格 |
# | 单元格  | 单元格 |

def gen_md_table(cp: str, sp="\r\n", sp_="\t", header=None):
    """
    生成markdown表格
    :param cp: str 从sql复制的表格数据，特征是以\r\n分行，\t分隔同行数据
    :param sp: str 行末分隔符，默认"\r\n"
    :param sp_: str 同一行数据分隔符，默认"\t"
    :param header: list 表头列表，默认["字段名", "字段说明", "字段类型"]
    :return:
    """
    if header is None:
        header = ["字段名", "字段说明", "字段类型"]
    str_return = "|" + "|".join(header) + "|" + "\n"
    str_return += "|  ----  " * header.__len__() + "|\n"
    sts = cp.split("\r\n")
    for s in sts:
        if not s:
            continue
        str_return += '|' + '|'.join([_ for _ in s.split("\t")]) + '|\n'
    return str_return


def clip_it():
    """
    剪切板自动化读取写入
    :return:
    """
    value = clip.paste()
    clip.copy(gen_md_table(value))


clip_it()
