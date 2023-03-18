import os
import glob
import argparse
import openai
from bs4 import BeautifulSoup

openai.api_key = '' # 替换成你的OpenAI API密钥

def translate_file(file_path, target_language):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    for tag in soup.find_all():
        if tag.string:
            translated_text = translate_text(tag.string, target_language)
            tag.string.replace_with(translated_text)
    
    with open(file_path, 'w') as f:
        f.write(str(soup))
    
def translate_text(text, target_language):
    prompt = f"translate the following text from english to {target_language}: {text},only translate text and cannot interpret it."
    response = openai.Completion.create(
        engine="text-davinci-002", 
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=20,
    )
    translation = response.choices[0].text.strip()
    return translation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='input directory containing SGML files')
    parser.add_argument('output_dir', help='output directory for translated SGML files')
    parser.add_argument('target_language', help='target language for translation (e.g. "zh" for Chinese)')
    args = parser.parse_args()

    input_dir = args.input_dir.rstrip('/')
    output_dir = args.output_dir.rstrip('/')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_path in glob.glob(f'{input_dir}/*.sgml'):
        file_name = os.path.basename(file_path)
        output_path = f'{output_dir}/{file_name}'
        translate_file(file_path, args.target_language)
        print(f'Translated {file_path} to {output_path}')
    
if __name__ == '__main__':
    main()