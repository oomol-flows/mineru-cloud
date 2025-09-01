#region generated meta
import typing
class Inputs(typing.TypedDict):
    pdf_url: str
    api_token: str
    is_ocr: bool | None
    enable_formula: bool | None
    enable_table: bool | None
    model_version: typing.Literal["pipeline", "vlm"] | None
    language: typing.Literal["ch", "en", "fr", "german", "korean", "japan", "arabic", "ta", "te", "ka", "thai", "la", "ru", "vi", "ur", "fa", "uk", "uz", "ug", "hi", "mr", "ne", "sa", "pu", "gu", "ja", "bn", "as", "or"] | None
    data_id: str | None
    callback: str | None
    page_ranges: str | None
    extra_formats: list[typing.Any] | None
    seed: str | None
class Outputs(typing.TypedDict):
    task_id: str
    status_code: float
    response_data: dict
    extract_data: dict
#endregion

import requests
from oocana import Context


def main(params: Inputs, context: Context) -> Outputs:
    """
    使用MinerU API从PDF文件中提取内容
    
    Args:
        params: 包含API token、PDF URL和各种提取选项配置
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
    
    # 构建请求数据，包含所有支持的参数
    data = {
        "url": params.get("pdf_url"),
    }
    
    # 添加可选参数
    if params.get("is_ocr") is not None:
        data["is_ocr"] = params["is_ocr"]
    if params.get("enable_formula") is not None:
        data["enable_formula"] = params["enable_formula"]
    if params.get("enable_table") is not None:
        data["enable_table"] = params["enable_table"]
    if params.get("language") is not None:
        data["language"] = params["language"]
    if params.get("data_id") is not None:
        data["data_id"] = params["data_id"]
    if params.get("callback") is not None:
        data["callback"] = params["callback"]
    if params.get("seed") is not None:
        data["seed"] = params["seed"]
    if params.get("extra_formats") is not None:
        data["extra_formats"] = params["extra_formats"]
    if params.get("page_ranges") is not None:
        data["page_ranges"] = params["page_ranges"]
    if params.get("model_version") is not None:
        data["model_version"] = params["model_version"]
    
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
                    "请求参数": data,
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