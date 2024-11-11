import fal_client
# 提交任务并获取处理器句柄
handler = fal_client.submit(
    "fal-ai/lora",
    arguments={
        "model_name": "stabilityai/stable-diffusion-xl-base-1.0",
        "prompt": "photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"
    },
)

# 使用 handler.get() 方法来同步获取结果
try:
    # 使用 handler.get() 方法来同步获取结果
    result = handler.get()
    print("任务完成，输出结果:", result)

except Exception as e:
    # 捕获并打印错误信息
    print(f"发生错误: {e}")
    if hasattr(e, 'response'):
        print(f"响应错误信息: {e.response.text}")

#以上是使用fal.ai提供的模型.
