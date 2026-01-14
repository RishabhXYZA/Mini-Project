import os

BASE_DIR = "."

def get_next_project_number():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
        return 1

    existing = [
        d for d in os.listdir(BASE_DIR)
        if d.startswith("project-") and d[8:].isdigit()
    ]

    numbers = [int(d.split("-")[1]) for d in existing]
    return max(numbers) + 1 if numbers else 1

def create_new_project():
    project_num = get_next_project_number()
    project_name = f"project-{project_num:02d}"
    project_path = os.path.join(BASE_DIR, project_name)

    os.makedirs(project_path)

    with open(os.path.join(project_path, "main.py"), "w") as f:
        f.write("# Entry point for this mini project\n")

    with open(os.path.join(project_path, "README.md"), "w") as f:
        f.write(f"# Mini Project {project_num}\n\nProject description goes here.\n")

    print(f"✅ Created {project_name} successfully!")

if __name__ == "__main__":
    create_new_project()
