import os
from jinja2 import Environment, FileSystemLoader

class SiteGenerator:
    def __init__(self, output_base_dir="generated_sites", template_dir="templates"):
        self.output_base_dir = output_base_dir
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def create_site_structure(self, business_name: str):
        """Creates the basic folder structure for a React site."""
        slug = business_name.lower().replace(" ", "-")
        site_path = os.path.join(self.output_base_dir, slug)

        # Create directories
        os.makedirs(os.path.join(site_path, "src", "components"), exist_ok=True)
        os.makedirs(os.path.join(site_path, "public"), exist_ok=True)

        return site_path

    def generate_files(self, site_data: dict):
        """Generates React files based on the extracted AI data."""
        business_name = site_data.get("business_name", "My Site")
        business_type = site_data.get("business_type", "business")
        site_path = self.create_site_structure(business_name)

        # 1. Generate App.jsx
        template = self.env.get_template("App.jsx.j2")
        # Add dynamic hero image based on business type
        image_keywords = {
            "restaurant": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=1200&auto=format&fit=crop",
            "portfolio": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?q=80&w=1200&auto=format&fit=crop",
            "ecommerce": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?q=80&w=1200&auto=format&fit=crop",
            "saas": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop"
        }
        site_data["hero_image"] = image_keywords.get(business_type.lower(), "https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=1200&auto=format&fit=crop")

        app_content = template.render(data=site_data)
        with open(os.path.join(site_path, "src", "App.jsx"), "w", encoding="utf-8") as f:
            f.write(app_content)

        # 2. Generate index.css (for theme/colors)
        template = self.env.get_template("index.css.j2")
        css_content = template.render(data=site_data)
        with open(os.path.join(site_path, "src", "index.css"), "w", encoding="utf-8") as f:
            f.write(css_content)

        # 3. Generate package.json
        template = self.env.get_template("package.json.j2")
        pkg_content = template.render(data=site_data)
        with open(os.path.join(site_path, "package.json"), "w", encoding="utf-8") as f:
            f.write(pkg_content)

        # 4. Generate index.html
        template = self.env.get_template("index.html.j2")
        html_content = template.render(data=site_data)
        with open(os.path.join(site_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

        # 5. Generate main.jsx
        template = self.env.get_template("main.jsx.j2")
        main_content = template.render(data=site_data)
        with open(os.path.join(site_path, "src", "main.jsx"), "w", encoding="utf-8") as f:
            f.write(main_content)

        # 6. Generate tailwind.config.js
        template = self.env.get_template("tailwind.config.js.j2")
        tw_content = template.render(data=site_data)
        with open(os.path.join(site_path, "tailwind.config.js"), "w", encoding="utf-8") as f:
            f.write(tw_content)

        # 7. Generate postcss.config.js
        template = self.env.get_template("postcss.config.js.j2")
        post_content = template.render(data=site_data)
        with open(os.path.join(site_path, "postcss.config.js"), "w", encoding="utf-8") as f:
            f.write(post_content)

        return site_path
