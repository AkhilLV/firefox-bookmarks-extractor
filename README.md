## Firefox bookmark extractor

### Why to use

Bookmarks can be tagged in firefox, but there is no way to export them by tags. This tools takes in an exported bookmark[html] file and outputs filtered bookmarks as a JSON file

### How to use

```
git clone ...
python main.py <bookmark_file_path> <tag1> <tag2> ...

where

bookmark_file_path: Export bookmarks from firefox to get a .html file
tag1, tag2: tags to filter by
```
