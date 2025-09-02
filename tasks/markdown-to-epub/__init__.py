#region generated meta
import typing
class Inputs(typing.TypedDict):
    markdown_file: str
    output_path: str
    title: str | None
    author: str | None
    theme: typing.Literal["duokan", "minimal", "modern", "classic"] | None
class Outputs(typing.TypedDict):
    epub_file: str
#endregion

from oocana import Context
from pathlib import Path
import pypandoc
from themes import ThemeManager

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
    
    # 获取主题
    theme_name = params.get("theme") or "duokan"
    try:
        theme = ThemeManager.get_theme(theme_name)
        css_content = theme.get_css_content()
        metadata = theme.get_metadata()
        pandoc_options = theme.get_pandoc_options()
    except ValueError as e:
        available_themes = ThemeManager.list_themes()
        raise ValueError(f"{e}. 可用主题: {list(available_themes.keys())}")
    
    # 配置 EPUB 转换选项
    epub_options = pandoc_options.copy()
    epub_options.extend([
        '--metadata', f'title={title}',
        '--metadata', f'author={author}',
        '--metadata', f'lang={metadata.get("lang", "zh")}',
        '--resource-path', str(markdown_path.parent),
    ])
    
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