from abc import ABC, abstractmethod
from typing import Dict, Any

class EpubTheme(ABC):
    """EPUB 主题基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_css_content(self) -> str:
        """获取主题的 CSS 样式内容"""
        pass
    
    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        """获取主题的元数据配置"""
        pass
    
    def get_pandoc_options(self) -> list:
        """获取 pandoc 转换选项，子类可重写以自定义"""
        return [
            '--standalone',
            '--toc',
            '--toc-depth=3',
            '--epub-chapter-level=2',
        ]
    
    def get_theme_info(self) -> Dict[str, str]:
        """获取主题信息"""
        return {
            "name": self.name,
            "description": self.__doc__ or "暂无描述"
        }