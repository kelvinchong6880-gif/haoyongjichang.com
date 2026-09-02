import os

base_dir = r"c:\Users\USER\Desktop\haoyongjichang.com\src\pages"

replacements = {
    "edp02.civetaff.com/#/?code=CYg7QSJo": "edp01.civetaff.com/#/?code=CYg7QSJo"
}

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".astro"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            for old_str, new_str in replacements.items():
                new_content = new_content.replace(old_str, new_str)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Reverted affiliate links in {os.path.relpath(filepath, base_dir)}")

print(f"Total files reverted: {count}")
