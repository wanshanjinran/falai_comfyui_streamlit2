import fal_client 

#可以用subscibe_sample来检查有没有连接上fal.ai,如果连上了，subscribe_sample能返回如下的结果。
#result={'outputs': {'9': {'images': [{'filename': 'ComfyUI_00004_.png', 'subfolder': '', 'type': 'output', 'url': 'https://fal.media/files/zebra/sf8CiI1xvdvm1hUNkm1gJ_ComfyUI_00004_.png'}]}}, 'fal_outputs': {}, 'timings': {}}
#image_list=traverse_for_images(result)
#print(image_list)
def subscribe_sample():
    # 提交任务并返回同步请求句柄
    request_handle = fal_client.submit(
        "comfy/AI-Team/i2itry",
        arguments={
            "loadimage_1": "https://helios-i.mashable.com/imagery/articles/02EieRZxQn7dBCDxCoN4mxR/hero-image.fill.size_1248x702.v1730926276.jpg",
            "prompt": "photograph of victorian woman with wings, sky clouds, meadow grass"
        }
    )
    result=request_handle.get()
   # print("任务结果",result)
    return result

def subscribe_i2itry(input_image,input_text):
    
    # 提交任务并返回同步请求句柄
    request_handle = fal_client.submit(
        "comfy/AI-Team/i2itry",
        arguments={
            "loadimage_1":input_image,
            "prompt": input_text
        }
    )
    result=request_handle.get()
    print("任务结果",result)
    return result

def traverse_for_images(result):
    image_list = []
    if isinstance(result,dict):
        for key,value in result.items():
            if key=="images" and isinstance(value,list):
                for image in value:
                    if isinstance(image,dict) and 'url' in image:
                        image_list.append(image['url'])
            elif isinstance(value, (dict, list)):
                image_list.extend(traverse_for_images(value))
    elif isinstance(result, list):
        for item in result:
            image_list.extend(traverse_for_images(item))    
    return image_list

def output_images(prompt):
    if isinstance(prompt,dict):
        result=subscribe_i2itry(prompt["image"],prompt["text"])
        image_list=traverse_for_images(result)
        return image_list
    else:
        print("promopt结构错误")
