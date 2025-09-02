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
    
    # 优化的 CSS 样式 - 参考多看阅读风格
    css_content = """
    /* 基础样式 */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, "Songti SC", "STSong", serif;
        font-size: 16px;
        line-height: 1.8;
        margin: 1em 1.5em;
        text-align: justify;
        color: #333;
    }
    
    /* 标题样式 */
    h1 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "SF Pro Display", "Helvetica Neue", sans-serif;
        font-size: 28px;
        text-align: center;
        color: #91531d;
        font-weight: 600;
        margin-top: 2.5em;
        margin-bottom: 2.5em;
        border-bottom: 2px solid #e8c696;
        padding-bottom: 0.5em;
    }
    
    h2 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "SF Pro Display", "Helvetica Neue", sans-serif;
        font-size: 24px;
        color: #91531d;
        font-weight: 600;
        margin-top: 2em;
        margin-bottom: 1.5em;
        text-indent: 0;
    }
    
    h3 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "SF Pro Display", "Helvetica Neue", sans-serif;
        font-size: 20px;
        color: #91531d;
        font-weight: 600;
        margin-top: 1.8em;
        margin-bottom: 1.2em;
        text-indent: 0;
    }
    
    h4, h5, h6 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "SF Pro Display", "Helvetica Neue", sans-serif;
        font-size: 18px;
        color: #91531d;
        font-weight: 600;
        margin-top: 1.5em;
        margin-bottom: 1em;
        text-indent: 0;
    }
    
    /* 段落样式 */
    p {
        text-indent: 2em;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }
    
    /* 列表样式 */
    ul, ol {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
        margin: 1em 0;
        padding-left: 2em;
    }
    
    li {
        margin: 0.3em 0;
        line-height: 1.6;
    }
    
    /* 代码样式 */
    code {
        font-family: "SF Mono", "Monaco", "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
        font-size: 14px;
        background-color: #f8f8f8;
        color: #91531d;
        padding: 0.2em 0.4em;
        border-radius: 3px;
        border: 1px solid #e0e0e0;
    }
    
    pre {
        font-family: "SF Mono", "Monaco", "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
        font-size: 14px;
        background-color: #f8f8f8;
        color: #333;
        padding: 1em;
        border-radius: 5px;
        border: 1px solid #e0e0e0;
        overflow-x: auto;
        line-height: 1.4;
        margin: 1em 0;
    }
    
    pre code {
        background: none;
        border: none;
        padding: 0;
        color: inherit;
    }
    
    /* 引用样式 */
    blockquote {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Arial, serif;
        font-style: italic;
        border-left: 4px solid #91531d;
        margin: 1em 0;
        padding: 0.5em 1em;
        background-color: #f9f9f9;
        color: #666;
    }
    
    blockquote p {
        text-indent: 0;
        margin: 0.5em 0;
    }
    
    /* 表格样式 */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em auto;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "SF Pro Display", "Helvetica Neue", sans-serif;
        font-size: 14px;
    }
    
    th, td {
        border: 1px solid #ccc;
        padding: 0.5em 0.8em;
        text-align: left;
        line-height: 1.4;
    }
    
    th {
        background-color: #f5f5f5;
        font-weight: bold;
        color: #333;
    }
    
    /* 图片样式 */
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1em auto;
        border-radius: 4px;
    }
    
    /* 链接样式 */
    a {
        color: #91531d;
        text-decoration: underline;
    }
    
    a:hover {
        color: #b8651f;
    }
    
    /* 强调样式 */
    strong, b {
        font-weight: bold;
        color: #333;
    }
    
    em, i {
        font-style: italic;
    }
    
    /* 分隔线 */
    hr {
        border: none;
        border-top: 2px solid #e8c696;
        margin: 2em 0;
    }
    
    /* 脚注样式 */
    .footnote {
        font-size: 14px;
        color: #666;
        border-top: 1px solid #ccc;
        margin-top: 2em;
        padding-top: 1em;
    }
    
    /* 页面布局优化 */
    @page {
        margin: 1cm 0.8cm;
    }
    
    /* 章节分页 */
    h1 {
        page-break-before: always;
    }
    
    /* 避免孤行寡行 */
    p {
        orphans: 2;
        widows: 2;
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