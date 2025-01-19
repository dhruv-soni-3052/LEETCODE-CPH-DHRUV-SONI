import os
from bs4 import BeautifulSoup
import requests


def extract_testcases(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    testcases = []

    pre_tags = soup.find_all("pre")
    for pre in pre_tags:
        input_match = pre.find("strong", string="Input:")
        output_match = pre.find("strong", string="Output:")
        if input_match and output_match:
            input_value = input_match.next_sibling.strip() if input_match.next_sibling else ""
            output_value = output_match.next_sibling.strip() if output_match.next_sibling else ""
            testcases.append({"input": input_value, "output": output_value})

    if not testcases:
        examples = soup.find_all("div", class_="example-block")
        for example in examples:
            input_span = example.find("span", class_="example-io")
            output_span = input_span.find_next("span", class_="example-io") if input_span else None
            if input_span and output_span:
                input_value = input_span.get_text(strip=True)
                output_value = output_span.get_text(strip=True)
                testcases.append({"input": input_value, "output": output_value})

    return testcases


SCRAPERAPI_KEY = "afa2434ad69b8ba2196e99ab87fdf5d0"


def get_proxy():
    """Fetch a proxy IP using ScraperAPI."""
    proxy_url = f"http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url=http://httpbin.org/ip"
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            proxy_data = response.json()
            proxy_ip = proxy_data.get("origin")
            proxy_ip = proxy_ip.split()[-1]
            if proxy_ip:
                return f"http://{proxy_ip}"
    except requests.exceptions.RequestException as e:
        print(f"Failed to get proxy: {e}")
    return None


def get_problem_details(title_slug):
    """Fetch problem details using ScraperAPI for proxy rotation."""
    url = f"https://alfa-leetcode-api.onrender.com/select?titleSlug={title_slug}"
    proxy = get_proxy()

    if not proxy:
        print("No valid proxy available.")
        return None

    proxies = {
        "http": proxy,
        "https": proxy,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def extract_slug_from_url(url):
    segments = url.strip('/').split('/')
    try:
        for i in range(len(segments)):
            if segments[i] == "problems":
                return segments[i + 1]
    except:
        pass
    print("You entered an incorrect URL.")


def create_and_open_files(testcases):
    with open("input.txt", "w") as input_file, open("output.txt", "w") as output_file:
        for testcase in testcases:
            input_file.write(testcase["input"] + "\n")
            output_file.write(testcase["output"] + "\n")

    with open("solution.py", "w") as solution_file:
        pass 

    os.system("start input.txt")
    os.system("start output.txt")
    os.system("start solution.py")


s = input("Enter LeetCode problem URL: ")
slug = extract_slug_from_url(s)
if slug:
    print(f"Extracted slug: {slug}")
    problem_details = get_problem_details(slug)
    if problem_details:
        html_content = problem_details['question']
        testcases = extract_testcases(html_content)
        print("Extracted Testcases:", testcases)
        create_and_open_files(testcases)
    else:
        print("Failed to fetch problem details.")
else:
    print("Failed to extract slug.")
