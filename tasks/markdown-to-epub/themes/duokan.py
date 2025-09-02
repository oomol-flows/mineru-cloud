from .base import EpubTheme
from typing import Dict, Any

class DuokanTheme(EpubTheme):
    """多看阅读风格主题 - 温暖的棕色调，适合长时间阅读"""
    
    def __init__(self):
        super().__init__("duokan")
    
    def get_css_content(self) -> str:
        """返回多看风格的 CSS 样式"""
        return """
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
    
    def get_metadata(self) -> Dict[str, Any]:
        """返回多看主题的元数据配置"""
        return {
            "lang": "zh",
            "theme_color": "#91531d",
            "background_color": "#ffffff"
        }