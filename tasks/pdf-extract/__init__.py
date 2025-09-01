# region generated meta
import typing

class Inputs(typing.TypedDict):
    api_token: str
    pdf_url: str
    enable_ocr: bool
    enable_formula: bool


class Outputs(typing.TypedDict):
    task_id: str
    status_code: int
    response_data: dict
    extract_data: dict

# endregion

import requests
from oocana import Context


def main(params: Inputs, context: Context) -> Outputs:
    """
    使用MinerU API从PDF文件中提取内容
    
    Args:
        params: 包含API token、PDF URL、OCR和公式识别配置
        context: OOMOL上下文对象
        
    Returns:
        包含任务ID、状态码和提取数据的字典
    """
    
    token = params["api_token"]
    url = "https://mineru.net/api/v4/extract/task"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    data = {
        "url": params["pdf_url"],
        "is_ocr": params["enable_ocr"],
        "enable_formula": params["enable_formula"],
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        status_code = response.status_code
        
        if response.status_code == 200:
            response_json = response.json()
            task_id = response_json.get("data", {}).get("task_id", "")
            extract_data = response_json.get("data", {})
            
            context.preview({
                "type": "json",
                "data": {
                    "状态码": status_code,
                    "任务ID": task_id,
                    "响应数据": response_json
                }
            })
            
            return {
                "task_id": task_id,
                "status_code": status_code,
                "response_data": response_json,
                "extract_data": extract_data
            }
        else:
            error_data = {
                "error": f"API请求失败，状态码: {status_code}",
                "response": response.text
            }
            
            context.preview({
                "type": "json",
                "data": error_data
            })
            
            return {
                "task_id": "",
                "status_code": status_code,
                "response_data": error_data,
                "extract_data": {}
            }
            
    except Exception as e:
        error_data = {"error": str(e)}
        
        context.preview({
            "type": "json",
            "data": error_data
        })
        
        return {
            "task_id": "",
            "status_code": 0,
            "response_data": error_data,
            "extract_data": {}
        }