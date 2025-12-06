import yaml

def generate_frontmatter(chapter_id, title, description, version, author):
    frontmatter = {
        "id": chapter_id,
        "title": title,
        "description": description,
        "version": version,
        "author": author,
    }
    return "---\n" + yaml.dump(frontmatter, sort_keys=False) + "---"

def generate_content_structure(chapter_title, sections):
    content = f"# {chapter_title}\n\n"
    for section in sections:
        content += f"## {section}\n\n"
    return content

if __name__ == "__main__":
    # Chapter 004 details
    chapter_id = "004"
    title = "Introduction to Humanoid Robotics and VLA Systems"
    description = "An overview of humanoid robotics, focusing on anatomy, control, and the integration of Vision-Language-Action (VLA) systems for advanced robotic intelligence."
    version = "1.0"
    author = "Fiza"
    sections = [
        "Learning Objectives",
        "Introduction",
        "Humanoid Robot Anatomy",
        "Control Systems for Humanoids",
        "VLA Systems Overview",
        "Challenges and Future Directions",
        "Summary",
        "Glossary (optional)",
    ]

    front_matter_content = generate_frontmatter(chapter_id, title, description, version, author)
    content_structure = generate_content_structure(title, sections)

    full_chapter_content = front_matter_content + content_structure
    print(full_chapter_content)
