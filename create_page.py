# create_page.py
import sys
import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

try:
    # --- Arguments that will be passed from our n8n workflow ---
    page_type = sys.argv[1]      # e.g., "blog" or "service"
    page_title = sys.argv[2]     # The title of the new page
    html_content = sys.argv[3]   # The AI-generated article body
    blog_category = sys.argv[4]  # The category we added

    # --- Configuration ---
    # This loads the templates from the current folder
    env = Environment(loader=FileSystemLoader('.'))
    
    # Determine which template file to use
    template_name = f"{page_type}_template.html"
    template = env.get_template(template_name)

    # --- Prepare all the data for the placeholders ---
    # Create a URL-friendly filename (e.g., "my-new-post.html")
    slug = page_title.lower().replace(' ', '-').replace('&', 'and').replace('?', '')
    filename = f"{slug}.html"
    today_date = datetime.now().strftime("%B %d, %Y")

    template_data = {
        "PAGE_TITLE": page_title,
        "POST_DATE": today_date,
        "BLOG_CATEGORY": blog_category,
        "BLOG_CONTENT_HTML": html_content
    }

    # --- Render the final HTML by filling the template ---
    final_html = template.render(template_data)

    # --- Save the new HTML file to the correct folder ---
    output_folder = "blog" if page_type == "blog" else "."
    output_path = os.path.join(output_folder, filename)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    # Send a success message back to n8n
    print(f"Success: Created page at {output_path}")

except Exception as e:
    # If something goes wrong, send an error message
    print(f"Error: {e}")
    sys.exit(1)