# ChatGPT_translate_sgml
- 这个脚本使用了BeautifulSoup库来处理SGML文件，并使用Google Translate API进行翻译。
- 用户可以指定输入和输出文件夹，以及目标语言。
- 脚本会遍历输入文件夹中的所有SGML文件，并将它们翻译成目标语言后输出到输出文件夹中。
- 在翻译过程中，脚本会忽略标签之间的内容，并只翻译标签内的文本内容。

- This script uses the BeautifulSoup library to process SGML files and the Google Translate API for translation. 
- Users can specify input and output folders, as well as the target language. 
- The script will iterate through all SGML files in the input folder and output them in the target language to the output folder. 
- During translation, the script ignores the content between tags and only translates the text content within the tags.

# How to use
python3 translate_sgml.py 'source_file_path' 'target_file_path' 'target_language'

> python3 translate_sgml.py '/Users/jim/Documents/TestDemo' '/Users/jim/Documents/TestDemo' 'zh'

# Prompt
translate the following SGML text to {target_language},only translate text and cannot interpret it,do not translate the SGML tags.: {text}
