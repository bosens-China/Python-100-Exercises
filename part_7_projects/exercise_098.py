"""
### 98. 网页内容抓取器

- **描述:** 使用 `requests` 获取一个指定网页（如博客文章）的 HTML 内容，然后使用 `BeautifulSoup4` 库（需 `pip install beautifulsoup4`）解析 HTML，并提取出网页的标题和所有段落文本。
- **提示:** `requests.get()` 获取页面，`BeautifulSoup(html, 'html.parser')` 解析，使用 `soup.title.string` 获取标题，`soup.find_all('p')` 获取所有段落。
- **期待:** 程序能打印出目标网页的标题和正文内容。
"""
import requests
from bs4 import BeautifulSoup
import sys
from typing import Tuple, List, Optional

def fetch_and_parse(url: str) -> Optional[BeautifulSoup]:
    """获取指定 URL 的 HTML 内容并用 BeautifulSoup 解析。"""
    # 在这里写下你的代码
    # 提示: 使用 requests.get, response.raise_for_status, 和 BeautifulSoup(...)
    raise NotImplementedError

def extract_title_and_paragraphs(soup: BeautifulSoup) -> Tuple[str, List[str]]:
    """从 BeautifulSoup 对象中提取标题和所有段落文本。"""
    # 在这里写下你的代码
    # 提示: 使用 soup.title.string 和 soup.find_all('p')
    raise NotImplementedError

def main():
    """主函数入口"""
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        print(f"正在抓取: {target_url}")
        
        soup = fetch_and_parse(target_url)
        
        if soup:
            title, paragraphs = extract_title_and_paragraphs(soup)
            print("\n" + "="*20)
            print(f"网页标题: {title}")
            print("="*20 + "\n")
            
            if paragraphs:
                print("提取到的段落:")
                for i, p_text in enumerate(paragraphs, 1):
                    print(f"[{i}] {p_text}\n")
            else:
                print("未能提取到任何段落。")
    else:
        print("用法: python exercise_098.py <URL>")
        print("例如: python exercise_098.py https://www.python.org")

if __name__ == "__main__":
    main() 