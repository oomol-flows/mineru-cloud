# region generated meta
import typing

class Inputs(typing.TypedDict):
    api_token: str
    task_id: str
    max_retries: typing.Optional[int]

class Outputs(typing.TypedDict):
    status_code: int
    response_data: dict
    task_data: dict

# endregion

import requests
import time
from oocana import Context

def main(params: Inputs, context: Context) -> Outputs:
    """
    从 MinerU API 获取 PDF 提取任务的结果
    
    Args:
        params: 包含 api_token 和 task_id 的输入参数
        context: OOMOL 上下文对象
        
    Returns:
        包含状态码、完整响应数据和任务结果数据的字典
    """
    token = params["api_token"]
    task_id = params["task_id"]
    max_retries = params.get("max_retries", 300)
    
    url = f"https://mineru.net/api/v4/extract/task/{task_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    try:
        # 轮询直到任务完成
        retry_count = 0
        
        while retry_count < max_retries:
            response = requests.get(url, headers=headers)
            status_code = response.status_code
            response_data = response.json()
            
            # 提取任务数据
            task_data = response_data.get("data", {})
            task_state = task_data.get("state", "")
            
            # 打印调试信息
            print(f"状态码: {status_code}, 任务状态: {task_state}, 重试次数: {retry_count + 1}")
            
            # 如果任务完成或失败，退出循环
            if task_state == "done" or task_state == "failed":
                print(f"任务完成，最终状态: {task_state}")
                break
                
            # 等待1秒后重试
            time.sleep(1)
            retry_count += 1
        
        # 如果达到最大重试次数仍未完成
        if retry_count >= max_retries:
            print("达到最大重试次数，任务仍未完成")
        
        return {
            "status_code": status_code,
            "response_data": response_data,
            "task_data": task_data
        }
        
    except requests.exceptions.RequestException as e:
        error_msg = f"请求失败: {str(e)}"
        print(error_msg)
        return {
            "status_code": 0,
            "response_data": {"error": error_msg},
            "task_data": {}
        }
    except Exception as e:
        error_msg = f"处理响应时出错: {str(e)}"
        print(error_msg)
        return {
            "status_code": 0,
            "response_data": {"error": error_msg},
            "task_data": {}
        }