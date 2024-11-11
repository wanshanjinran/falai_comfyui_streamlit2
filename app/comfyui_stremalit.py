import streamlit as st
import sync_falai_comfyui as sfc
from io import BytesIO
import base64
import os
#设置环境
os.environ['FAL_KEY'] = 'your fal key'
print(os.environ['FAL_KEY'])
st.title("接入falai的comfyui流程")
"图片数据调试"
#x = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
#if x is not None:
#    image_bytes = x.read()  # 获取字节数据
#st.write(image_bytes)
#st.write(x)
#byte_data = BytesIO(x.read())
#img_base64 = base64.b64encode(image_bytes).decode("utf-8")
#st.write(byte_data)


image=st.file_uploader("原始图片", type=["png", "jpg", "jpeg"],key='input_image')
if image:
    st.image(image)
text=st.text_area("正向提示词",key='input_text')
denoise=st.slider("denoise值",0.0,1.0,0.1,key="input_denoise")

# 如果上传了图片并且没有在session_state中设置过图片，存入session_state
if image is not None and 'input_image' not in st.session_state:
    st.session_state.input_image = image

# 如果有文本输入，存入session_state
if text and 'input_text' not in st.session_state:
    st.session_state.input_text = text
# 如果有denoise输入，存入session_state
if text and 'input_text' not in st.session_state:
    st.session_state.input_denoise = denoise

# 准备要传递给生成函数的提示信息
prompt = {
    'image': st.session_state.input_image,
    'text': st.session_state.input_text,
    'denoise':st.session_state.input_denoise
}

def generate_image(prompt):
    if prompt['image'] is not None and prompt['text']:
        # 将上传的图片转换为字节流
        img_bytes = prompt['image'].read()
        img_IO=BytesIO(prompt['image'].read())
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")  # 转为base64编码
        
        # 将图片和文本传递给 `falai` API
        result = sfc.output_images({
            'image': f"data:image/jpg;base64,{img_base64}",  # 将base64编码的图片传递给API
            'text': prompt['text'],
            'denoise':prompt['denoise']
        })
        

        # 显示生成的图像
        if result:
            st.image(result, caption="生成的图像", use_column_width=True)
        else:
            st.error("未能生成图像，请检查输入。")
    else:
        st.error("请上传图片并输入提示词。")


# 按钮触发图生图生成
if st.button("图生图生成按钮", key='i2i_generate_button'):
    generate_image(prompt)


#测试成功
#result=cgf.subscribe()
#image_list=cgf.traverse_for_images(result)
#st.write(image_list)
#st.image(image_list[0]) 