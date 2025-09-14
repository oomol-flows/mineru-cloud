from oocana import Context
import os

#region generated meta
import typing
class Inputs(typing.TypedDict):
    file_paths: list[str]
    char_limit: float | None
class Outputs(typing.TypedDict):
    markdown_file: str
    first_500_chars: str
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    file_paths = params.get('file_paths', [])
    char_limit = params.get('char_limit', 1000)
    
    # 筛选markdown文件
    markdown_files = []
    for file_path in file_paths:
        # 检查文件扩展名是否为markdown格式
        if file_path.lower().endswith(('.md', '.markdown', '.mdown', '.mkd', '.mkdn')):
            # 检查文件是否存在
            if os.path.isfile(file_path):
                markdown_files.append(file_path)
    
    if not markdown_files:
        raise ValueError("没有找到任何markdown文件")

    # 读取第一个markdown文件的前N个字符
    first_md_file = markdown_files[0]
    first_500_chars = ""

    try:
        with open(first_md_file, 'r', encoding='utf-8') as f:
            content = f.read(char_limit)  # 读取前N个字符
            first_500_chars = content
    except Exception as e:
        first_500_chars = f"读取文件出错: {str(e)}"

    return {
        "markdown_file": first_md_file,
        "first_500_chars": first_500_chars
    }