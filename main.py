import requests
import json
import os
from datetime import datetime

# 从环境变量中获取 Key（为了安全，不要直接把 Key 写在代码里传到网上去）
# 如果你实在觉得麻烦，也可以直接写：webhook_key = "你的key"
webhook_key = os.environ.get("WECHAT_WEBHOOK_KEY")


def send_wechat_msg():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={webhook_key}"
    headers = {"Content-Type": "application/json"}

    # 获取当前日期
    today = datetime.now().strftime("%Y-%m-%d")

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"""
### 🔔 温馨提醒: 每日工作通知
**日期**: <font color=\"info\">{today}</font>
**事项**:
> 1. 记得填写夸夸榜！
> 2. 祝大家工作顺利！💪
            """
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"响应结果: {response.text}")
    except Exception as e:
        print(f"发送出错: {e}")


if __name__ == "__main__":
    if webhook_key:
        send_wechat_msg()
    else:
        print("错误：未找到 Webhook Key，请检查 GitHub Secrets 设置。")