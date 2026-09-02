import os
import json
from datetime import datetime, timezone, timedelta

src_pages = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages"
published_json_path = r"c:\Users\USER\Desktop\haoyongjichang.com\src\data\page-published.json"
lastmod_json_path = r"c:\Users\USER\Desktop\haoyongjichang.com\src\data\sitemap-lastmod.json"

# Current time in +08:00
tz = timezone(timedelta(hours=8))
current_time = datetime.now(tz).isoformat(timespec='seconds')

def get_valid_routes():
    routes = set()
    for root, dirs, files in os.walk(src_pages):
        for file in files:
            if file.endswith((".astro", ".md", ".mdx")):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, src_pages)
                
                # convert backslashes to forward slashes
                rel_path = rel_path.replace("\\", "/")
                
                # strip extension
                route = os.path.splitext(rel_path)[0]
                
                # handle index.astro
                if route == "index":
                    route = "/"
                elif route.endswith("/index"):
                    route = "/" + route[:-5]
                else:
                    route = "/" + route + "/"
                    
                routes.add(route)
    return routes

valid_routes = get_valid_routes()

def sync_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        old_data = json.load(f)
        
    new_data = {}
    
    # Process only valid routes
    for route in sorted(valid_routes):
        if route in old_data:
            new_data[route] = old_data[route]
        else:
            new_data[route] = current_time
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
        
    return len(new_data)

count1 = sync_json(published_json_path)
count2 = sync_json(lastmod_json_path)

print(f"Synced {count1} routes to page-published.json and {count2} routes to sitemap-lastmod.json")
