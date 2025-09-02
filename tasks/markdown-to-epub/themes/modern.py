from .base import EpubTheme
from typing import Dict, Any

class ModernTheme(EpubTheme):
    """现代风格主题 - 简洁现代的深色主题，适合夜间阅读"""
    
    def __init__(self):
        super().__init__("modern")
    
    def get_css_content(self) -> str:
        """返回现代风格的 CSS 样式"""
        return """
/* 基础样式 - 深色主题 */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "SF Pro Display", "Helvetica Neue", "Noto Sans CJK SC", serif;
    font-size: 16px;
    line-height: 1.7;
    margin: 1.2em;
    text-align: justify;
    color: #e0e0e0;
    background-color: #1a1a1a;
}

/* 标题样式 */
h1 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "SF Pro Display", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 30px;
    font-weight: 300;
    color: #64b5f6;
    text-align: center;
    margin-top: 2em;
    margin-bottom: 1.5em;
    border-bottom: 1px solid #333;
    padding-bottom: 0.5em;
}

h2 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "SF Pro Display", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 24px;
    font-weight: 400;
    color: #90caf9;
    margin-top: 2em;
    margin-bottom: 1.2em;
    text-indent: 0;
}

h3 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "SF Pro Display", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 20px;
    font-weight: 400;
    color: #bbdefb;
    margin-top: 1.8em;
    margin-bottom: 1em;
    text-indent: 0;
}

h4, h5, h6 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "SF Pro Display", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 18px;
    font-weight: 500;
    color: #e3f2fd;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    text-indent: 0;
}

/* 段落样式 */
p {
    margin-top: 0.8em;
    margin-bottom: 0.8em;
    text-indent: 0;
}

/* 列表样式 */
ul, ol {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    margin: 1em 0;
    padding-left: 1.5em;
}

li {
    margin: 0.4em 0;
    line-height: 1.5;
}

/* 代码样式 */
code {
    font-family: "SF Mono", "Monaco", "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
    font-size: 14px;
    background-color: #2a2a2a;
    color: #f8f8f2;
    padding: 0.2em 0.4em;
    border-radius: 4px;
    border: 1px solid #444;
}

pre {
    font-family: "SF Mono", "Monaco", "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
    font-size: 14px;
    background-color: #2a2a2a;
    color: #f8f8f2;
    padding: 1em;
    border-radius: 6px;
    border: 1px solid #444;
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
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    border-left: 4px solid #64b5f6;
    margin: 1em 0;
    padding: 0.8em 1.2em;
    background-color: #263238;
    color: #b0bec5;
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
    border: 1px solid #444;
    padding: 0.6em 0.8em;
    text-align: left;
    line-height: 1.4;
}

th {
    background-color: #263238;
    font-weight: 500;
    color: #e3f2fd;
}

td {
    background-color: #1e1e1e;
}

/* 图片样式 */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
    border-radius: 6px;
}

/* 链接样式 */
a {
    color: #64b5f6;
    text-decoration: none;
    border-bottom: 1px solid transparent;
}

a:hover {
    color: #90caf9;
    border-bottom-color: #90caf9;
}

/* 强调样式 */
strong, b {
    font-weight: 600;
    color: #ffffff;
}

em, i {
    font-style: italic;
    color: #bbdefb;
}

/* 分隔线 */
hr {
    border: none;
    border-top: 1px solid #444;
    margin: 2em 0;
}

/* 脚注样式 */
.footnote {
    font-size: 13px;
    color: #9e9e9e;
    border-top: 1px solid #444;
    margin-top: 2em;
    padding-top: 1em;
}

/* 页面布局 */
@page {
    margin: 1cm;
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
        """返回现代主题的元数据配置"""
        return {
            "lang": "zh",
            "theme_color": "#64b5f6",
            "background_color": "#1a1a1a"
        }