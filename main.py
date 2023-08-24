from bs4 import BeautifulSoup
import sys

if len(sys.argv) < 2:
    print("Please provide a file path")
    sys.exit(1)

file_path = sys.argv[1]
user_tags = sys.argv[2:]

with open("bookmarks.html", encoding="utf-8") as fp:
    html_doc = fp.read()

soup = BeautifulSoup(html_doc, 'html.parser')

data = []

for link in soup.find_all("a"):
    if ("tags" in link.attrs and link.attrs["tags"] in user_tags) or len(user_tags) == 0:
        data.append({
            "url": link.attrs["href"],
            "title": link.text
        })

with open("out.json", "w", encoding="utf-8") as fp:
    fp.write(str(data))

print("Bookmarks exported to out.json")
