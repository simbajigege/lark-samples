import json

def extract_api_info(input_file, output_file):
    """
    从输入的JSON文件中提取API的name, detail, bizTag信息，并保存到输出文件中。

    :param input_file: 输入的JSON文件路径
    :param output_file: 输出的JSON文件路径
    """
    # 读取原始JSON文件
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 提取所需信息
    api_info_list = []
    for api in data['data']['apis']:
        api_info = {
            'name': api.get('name'),
            'detail': api.get('detail'),
            'bizTag': api.get('bizTag')
        }
        api_info_list.append(api_info)

    # 将提取的信息保存到新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(api_info_list, outfile, ensure_ascii=False, indent=4)

    print(f"API信息已成功提取并保存到'{output_file}'文件中。")

def extract_api_info_by_biz(input_file, output_file, biz_tags):
    """
    根据bizTag列表过滤并提取API信息,保存到输出文件中。
    如果API的bizTag与biz_tags列表中的任何一个匹配，该API将被提取。

    :param input_file: 输入的JSON文件路径
    :param output_file: 输出的JSON文件路径 
    :param biz_tags: 要过滤的业务标签列表
    """
    # 读取原始JSON文件
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 提取指定bizTag的API信息
    filtered_api_info = []
    for api in data['data']['apis']:
        if api.get('bizTag') in biz_tags:
            api_info = {
                'name': api.get('name'),
                #'detail': api.get('detail'), 
                'bizTag': api.get('bizTag')
            }
            filtered_api_info.append(api_info)

    # 将过滤后的信息保存到新文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_api_info, outfile, ensure_ascii=False, indent=4)

    print(f"已成功提取bizTag在{biz_tags}列表中的API信息并保存到'{output_file}'文件中。")


if __name__ == "__main__":
    # 如果直接执行脚本，使用默认的文件路径
    input_file = 'feishu API list.json'
    output_file = 'extracted_api_info.json'
    filtered_output_file = 'filtered_api_info.json'
    extract_api_info(input_file, output_file)
    # 使用多个bizTag进行过滤
    # 使用多个bizTag进行过滤
    biz_tags = ['ccm']
    extract_api_info_by_biz(input_file, filtered_output_file, biz_tags)