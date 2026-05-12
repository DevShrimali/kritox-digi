import os
import glob
import re

directories = ["tech", "case-studies"]

for dir_name in directories:
    for filepath in glob.glob(f"{dir_name}/*.html"):
        with open(filepath, "r") as f:
            content = f.read()
        
        # We look for the hero section, typically it's the first section after </nav>
        # Or look for `<section class="relative bg-white text-[#1F3D5A] pt-20...`
        # and replace `bg-white` with `bg-[#FFFBF0]`
        
        # We can just replace `<section class="relative bg-white` with `<section class="relative bg-[#FFFBF0]`
        # if it's the hero. Usually the first section in the body.
        
        # Better approach: find "Hero Section" comment and replace bg-white
        new_content = re.sub(
            r"(<!-- [A-Za-z ]*Hero Section[A-Za-z ]* -->\s*<section class=\"[^\"]*)bg-white",
            r"\1bg-[#FFFBF0]",
            content
        )
        
        if new_content != content:
            print(f"Updated {filepath}")
            with open(filepath, "w") as f:
                f.write(new_content)

