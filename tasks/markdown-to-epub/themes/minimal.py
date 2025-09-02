from .base import EpubTheme
from typing import Dict, Any

class MinimalTheme(EpubTheme):
    """简约风格主题 - 简洁清爽的黑白风格"""
    
    def __init__(self):
        super().__init__("minimal")
    
    def get_css_content(self) -> str:
        """返回简约风格的 CSS 样式"""
        return """
/* 基础样式 */
body {
    font-family: "Georgia", "Times New Roman", "STSong", "SimSun", serif;
    font-size: 16px;
    line-height: 1.6;
    margin: 1em;
    color: #333;
    text-align: left;
}

/* 标题样式 */
h1 {
    font-family: "Helvetica Neue", "Arial", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 32px;
    font-weight: 300;
    color: #222;
    margin-top: 2em;
    margin-bottom: 1.5em;
    text-align: center;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.3em;
}

h2 {
    font-family: "Helvetica Neue", "Arial", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 24px;
    font-weight: 400;
    color: #222;
    margin-top: 2em;
    margin-bottom: 1em;
}

h3 {
    font-family: "Helvetica Neue", "Arial", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 20px;
    font-weight: 400;
    color: #333;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
}

h4, h5, h6 {
    font-family: "Helvetica Neue", "Arial", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 18px;
    font-weight: 500;
    color: #444;
    margin-top: 1.2em;
    margin-bottom: 0.6em;
}

/* 段落样式 */
p {
    margin-top: 0.8em;
    margin-bottom: 0.8em;
    text-indent: 0;
}

/* 列表样式 */
ul, ol {
    margin: 1em 0;
    padding-left: 1.5em;
}

li {
    margin: 0.2em 0;
    line-height: 1.5;
}

/* 代码样式 */
code {
    font-family: "Consolas", "Monaco", "Courier New", monospace;
    font-size: 14px;
    background-color: #f5f5f5;
    color: #666;
    padding: 0.1em 0.3em;
    border-radius: 2px;
}

pre {
    font-family: "Consolas", "Monaco", "Courier New", monospace;
    font-size: 14px;
    background-color: #f8f8f8;
    color: #555;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 3px;
    overflow-x: auto;
    line-height: 1.3;
    margin: 1em 0;
}

pre code {
    background: none;
    border: none;
    padding: 0;
}

/* 引用样式 */
blockquote {
    border-left: 3px solid #ddd;
    margin: 1em 0;
    padding: 0.5em 1em;
    background-color: #fafafa;
    color: #555;
    font-style: normal;
}

blockquote p {
    margin: 0.5em 0;
}

/* 表格样式 */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 14px;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.4em 0.6em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
    font-weight: bold;
}

/* 图片样式 */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
}

/* 链接样式 */
a {
    color: #0066cc;
    text-decoration: underline;
}

a:hover {
    color: #004499;
}

/* 强调样式 */
strong, b {
    font-weight: bold;
    color: #222;
}

em, i {
    font-style: italic;
}

/* 分隔线 */
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 2em 0;
}

/* 脚注样式 */
.footnote {
    font-size: 12px;
    color: #777;
    border-top: 1px solid #ddd;
    margin-top: 2em;
    padding-top: 1em;
}

/* 页面布局 */
@page {
    margin: 1.2cm;
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
    
    def get_metadata(self) -> Dict[str, Any]:
        """返回简约主题的元数据配置"""
        return {
            "lang": "zh",
            "theme_color": "#333333",
            "background_color": "#ffffff"
        }