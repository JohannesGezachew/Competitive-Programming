class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
        for path in paths:
            directory, *files = path.split()
        
            for file in files:
                name, content = file.split('(')
                content = content[:-1]
                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(f"{directory}/{name}")
        
        return [paths for paths in content_map.values() if len(paths) > 1]