from .base import EpubTheme
from typing import Dict, Any

class ClassicTheme(EpubTheme):
    """经典风格主题 - 传统书籍排版，衬线字体，适合正式文档"""
    
    def __init__(self):
        super().__init__("classic")
    
    def get_css_content(self) -> str:
        """返回经典风格的 CSS 样式"""
        return """
/* 基础样式 - 经典书籍风格 */
body {
    font-family: "Times New Roman", "Songti SC", "SimSun", "STSong", serif;
    font-size: 15px;
    line-height: 1.6;
    margin: 1em 1.5em;
    text-align: justify;
    color: #2c2c2c;
    background-color: #faf8f5;
}

/* 标题样式 */
h1 {
    font-family: "Times New Roman", "STZhongsong", "SimSun", serif;
    font-size: 26px;
    font-weight: bold;
    color: #8b4513;
    text-align: center;
    margin-top: 3em;
    margin-bottom: 2em;
    text-transform: uppercase;
    letter-spacing: 1px;
}

h2 {
    font-family: "Times New Roman", "STZhongsong", "SimSun", serif;
    font-size: 22px;
    font-weight: bold;
    color: #8b4513;
    margin-top: 2.5em;
    margin-bottom: 1.5em;
    text-indent: 0;
    border-bottom: 1px solid #d4a76a;
    padding-bottom: 0.3em;
}

h3 {
    font-family: "Times New Roman", "STZhongsong", "SimSun", serif;
    font-size: 18px;
    font-weight: bold;
    color: #8b4513;
    margin-top: 2em;
    margin-bottom: 1.2em;
    text-indent: 0;
}

h4, h5, h6 {
    font-family: "Times New Roman", "STZhongsong", "SimSun", serif;
    font-size: 16px;
    font-weight: bold;
    color: #8b4513;
    margin-top: 1.8em;
    margin-bottom: 1em;
    text-indent: 0;
}

/* 段落样式 */
p {
    text-indent: 2em;
    margin-top: 0.3em;
    margin-bottom: 0.3em;
    text-align: justify;
    line-height: 1.7;
}

/* 首段不缩进 */
p:first-of-type {
    text-indent: 0;
}

/* 列表样式 */
ul, ol {
    font-family: "Times New Roman", "Songti SC", "SimSun", serif;
    margin: 0.8em 0;
    padding-left: 2.5em;
}

li {
    margin: 0.2em 0;
    line-height: 1.6;
    text-align: justify;
}

/* 代码样式 */
code {
    font-family: "Courier New", "Monaco", "Consolas", monospace;
    font-size: 13px;
    background-color: #f5f5f5;
    color: #333;
    padding: 0.1em 0.3em;
    border: 1px solid #ddd;
}

pre {
    font-family: "Courier New", "Monaco", "Consolas", monospace;
    font-size: 13px;
    background-color: #f8f8f8;
    color: #333;
    padding: 1em;
    border: 1px solid #ddd;
    margin: 1em 0;
    line-height: 1.4;
    overflow-x: auto;
}

pre code {
    background: none;
    border: none;
    padding: 0;
}

/* 引用样式 */
blockquote {
    font-family: "Times New Roman", "Songti SC", "SimSun", serif;
    font-style: italic;
    border-left: 3px solid #8b4513;
    margin: 1em 0;
    padding: 0.5em 1.5em;
    background-color: #f9f7f4;
    color: #5d4e37;
}

blockquote p {
    text-indent: 0;
    margin: 0.5em 0;
    line-height: 1.6;
}

/* 表格样式 */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em auto;
    font-family: "Times New Roman", "Songti SC", "SimSun", serif;
    font-size: 14px;
}

th, td {
    border: 1px solid #d4a76a;
    padding: 0.5em 0.8em;
    text-align: left;
    line-height: 1.4;
}

th {
    background-color: #f5f2ed;
    font-weight: bold;
    color: #8b4513;
}

/* 图片样式 */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
    border: 1px solid #d4a76a;
    padding: 3px;
    background-color: #fff;
}

/* 链接样式 */
a {
    color: #8b4513;
    text-decoration: underline;
}

a:hover {
    color: #a0522d;
}

/* 强调样式 */
strong, b {
    font-weight: bold;
    color: #000;
}

em, i {
    font-style: italic;
    color: #5d4e37;
}

/* 分隔线 */
hr {
    border: none;
    border-top: 1px solid #d4a76a;
    margin: 2em 0;
}

/* 脚注样式 */
.footnote {
    font-size: 12px;
    color: #666;
    border-top: 1px solid #d4a76a;
    margin-top: 2em;
    padding-top: 1em;
    font-style: italic;
}

/* 页面布局 */
@page {
    margin: 2cm 1.5cm;
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

/* 首字母大写 */
p::first-letter {
    font-size: 1.1em;
    font-weight: bold;
}
        """
    
    def get_metadata(self) -> Dict[str, Any]:
        """返回经典主题的元数据配置"""
        return {
            "lang": "zh",
            "theme_color": "#8b4513",
            "background_color": "#faf8f5"
        }