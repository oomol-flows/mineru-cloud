from oocana import Context
import os

#region generated meta
import typing
class Inputs(typing.TypedDict):
    file_paths: list[str]
class Outputs(typing.TypedDict):
    markdown_file: str
#endregion

def main(params: Inputs, context: Context) -> Outputs:
    file_paths = params.get('file_paths', [])
    
    # 筛选markdown文件
    markdown_files = []
    for file_path in file_paths:
        # 检查文件扩展名是否为markdown格式
        if file_path.lower().endswith(('.md', '.markdown', '.mdown', '.mkd', '.mkdn')):
            # 检查文件是否存在
            if os.path.isfile(file_path):
                markdown_files.append(file_path)
    
    return {
        "markdown_file": markdown_files[0],
    }