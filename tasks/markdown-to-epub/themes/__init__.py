from .base import EpubTheme
from .duokan import DuokanTheme
from .minimal import MinimalTheme
from typing import Dict, Type

class ThemeManager:
    """主题管理器"""
    
    _themes: Dict[str, Type[EpubTheme]] = {
        "duokan": DuokanTheme,
        "minimal": MinimalTheme,
    }
    
    _default_theme = "minimal"
    
    @classmethod
    def get_theme(cls, theme_name: str = None) -> EpubTheme:
        """根据主题名称获取主题实例"""
        if theme_name is None:
            theme_name = cls._default_theme
            
        if theme_name not in cls._themes:
            raise ValueError(f"未知的主题: {theme_name}. 可用主题: {list(cls._themes.keys())}")
        
        theme_class = cls._themes[theme_name]
        return theme_class()
    
    @classmethod
    def list_themes(cls) -> Dict[str, str]:
        """列出所有可用主题"""
        themes_info = {}
        for theme_name, theme_class in cls._themes.items():
            instance = theme_class()
            themes_info[theme_name] = instance.get_theme_info()["description"]
        return themes_info
    
    @classmethod
    def register_theme(cls, theme_name: str, theme_class: Type[EpubTheme]):
        """注册新主题"""
        cls._themes[theme_name] = theme_class

# 导出主要接口
__all__ = ["EpubTheme", "ThemeManager", "DuokanTheme", "MinimalTheme"]