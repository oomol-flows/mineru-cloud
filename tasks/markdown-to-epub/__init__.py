#region generated meta
import typing
class Inputs(typing.TypedDict):
    markdown_file: str
    output_path: str
    title: str | None
    author: str | None
class Outputs(typing.TypedDict):
    epub_file: str
#endregion

from oocana import Context
from pathlib import Path
import pypandoc

def main(params: Inputs, context: Context) -> Outputs:
    """
    使用 pypandoc 将 Markdown 文件转换为 EPUB 电子书格式
    
    Args:
        params: 输入参数，包含 markdown_file, output_path, title, author
        context: OOMOL 上下文对象
        
    Returns:
        输出结果，包含生成的 EPUB 文件路径
    """
    
    # 读取并验证 Markdown 文件
    markdown_path = Path(params["markdown_file"])
    if not markdown_path.exists():
        raise FileNotFoundError(f"Markdown 文件不存在: {params['markdown_file']}")
    
    # 设置输出路径
    output_path = Path(params["output_path"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 获取标题和作者
    title = params.get("title") or markdown_path.stem
    author = params.get("author") or "Unknown Author"
    
    # 配置 EPUB 转换选项
    epub_options = [
        '--standalone',
        '--metadata', f'title={title}',
        '--metadata', f'author={author}',
        '--metadata', 'lang=zh',
        '--resource-path', str(markdown_path.parent),
        '--toc',  # 生成目录
        '--toc-depth=3',  # 目录深度
        '--epub-chapter-level=2',  # 章节级别
    ]
    
    # 添加 CSS 样式（可选）
    css_content = """
    body { 
        font-family: serif; 
        margin: 2em; 
        line-height: 1.6; 
    }
    h1, h2, h3, h4, h5, h6 { 
        color: #333; 
        margin-top: 1.5em; 
        margin-bottom: 0.5em; 
    }
    code { 
        background-color: #f5f5f5; 
        padding: 0.2em 0.4em; 
        border-radius: 3px; 
        font-family: monospace; 
    }
    pre { 
        background-color: #f5f5f5; 
        padding: 1em; 
        border-radius: 5px; 
        overflow-x: auto; 
    }
    blockquote { 
        border-left: 4px solid #ddd; 
        padding-left: 1em; 
        margin-left: 0; 
        font-style: italic; 
    }
    table { 
        border-collapse: collapse; 
        width: 100%; 
    }
    th, td { 
        border: 1px solid #ddd; 
        padding: 0.5em; 
        text-align: left; 
    }
    th { 
        background-color: #f5f5f5; 
        font-weight: bold; 
    }
    """
    
    # 创建临时 CSS 文件
    css_path = output_path.parent / "temp_style.css"
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    epub_options.extend(['--css', str(css_path)])
    
    try:
        # 使用 pypandoc 进行转换
        pypandoc.convert_file(
            str(markdown_path),
            'epub',
            outputfile=str(output_path),
            extra_args=epub_options
        )
        
        # 验证文件是否生成成功
        if not output_path.exists():
            raise RuntimeError("EPUB 文件生成失败")
            
        # 清理临时 CSS 文件
        if css_path.exists():
            css_path.unlink()
            
        return {"epub_file": str(output_path)}
        
    except Exception as e:
        # 清理临时文件
        if css_path.exists():
            css_path.unlink()
        raise RuntimeError(f"EPUB 转换失败: {str(e)}")