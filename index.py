import numpy as np
import figpack.views as fpv
import figpack
import os
import figpack_slides as fps

def example_1_view_type(metadata: dict, markdown: str) -> figpack.FigpackView:
    """Example custom view: damped sine wave."""
    plot_color = metadata.get("plot-color", "#FF0000")

    # Create a simple timeseries
    graph = fpv.TimeseriesGraph(y_label="Amplitude")

    # Generate data
    t = np.linspace(0, 10, 500)
    y = np.sin(2 * np.pi * t) * np.exp(-t / 5)

    # Add line series
    graph.add_line_series(
        name="Damped Sine",
        t=t.astype(np.float32),
        y=y.astype(np.float32),
        color=plot_color
    )

    return graph

def main():
    with open("index.md", "r") as f:
        md_content = f.read()

    theme_color = "#4A90E2"  # Example theme color
    theme = fps.create_theme_default_1(
        title_bg_color=theme_color,
        header_bg_color=theme_color,
        footer_bg_color=theme_color,
        custom_view_types={
            'example-1': example_1_view_type
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
