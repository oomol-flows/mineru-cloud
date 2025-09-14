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
    if not params.get("api_token"):
        raise ValueError("api_token 参数不能为空")
    
    if not params.get("task_id"):
        raise ValueError("task_id 参数不能为空")
    
    token = params["api_token"]
    task_id = params["task_id"]
    max_retries = params.get("max_retries") or 1800
    
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
            
            # 打印详细调试信息
            print(f"状态码: {status_code}, 任务状态: {task_state}, 重试次数: {retry_count + 1}")
            print(f"完整任务数据: {task_data}")
            
            # 如果API返回错误状态码，记录详细信息
            if status_code != 200:
                print(f"API返回非200状态码: {status_code}, 响应数据: {response_data}")
                # 但不立即抛出异常，继续尝试获取任务状态
            
            # 如果任务成功完成，退出循环
            if task_state == "done":
                print(f"任务完成，最终状态: {task_state}")
                break
                
            # 如果任务失败，抛出异常并包含详细错误信息
            if task_state in ["failed", "error", "cancelled"]:
                err_msg = task_data.get("err_msg", "")
                if err_msg:
                    raise RuntimeError(f"MinerU任务失败: {err_msg} (状态: {task_state})")
                else:
                    raise RuntimeError(f"任务状态异常，状态: {task_state}")
                
            # 如果任务处于等待或处理状态，继续轮询
            if task_state in ["waiting", "pending", "processing", "running", "queued", "started"]:
                print(f"任务处理中，状态: {task_state}")
            else:
                # 对于未知状态，记录日志但继续轮询
                print(f"遇到未知状态，继续轮询: {task_state}")
                
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
        raise RuntimeError(error_msg)
    except RuntimeError:
        # MinerU API 错误直接重新抛出，不包装
        raise
    except Exception as e:
        error_msg = f"处理响应时出错: {str(e)}"
        raise RuntimeError(error_msg)