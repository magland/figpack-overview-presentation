import numpy as np
import figpack.views as fpv
import figpack as fp
import os
import figpack_slides as fps

def execute_view(metadata: dict, markdown: str) -> fp.FigpackView:
    caption = metadata.get('caption', None)
    caption_font_size = metadata.get('font-size', 24)
    # Extract code from markdown - find content between ```python and ```
    code_lines = []
    in_code_block = False
    for line in markdown.split('\n'):
        if line.strip() == '```python':
            in_code_block = True
            continue
        elif line.strip() == '```':
            in_code_block = False
            continue
        if in_code_block:
            code_lines.append(line)
    
    code = '\n'.join(code_lines)
    
    namespace = {}
    
    # Execute the code in the namespace
    exec(code, namespace)

    # Get the view from the namespace
    view = namespace['view']

    if caption is not None:
        view = fpv.CaptionedView(
            view=view,
            caption=caption,
            font_size=caption_font_size
        )

    return view

def main():
    with open("index.md", "r") as f:
        md_content = f.read()

    theme_color = "#4A90E2"  # Example theme color
    theme = fps.create_theme_default_1(
        title_bg_color=theme_color,
        header_bg_color=theme_color,
        footer_bg_color=theme_color,
        custom_view_types={
            'execute-view': execute_view
        }
    )

    slides = fps.create_presentation(
        md_content, 
        theme=theme
    )

    slides.save("build", title=slides.title)

    if os.environ.get("UPLOAD_FIGURE") == "1":
        slides.show(upload=True, title=slides.title, open_in_browser=True)

if __name__ == "__main__":
    main()
